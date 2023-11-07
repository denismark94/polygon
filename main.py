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


if __name__ == '__main__':
    verbose = False
    creds_path = r'./db/credentials'
    hosts_path = r'./db/hosts'
    protocols_path = r'./db/protocols'
    actions = ['Отправка', 'Получение', 'Атака']
    db_reader = DBReader(creds_path, hosts_path, protocols_path)
    messages = {}
    requests = queue.Queue()
    # requests = []
    sent = []
    print('1. Инициализация БД узлов сети, пользователей и протоколов обмена')
    users = db_reader.getUsers()
    protocols = db_reader.getProtocols()
    hosts = db_reader.getHosts()
    maliciousHost = Host(['11.11.11.69', '1', '1'])
    server = Host(['11.11.11.141', '1', '1'])
    if verbose:
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
    picker = Picker(users, protocols, hosts)
    producer = Producer(picker, sent, maliciousHost)
    consumer = Consumer(hosts, users, messages, sent, server)

    print('2. Генерация запросов')
    consumer.erase_mailboxes()

    safeprint = _thread.allocate_lock()
    stat = []
    terminated = {'value': False}
    producing_thread = threading.Thread(target=producer.produce, args=(100, messages, requests, safeprint, verbose,
                                                                       terminated))
    producing_thread.daemon = True
    producing_thread.start()

    consuming_thread = threading.Thread(target=consumer.consume, args=(requests, stat, safeprint, terminated))
    consuming_thread.daemon = True
    consuming_thread.start()

    visualise(stat)

    producing_thread.join()
    consuming_thread.join()

    consumer.erase_mailboxes()
    print("Статистика.\nОтправлено: {0}\nОбработано: {1}\nПринято: {2}\nУтеряно: {3}\nПовреждено: {4}"
          .format(consumer.sent_cnt, consumer.processed, consumer.received, consumer.lost, consumer.corrupted))
