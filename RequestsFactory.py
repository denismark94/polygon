import random
import time
from datetime import datetime, timedelta


# Класс - обертка для пользователей
class User:
    def __init__(self, data):
        self.name = data[0]
        self.credentials = data[1:]

# Класс - обертка для узлов сети
class Host:
    def __init__(self, data, status='online'):
        self.ip = data[0]
        self.protocols = data[1:]
        self.status = status
        self.timeout = datetime.now()

    def refresh_status(self):
        if self.timeout < datetime.now():
            self.status = 'online'

    def dos(self, timeout):
        self.status = 'offline'
        self.timeout = timeout


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
    def __init__(self, credsDB, hostsDB, protocolsDB):
        self.credsDB = credsDB
        self.hostsDB = hostsDB
        self.protocolsDB = protocolsDB

    # Метод считывает из файла и возвращает абстрактный набор данных
    def getDataset(self, path):
        dataset = []
        fileData = open(path, 'rt')
        for i in fileData:
            i = i.strip()
            dataset.append(i.split(','))
        return dataset

    # Метод извлекает и возвращает возвращает считанный из файла массив пользователей
    def getUsers(self):
        dataset = self.getDataset(self.credsDB)
        users = []
        for data in dataset:
            users.append(User(data))
        return users

    # Метод извлекает и возвращает возвращает считанный из файла массив узлов сети
    def getHosts(self):
        dataset = self.getDataset(self.hostsDB)
        hosts = []
        for data in dataset:
            hosts.append(Host(data))
        return hosts

    # Метод извлекает и возвращает возвращает считанный из файла массив протоколов обмена
    def getProtocols(self):
        return self.getDataset(self.protocolsDB)[0]

# Класс, содержащий правила подбора параметров запросов
class Picker:
    # На вход подается ранее сгенерированный список пользователей, машин и протоколов
    def __init__(self, users, protocols, hosts):
        self.users = users
        self.protocols = protocols
        self.hosts = hosts

    # Метод выводит случайного пользователя - отправителя (без ограничений)
    def getSender(self):
        return random.randint(0, len(self.users) - 1)

    # Метод подбирает протокол обмена под пользователя
    # Пользователь должен обладать учетной записью для обмена по выбранному протоколу
    def getProtocol(self, sender):
        index = random.randint(0, len(self.protocols) - 1)
        while(sender.credentials[len(self.hosts) + index] == '0'):
            index = random.randint(0, len(self.protocols) - 1)
        return index

    # Выбор узла, с которого будет осуществляться отправка/получение
    # Узел должен поддерживать выбранный протокол, у пользователя должны быть учтеная запись для доступа к узлу
    def getHost(self, user, protocol):
        host = random.randint(0, len(self.hosts) - 1)
        while(user.credentials[host] == '0' or self.hosts[host].protocols[protocol] == '0'):
            host = random.randint(0, len(self.hosts) - 1)
        return host

    # Выбор получателя сообщения
    # Получатель должен обладать учетной записью для обмена по выбранному протоколу
    def getRecipient(self, protocol):
        receiver = 0
        while (self.users[receiver].credentials[len(self.hosts) + protocol] == '0'):
            receiver = random.randint(0, len(self.users) - 1)
        return receiver


