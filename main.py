import queue
from matplotlib import pyplot, animation
import threading
import _thread

from RequestsFactory import *
from Consumer import Consumer
from Producer import Producer


def visualise(stat):
    import numpy
    n = 1
    fig = pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    major_ticks = numpy.arange(0, 101, 20)
    minor_ticks = numpy.arange(0, 101, 5)

    def animate(n):
        xs = [i for i in range(len(stat))]
        ys = stat.copy()
        ax.clear()
        ax.set_xlim([0, 100])
        ax.set_ylim([0, 1.1])
        ax.set_xticks(range(0, 101, 10))
        ax.set_xticks(range(0, 101, 5), minor=True)
        ax.set_yticks(numpy.arange(0, 1.1, 0.2))
        ax.set_yticks(numpy.arange(0, 1.1, 0.1), minor=True)
        ax.grid(which="both")
        ax.plot(xs, ys)

    ani = animation.FuncAnimation(fig, animate, interval=100)
    pyplot.show()


# Запуск имитации с определенными пользователем параметрами
def start_imit(users, hosts, protocols, timeout, delay, num_of_msgs, num_of_consumers, terminated):
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
    picker = Picker(users, protocols, hosts)
    # Объект, генерирующий задачи
    producer = Producer(picker, actions, sent)
    # Объект, выполняющий задачи
    consumer = Consumer(hosts, users, messages, sent)
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
    print("Статистика.\nОтправлено: {0}\nОбработано: {1}\nПринято: {2}\nУтеряно: {3}\nПовреждено: {4}"
          .format(consumer.sent_cnt, consumer.processed, consumer.received, consumer.lost, consumer.corrupted))


def load_from_db():
    creds_path = r'./db/credentials'
    hosts_path = r'./db/hosts'
    protocols_path = r'./db/protocols'
    db_reader = DBReader(creds_path, hosts_path, protocols_path)
    users = db_reader.getUsers()
    protocols = db_reader.getProtocols()
    hosts = db_reader.getHosts()
    return users, protocols, hosts


def print_db(users, protocols, hosts):
    print("-----------------------------------")
    print('Пользователи:')
    for user in users:
        print('{0}: {1}'.format(user.name, user.credentials))
    print("-----------------------------------")
    print('Протоколы обмена:')
    print(protocols)
    print("-----------------------------------")
    print('Узлы сети:')
    for host in hosts:
        print('{0}: ['.format(host.ip), end='')
        for j in range(len(protocols) - 1):
            print('{0}:{1}'.format(protocols[j], host.protocols[j]), end=', ')
        print('{0}:{1}]'.format(protocols[len(protocols) - 1], host.protocols[len(protocols) - 1]))


if __name__ == '__main__':
    verbose = True
    timeout = 1000
    delay = 60
    num_of_msgs = 10
    num_of_consumers = 1
    terminated = {'value': False}

    print('1. Инициализация БД узлов сети, пользователей и протоколов обмена')
    users, protocols, hosts = load_from_db()
    if verbose:
        print_db(users, protocols, hosts)

    print('2. Генерация запросов')
    prod_t, cons_ts, consumer = start_imit(users,
                                           hosts,
                                           protocols,
                                           timeout,
                                           delay,
                                           num_of_msgs,
                                           num_of_consumers,
                                           terminated)


    time.sleep(15)
    print("2.1. Прерывание имитации")
    stop_imit(terminated)

    join_threads(prod_t, cons_ts)
    print('3. Вывод результатов')
    show_stat(consumer)