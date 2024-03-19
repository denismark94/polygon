import queue
from matplotlib import pyplot, animation
import threading
import _thread

from RequestsFactory import *
from Consumer import Consumer
from Producer import Producer


# Запуск имитации с определенными пользователем параметрами
def start_imit(db, timeout, delay, num_of_msgs, num_of_consumers, terminated):
    # словарь под сгенерированные в ходе работы сообщения
    messages = {}
    # Очередь задач
    requests = queue.Queue()
    # Массив для сбора отправленных писем???
    sent = []
    # Набор действий для генерации и обработки запросов
    # actions = ['Отправка', 'Получение', 'Атака']
    actions = ['Отправка', 'Получение']
    # Массив для сбора статистики
    stat = []
    # Объект, выбирающий подходящих пользователей и машины в зависимости от матрицы доступа
    picker = Picker(db)
    # Объект, генерирующий задачи
    producer = Producer(picker, actions, sent)
    # Объект, выполняющий задачи
    consumer = Consumer(db, messages, sent)
    # Очистка почтовых ящиков всех пользователей
    consumer.erase_mailboxes()
    # Объект для потокобезопасной печати в консоль
    safeprint = _thread.allocate_lock()
    # Создание потока для генерации задач
    producing_thread = threading.Thread(target=producer.produce,
                                        args=(num_of_msgs, messages, requests, safeprint, verbose, terminated))
    producing_thread.daemon = True
    producing_thread.start()
    # Создание нескольких потоков- обработчиков задач
    consuming_threads = []
    for i in range(num_of_consumers):
        ct = threading.Thread(target=consumer.consume,
                                                args=(requests, stat, safeprint, terminated))
        ct.daemon = True
        ct.start()
        consuming_threads.append(ct)
    return producing_thread, consuming_threads, consumer


def stop_imit(interrupt):
    interrupt = True


def join_threads(producer_thread, consuming_threads):
    producer_thread.join()
    for ct in consuming_threads:
        ct.join()


def show_stat(consumer):
    print("Статистика.")
    print("Обработано:", consumer.processed)
    print("Отправлено:", consumer.sent_cnt)
    print("Принято:", consumer.received)
    print("Утеряно:", consumer.lost)
    print("Повреждено:", consumer.corrupted)


if __name__ == '__main__':
    verbose = True
    timeout = 1000
    delay = 60
    num_of_msgs = 50
    num_of_consumers = 1
    terminated = {'value': False}
    db = 'db/BaseConnect.db'
    print('Генерация запросов')
    prod_t, cons_ts, consumer = start_imit(db, timeout, delay, num_of_msgs, num_of_consumers, terminated)
    # time.sleep(15)
    # print("2.1. Прерывание имитации")
    # stop_imit(terminated)
    #
    join_threads(prod_t, cons_ts)
    print('3. Вывод результатов')
    show_stat(consumer)