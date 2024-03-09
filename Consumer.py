import queue
from datetime import datetime, timedelta
from SSHHandler import SSHHandler

class Consumer:

    def __init__(self,hosts, users, messages, sent) -> None:
        super().__init__()
        self.hosts = hosts
        self.users = users
        self.messages = messages
        self.sent = sent
        from RequestsFactory import Host
        self.server = Host(['11.11.11.141', '1', '1'])
        self.ssh_handler = SSHHandler()
        self.sent_cnt = 0
        self.received = 0
        self.lost = 0
        self.corrupted = 0
        self.processed = 0

    def refresh_hosts(self):
        self.server.refresh_status()

    def getRequest(self, requests, safeprint):
        self.refresh_hosts()
        # request = requests.pop(0)
        request = requests.get(block=False)
        if request.type == 0:
            self.send(request, safeprint)
        elif request.type == 1:
            self.receive(request, safeprint)
        else:
            self.attack(safeprint)

    def stub(self, seconds=3):
        import time
        time.sleep(seconds)
        return 0

    def send(self, request, safeprint):
        host = self.hosts[request.host].ip
        message = self.messages[request.message_id]
        sender = self.users[message.sender]
        ssh_credentials = sender.credentials[request.host].split(':')
        smtp_cred_id = message.protocol + len(self.hosts)
        smtp_credentials = sender.credentials[smtp_cred_id].split(':')
        recipient_address = self.users[message.recipient].credentials[smtp_cred_id].split(":")[0]
        flag = message.flag

        # TODO Убрать заглушку
        # exit_code = self.stub(1)
        self.ssh_handler.connect(host=host, username=ssh_credentials[0],password=ssh_credentials[1])
        exit_code = self.ssh_handler.send(name=sender.name, sender_email=smtp_credentials[0],
                                                  recipient_email=recipient_address,password=smtp_credentials[1],
                                                  msg_id='{0}'.format(message.id),flag='{0:08b}'.format(flag))
        self.ssh_handler.disconnect()
        if exit_code == 0:
            self.messages[request.message_id].sent = True
            self.sent.append(request.message_id)
            self.sent_cnt += 1
        with safeprint:
            print("==========Обработка===========")
            print(request.actions_ru[request.type] + '...')
            print("ID сообщения: {0:08b}\nФлаг: {1:08b}".format(message.id, flag))
            if exit_code == 0:
                print("Отправка завершилась успешно")
            else:
                print("Не удалось отправить сообщение", exit_code)
            print("==============================")

    def receive(self, request, safeprint):
        host = self.hosts[request.host].ip
        message = self.messages[request.message_id]
        recipient = self.users[message.recipient]
        ssh_credentials = recipient.credentials[request.host].split(':')
        smtp_credentials = recipient.credentials[message.protocol].split(':')
        # TODO Убрать заглушку
        # exit_code = self.stub(1)
        # flag = "{0:08b}".format(message.flag)
        self.ssh_handler.connect(host=host, username=ssh_credentials[0], password=ssh_credentials[1])
        print("ID сообщения: {0}".format(request.message_id))
        exit_code, flag = self.ssh_handler.receive(name=smtp_credentials[0], password=smtp_credentials[1],
                                                   msg_id='{0}'.format(request.message_id))
        self.ssh_handler.disconnect()
        if exit_code == 0:
            if "{0:08b}".format(message.flag) == flag:
                self.received += 1
            else:
                self.corrupted += 1
        else:
            self.lost += 1
        self.processed += 1

        with safeprint:
            print("==========Обработка===========")
            print(request.actions_ru[request.type] + '...')
            if exit_code == 0:
                print("Сообщение с флагом {0} получено".format(flag))
                print("Эталонный флаг: {0:08b}".format(message.flag))
                if "{0:08b}".format(message.flag) == flag:
                    print("Целостность флага не была нарушена")
                else:
                    print("Внимание! Целостность ресурса нарушена. Флаги не совпадают")
            else:
                print("Сообщение получить не удалось")
            print("==============================")

    def attack(self, safeprint):
        self.refresh_hosts()
        if self.server.status == 'online':
            self.server.dos(datetime.now() + timedelta(seconds = 10))
        with safeprint:
            print("==========Обработка===========")
            # print(request.actions_ru[request.type] + '...')
            print("==============================")

    def erase_mailboxes(self):
        protocol_id = 0
        for user in self.users:
            host = 0
            ssh_credentials = []
            smtp_credentials = user.credentials[len(self.hosts) + protocol_id].split(':')
            for i in range(len(self.hosts)):
                if user.credentials[i] != '0':
                    host = self.hosts[i].ip
                    ssh_credentials = user.credentials[i].split(':')
                    break

            self.ssh_handler.connect(host=host,username=ssh_credentials[0],password=ssh_credentials[1])
            self.ssh_handler.receive(name=smtp_credentials[0],password=smtp_credentials[1], msg_id='-1', erase=True)
            self.ssh_handler.disconnect()

    def consume(self, requests, stat, safeprint, terminated):
        i = 0
        import time
        while not (terminated['value'] and requests.empty()):
            if requests.empty():
                continue
            if i > 0 and i % 5 == 0:
                if self.processed:
                    stat.append(self.received / self.processed)
                else:
                    stat.append(0)
            self.getRequest(requests, safeprint)
            print('Отправленных сообщений: {0}'.format(len(self.sent)))

            i += 1


