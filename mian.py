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

with sqlite3.connect('BaseID.db') as db:            # загружаем данные в db
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
        #self.setWindowIcon('путь к фоточке')
        self.ts.pushButton.clicked.connect(self.copy_text)


    def copy_text(self):
          config = configparser.ConfigParser()  # создаём объекта парсера
          config.read("Conf.ini")  # читаем конфиг
          print(config["Logi"]["ip_add"])
          print(config["Logi"]["password"])
          print("___________________________________________________________")
          # print(config["SetWork"]["KolvoPot"])
          # print(config["SetWork"]["Post"])

          # self.ts.lineEdit_2.setText(config["SetWork"]["Inter"])        # запись из ini в Edit
          # self.ts.lineEdit_3.setText(config["SetWork"]["KolvoPot"])
          # self.ts.lineEdit_4.setText(config["SetWork"]["Post"])




          text = self.ts.lineEdit_2.text()              # чтение с Edit
          host = text
          text = self.ts.lineEdit_3.text()              # чтение с Edit
          sender = text
          text = self.ts.lineEdit_4.text()              # чтение с Edit
          secret = text


          for i in range(int(secret)):
              print('------->', i)
              print(host)
              print(sender)
              print(secret)
              time.sleep(int(host))  # Задержка на заданное число
              # тут должно быть что-то типо получены ли данные или нет, если не получчили то ждём пока будут

# ------------------------------------------------------------------------------------------------------------------------------------тут отправка и работа с ssh
              # recipient = 'lynx2'
              # self.connect(host=host, username=sender, password=secret)
              # code = self.send(name=sender, sender_email=sender, recipient_email=recipient, password=secret)
              # print(code)
              # self.disconnect()
#------------------------------------------------------------------------------------------------------------------------------------тут отправка и работа с ssh


          # texTab = QtGui.QTextItem('dfsg')
          # self.ts.tableWidget_2.setItem(1, 1, texTab)
          #
          # self.ts.lineEdit_3.setText(text)              # запись в Edit
#------------------------------------------------------------------------------------------------------------------------------------тут отправка и работа с ssh
    # def connect (self, host, username, password): #функция отетственна за подключение ssh: ssh lynx@192.168.10.17 + password
    #     self.exit_code = 0
    #     try:
    #         self.client.connect(hostname=host, username=username, password=password, timeout=10)
    #     except TimeoutError:
    #         print('Timeout reached while connecting to {0}'.format(host), file=sys.stderr)
    #         self.exit_code = 3
    #
    # def disconnect(self): #exit в ssh
    #     self.client.close()
    #
    # def execute(self, command): #прямое исполнение кода в командной строке
    #     stdin, stdout, stderr = self.client.exec_command(command)
    #     exit_code = stdout.channel.recv_exit_status()
    #     output = stdout.readlines()
    #     return exit_code, output
    #
    # def send(self, name, sender_email, recipient_email, password, verbose=True):
    #     # exit codes: 0 - ok, 1 - error, 3 - connection timeout
    #     if not self.exit_code:
    #         # command1 = './send.sh -n ' + name + \
    #         #           ' -r ' + recipient_email +  \
    #         #           ' -u ' + sender_email + \
    #         #           ' -p ' + password + \
    #         #           (' -v' if verbose else '')
    #         command1 = 'ifconfig'
    #         self.exit_code, output = self.execute(command1)
    #         if verbose:
    #             for i in output:
    #                 print(i, end='')
    #     return self.exit_code
    #
    # def receive(self, name, password, verbose=True, erase=True):
    #     # exit codes: 0 - ok, 1 - no messages, 2 - error, 3 - connection timeout
    #
    #     if not self.exit_code:
    #         command2 = './receive.sh -u ' + name + ' -p ' + password + ' -i '+ \
    #                   (' -v' if verbose else '') + (' -e' if erase else '')
    #         self.exit_code, output = self.execute(command2)
    #         if verbose:
    #             for i in output:
    #                 print(i, end='11')
    #         if self.exit_code == 0:
    #             print(i, end='22')
    #     return self.exit_code
#------------------------------------------------------------------------------------------------------------------------------------

app = QtWidgets.QApplication([])
application = Cor()
application.show()
sys.exit(app.exec())