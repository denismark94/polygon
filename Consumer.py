import queue
from datetime import datetime, timedelta

from RequestsFactory import DBReader
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
        self.db_reader = DBReader(1,2,3)
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
        # host = self.hosts[request.host].ip
        host = self.db_reader.get_ipaddress(request.host)[0]
        message = self.messages[request.message_id]
        # sender = self.db_re [message.sender]
        # ssh_credentials = sender.credentials[request.host].split(':')
        ssh_credentials = self.db_reader.get_ssh_credentials(message.sender, request.host)[0]
        # smtp_cred_id = message.protocol + len(self.hosts)
        # smtp_credentials = sender.credentials[smtp_cred_id].split(':')
        smtp_credentials = self.db_reader.get_protocol_credentials(message.sender, message.protocol)[0]

        # recipient_address = self.users[message.recipient].credentials[smtp_cred_id].split(":")[0]
        recipient_address = self.db_reader.get_protocol_credentials(message.recipient, message.protocol)[0][0]
        flag = message.flag
        sender_name = self.db_reader.get_username(message.sender)[0]
        # TODO Убрать заглушку
        # exit_code = self.stub(1)

        self.ssh_handler.connect(host=host, username=ssh_credentials[0],password=ssh_credentials[1])
        exit_code = self.ssh_handler.send(name=sender_name, sender_email=smtp_credentials[0],
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
        # host = self.hosts[request.host].ip
        host = self.db_reader.get_ipaddress(request.host)[0]
        message = self.messages[request.message_id]

        # recipient = self.users[message.recipient]
        ssh_credentials = self.db_reader.get_ssh_credentials(message.recipient, request.host)[0]
        smtp_credentials = self.db_reader.get_protocol_credentials(message.recipient, message.protocol)[0]
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
        self.db_reader.connect_sql_db()
        protocol_id = self.db_reader.get_protocol_id("smtp")
        user_ids = self.db_reader.get_protocol_users(protocol_id)
        available_machines = self.db_reader.get_available_machines(protocol_id)
        for user in user_ids:
            username = self.db_reader.get_username(user)[0]
            ssh_credentials = self.db_reader.get_ssh_credentials(user)
            for credential in ssh_credentials:
                host_id = credential[0]
                if host_id in available_machines:
                    ipaddress = self.db_reader.get_ipaddress(host_id)[0]
                    smtp_credentials = self.db_reader.get_protocol_credentials(user, protocol_id)
                    if smtp_credentials:
                        self.ssh_handler.connect(host=ipaddress, username=credential[1], password=credential[2])
                        self.ssh_handler.receive(name=smtp_credentials[0][0],password=smtp_credentials[0][1], msg_id='-1', erase=True)
                        self.ssh_handler.disconnect()
                        print("Почта для пользователя {0} на АРМ {1} очищена".format(username, ipaddress))

    def consume(self, requests, stat, safeprint, terminated):
        self.db_reader.connect_sql_db()
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


