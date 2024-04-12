import random
import time
from datetime import datetime, timedelta
import sqlite3

# Класс - обертка для генерируемых сообщений
class Message:

    def __init__(self, id, sender, recipient, protocol):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.protocol = protocol
        self.flag = self.generateFlag()
        self.sent = False

    # Метод генерации случайного флага
    def generateFlag(self):
        return random.getrandbits(8)

# Класс - обертка для формируемых запросов
class Request:
    actions = ['send', 'receive','attack']
    actions_ru = ['Отправка', 'Получение','Атака']
    def __init__(self, type, host, message_id):
        self.type = type
        self.host = host
        self.message_id = message_id

# Класс, считывающий исходные данные из файлов
class DBReader:
    # Конструктор принимает ссылки на файлы с учетными данными, машинами и протоколами обмена
    # !!ВАЖНО!! Файлы должны быть согласованы!!
    def __init__(self, db):
        self.cursor = None
        self.db = db

    def connect_sql_db(self):
        # todo: Перенести путь к БД в параметр"
        self.cursor = sqlite3.connect(self.db).cursor()

    def get_protocol_id(self, protocol):
        query = "SELECT id_protocol FROM Tab_protocols where name = '{}'".format(protocol)
        return self.get_ids(query)[0]

    def get_protocol_name(self, protocol_id):
        query = "SELECT name FROM Tab_protocols where id_protocol = '{}'".format(protocol_id)
        return self.get_ids(query)[0]
    def get_uids(self):
        query = "SELECT id_user FROM Tab_user"
        return self.get_ids(query)

    def get_host_ids(self):
        query = "SELECT id_arm FROM Tab_arm"
        return self.get_ids(query)

    def get_protocol_users(self, protocol_id):
        query = "SELECT id_user FROM exchange_credentials where id_protocol = " + str(protocol_id)
        return self.get_ids(query)

    def get_ids(self, query):
        self.cursor.execute(query)
        ids = [x[0] for x in self.cursor.fetchall()]
        return ids

    def get_ssh_credentials(self, user_id, host_id=-1):
        if host_id == -1:
            query = "SELECT id_arm, login, password FROM ssh_credentials where id_user = " + str(user_id)
        else:
            query = "SELECT login, password FROM ssh_credentials where id_user = {0} and id_arm = {1}" \
                .format(user_id, host_id)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_available_machines(self, protocol_id):
        query = "SELECT id_arm FROM host_protocols_access where id_protocol = " + str(protocol_id)
        return self.get_ids(query)

    def get_ipaddress(self, host_id):
        query = "SELECT ip_addres FROM Tab_arm where id_arm = " + str(host_id)
        return self.get_ids(query)[0]

    def get_associated_hosts(self, user_id, protocol_id):
        query = "SELECT ssh_credentials.id_arm FROM ssh_credentials, host_protocols_access" \
                " WHERE ssh_credentials.id_user = {0} " \
                "and host_protocols_access.id_protocol = {1}".format(user_id, protocol_id)
        return self.get_ids(query)
    # Метод извлекает и возвращает возвращает считанный из файла массив протоколов обмена

    def get_associated_protocols(self, user_id):
        query = "SELECT id_protocol FROM exchange_credentials WHERE id_user = " + str(user_id)
        return self.get_ids(query)

    def get_recipients(self, sender_id, protocol_id):
        query = "SELECT id_user FROM exchange_credentials WHERE id_protocol = {0} and id_user != {1}".\
            format(protocol_id, sender_id)
        return self.get_ids(query)

    def get_protocol_credentials(self, user_id, protocol_id):
        query = "SELECT login, password FROM exchange_credentials WHERE id_protocol = {0} and id_user = {1}". \
            format(protocol_id, user_id)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_username(self, user_id):
        query = "SELECT name_user FROM Tab_user WHERE id_user = " + str(user_id)
        return self.get_ids(query)[0]

# Класс, содержащий правила подбора параметров запросов
class Picker:
    # На вход подается ранее сгенерированный список пользователей, машин и протоколов
    def __init__(self, db):
        self.dbreader = DBReader(db)
    # Метод выводит id случайного пользователя - отправителя (без ограничений)
    def get_sender_id(self):
        return random.choice(self.dbreader.get_uids())

    # Метод подбирает протокол обмена под пользователя
    # Пользователь должен обладать учетной записью для обмена по выбранному протоколу
    def get_protocol_id(self, user_id):
        protocols = self.dbreader.get_associated_protocols(user_id)
        return random.choice(protocols) if protocols else -1

    # Выбор узла, с которого будет осуществляться отправка/получение
    # Узел должен поддерживать выбранный протокол, у пользователя должны быть учтеная запись для доступа к узлу
    def get_host_id(self, user_id, protocol_id):
        hosts = self.dbreader.get_associated_hosts(user_id, protocol_id)
        return random.choice(hosts) if hosts else -1

    # Выбор получателя сообщения
    # Получатель должен обладать учетной записью для обмена по выбранному протоколу
    def get_recipient_id(self, sender_id, protocol_id):
        available_users = self.dbreader.get_recipients(sender_id, protocol_id)
        return random.choice(available_users) if available_users else -1