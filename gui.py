import sys
import time
import paramiko
import sqlite3
import configparser
import random
import requests

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from Test import Ui_MainWindow

connection = sqlite3.connect('BaseID.db')
connection.close()

with sqlite3.connect('BaseID.db') as db:  # загружаем данные в db
    cursor = db.cursor()
    # создаём таблицы в db
    # quwery = """ CREATE TABLE IF NOT EXISTS protocols(id_prt INTEGER, prt TEXT)"""
    # quwery = """ CREATE TABLE IF NOT EXISTS hosts(id_host INTEGER, ip_host TEXT, prt_smtp TEXT, prt_ftp TEXT)"""
    # quwery = """ CREATE TABLE IF NOT EXISTS map_arm(id_user INTEGER, UserN TEXT, ARM1_log TEXT, ARM1_pas TEXT,
    #                                                                              ARM2_log TEXT, ARM2_pas TEXT,
    #                                                                              SERV_log TEXT, SERV_pas TEXT)"""
    # quwery = """ CREATE TABLE IF NOT EXISTS flagBase(id_flag INTEGER, flag TEXT)"""
    # cursor.execute(quwery)

    # заполняем поля в db
    # quwery1 = """ INSERT INTO protocols (id_prt, prt) VALUES(1, 'smtp')"""
    # quwery2 = """ INSERT INTO protocols (id_prt, prt) VALUES(2, 'ftp')"""

    # quwery1 = """ INSERT INTO hosts (id_host, ip_host, prt_smtp, prt_ftp) VALUES(1, '11.11.11.151', 'smtp', '0')"""
    # quwery2 = """ INSERT INTO hosts (id_host, ip_host, prt_smtp, prt_ftp) VALUES(2, '11.11.11.152', 'smtp', '0')"""

    # quwery1 = """ INSERT INTO map_arm (id_user, UserN, ARM1_log, ARM1_pas,
    #                                           ARM2_log, ARM2_pas,
    #                                           SERV_log, SERV_pas)
    #                           VALUES(1, 'Alice', 'Arm1', 'Arm1qwer',
    #                                              'Arm2', 'Arm2qwer',
    #                                              '0', '0')"""
    # quwery2 = """ INSERT INTO map_arm (id_user, UserN, ARM1_log, ARM1_pas,
    #                                           ARM2_log, ARM2_pas,
    #                                           SERV_log, SERV_pas)
    #                           VALUES(2, 'Bob', 'Arm1', 'Arm1qwer',
    #                                              'Arm2', 'Arm2qwer',
    #                                              '0', '0')"""
    # for i in range(20):
    # #   WORDS = random.randint(122, 123456778)  # значение от 122 до 123456778
    #     quwery = """ INSERT INTO flagBase (id_flag, flag) VALUES(1, 'WORDS')"""
    #     cursor.execute(quwery)

    # загружаем данные в db
    # cursor.execute(quwery)
    # cursor.execute(quwery1)
    # cursor.execute(quwery2)


# with sqlite3.connect('BaseID.db') as db:            # вывод данных в cdm
#     cursor = db.cursor()
#     cursor.execute("SELECT IDuser, * FROM IDhniki")
#     items = cursor.fetchall()
#     for el in items:
#         print(el[0], "  ", el[1], "  ", el[2], "  ", el[3])
#     db.commit()                                                       # обновляем db


class Cor(QtWidgets.QMainWindow):
    def __init__(self):
        super(Cor, self).__init__()
        self.ts = Ui_MainWindow()
        self.ts.setupUi(self)
        self.init_UI()

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.exit_code = 0

    def init_UI(self):
        self.setWindowTitle("Оператор")
        # self.setWindowIcon('путь к фоточке')
        self.ts.pushButton.clicked.connect(self.copy_text)
        self.load_from_config()

    def load_from_config(self):
        config = configparser.ConfigParser()  # создаём объекта парсера
        config.read("Conf.ini")  # читаем конфиг
        print("IP-адрес: {0}".format(config["Logi"]["ip_add"]))
        print("Пароль: {0}".format(config["Logi"]["password"]))
        print("Число потоков: {0}".format(config["SetWork"]["KolvoPot"]))
        print("Количество писем: {0}".format(config["SetWork"]["Post"]))
        print("Задержка: {0}".format(config["SetWork"]["Inter"]))

        self.ts.e_delay.setText(config["SetWork"]["Inter"])  # запись из ini в Edit
        self.ts.e_threads_amount.setText(config["SetWork"]["KolvoPot"])
        self.ts.e_messages_amount.setText(config["SetWork"]["Post"])

    def copy_text(self):
        delay = self.ts.e_delay.text()  # чтение с Edit
        threads_amount = self.ts.e_threads_amount.text()  # чтение с Edit
        msg_amount = self.ts.e_messages_amount.text()  # чтение с Edit
        host = "11.11.11.151"
        sender = "Alice"
        secret = "123qweR%"
        for i in range(int(msg_amount)):
            print('------->', i)
            print("host: {0}".format(host))
            print("sender: {0}".format(sender))
            print("password: {0}".format(secret))
            time.sleep(int(delay))  # Задержка на заданное число
            # тут должно быть что-то типо получены ли данные или нет, если не получчили то ждём пока будут


# ------------------------------------------------------------------------------------------------------------------------------------тут отправка и работа с ssh
# recipient = 'lynx2'
# self.connect(host=host, username=sender, password=secret)
# code = self.send(name=sender, sender_email=sender, recipient_email=recipient, password=secret)
# print(code)
# self.disconnect()
# ------------------------------------------------------------------------------------------------------------------------------------тут отправка и работа с ssh


# texTab = QtGui.QTextItem('dfsg')
# self.ts.tableWidget_2.setItem(1, 1, texTab)
#
# self.ts.lineEdit_3.setText(text)              # запись в Edit
# ------------------------------------------------------------------------------------------------------------------------------------тут отправка и работа с ssh

app = QtWidgets.QApplication([])
application = Cor()
application.show()
sys.exit(app.exec())