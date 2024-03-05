import sys
import time
import paramiko
import sqlite3
import configparser
import random
import requests
import threading

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from Test import Ui_MainWindow
from PyQt6 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg




# График
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        grid = QtWidgets.QGridLayout(self.centralwidget)
        grid.addWidget(self.graphWidget, 4, 7)
        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])


class Cor(QtWidgets.QMainWindow):

    arm_rand = ""
    passwor_rand = ""
    user_rand = ""
    # logg = ""

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
        self.ts.pushButton_2.clicked.connect(self.clic)

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


          if (host != '') or (sender != '') or (secret != ''):

            self.create_task()
            self.ts.progressBar.setProperty("value", 0)
            for i in range(int(secret)):
                print('--------------------------->', i+1)
                self.create_task()
                global arm_rand
                print(arm_rand)
                global user_rand
                print(user_rand)
                global passwor_rand
                print(passwor_rand)
                print(self.ts.comboBox.currentText())



                MaxBar = int(secret)
                self.ts.progressBar.setProperty("maximum", MaxBar)
                self.ts.progressBar.setProperty("value", i+1)
                time.sleep(int(host))  # Задержка на заданное число
          else:
              print('Заполните пустые поля')
              # тут должно быть что-то типо получены ли данные или нет, если не получчили то ждём пока будут

    def DB_create(self):
        print("Тут вот базы мутятся")
        connection = sqlite3.connect('BaseConnect.db')
        connection.close()

        # загружаем данные в db
        with sqlite3.connect('BaseConnect.db') as db:
            cursor = db.cursor()

        # создаём таблицы в db
        # quwery = """ CREATE TABLE IF NOT EXISTS Tab_arm(id_arm INTEGER, ip_addres TEXT)"""
        # cursor.execute(quwery)

        # заполняем поля в db
        #     quwery  = """ INSERT INTO Tab_user (id_user, name_user, passwor_user, protocol_user, access_id_arm) VALUES(1, 'lynx', 'kali', 'smtp', '2')"""
        #     cursor.execute(quwery)

        # вывод данных в cdm
        # with sqlite3.connect('BaseID.db') as db:
        #     cursor = db.cursor()
        #     cursor.execute("SELECT IDuser, * FROM IDhniki")
        #     items = cursor.fetchall()
        #     for el in items:
        #         print(el[0], "  ", el[1], "  ", el[2], "  ", el[3])
        #     db.commit()                                                       # обновляем db

    def create_task(self):
        global user_rand
        global passwor_rand
        global arm_rand

        connection = sqlite3.connect('BaseConnect.db')
        connection.close()

 # загружаем данные в db
        with sqlite3.connect('BaseConnect.db') as db:
            cursor = db.cursor()

        flagCnB = 0

#  Проверка галочки АРМ
        if self.ts.checkBox.isChecked() == False and self.ts.checkBox_2.isChecked() == False and self.ts.checkBox_3.isChecked() == False and self.ts.checkBox_4.isChecked() == False :
            print('Выберире ARM')
        else:
            arm = []
            if self.ts.checkBox.isChecked() == True:
                arm.append(1)
            if self.ts.checkBox_2.isChecked() == True:
                arm.append(2)
            if self.ts.checkBox_3.isChecked() == True:
                arm.append(3)
            if self.ts.checkBox_4.isChecked() == True:
                arm.append(4)

            random.shuffle(arm)
            arm_rand_id = str(random.choice(arm))
            # print(arm_rand_id)
            flagCnB = flagCnB + 1


#  Проверка галочки пользователя
        if self.ts.checkBox_9.isChecked() == False and self.ts.checkBox_10.isChecked() == False and self.ts.checkBox_11.isChecked() == False and self.ts.checkBox_12.isChecked() == False:
            print('Выберире Пользователя')
        else:
            use = []
            if self.ts.checkBox_9.isChecked() == True:
                use.append(1)
            if self.ts.checkBox_10.isChecked() == True:
                use.append(2)
            if self.ts.checkBox_11.isChecked() == True:
                use.append(3)
            if self.ts.checkBox_12.isChecked() == True:
                use.append(4)

            random.shuffle(use)
            user_rand_id = str(random.choice(use))
            # print(user_rand_id)
            flagCnB = flagCnB + 1


        if flagCnB == 2:
            serh = "SELECT name_user FROM Tab_user WHERE id_user = " + user_rand_id
            cursor.execute(serh)
            user_rand = cursor.fetchone()
            for user_rand in user_rand:
                user_rand = user_rand

            serh = "SELECT passwor_user FROM Tab_user WHERE id_user = " + user_rand_id
            cursor.execute(serh)
            passwor_rand = cursor.fetchone()
            for passwor_rand in passwor_rand:
                passwor_rand = passwor_rand

            serh = "SELECT ip_addres FROM Tab_arm WHERE id_arm = " + arm_rand_id
            cursor.execute(serh)
            arm_rand = cursor.fetchone()
            for arm_rand in arm_rand:
                arm_rand = arm_rand

    # def Thread(self): # Будет выступать в роли декоратора
    #     for i in range(5):
    #         print(i)
    #         time.sleep(5)
    # def Thread2(self): # Будет выступать в роли декоратора
    #     for i in range(5):
    #         print(i)
    #         time.sleep(5)

    def clic(self):
        # Создаем поток
        thread = threading.Thread(target=self.copy_text, daemon=True)
        # Запускаем поток
        thread.start()
        # Ожидаем завершения потока
        thread.join()
        print("Главный поток завершен")





# Работа с уддаенной машиной
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