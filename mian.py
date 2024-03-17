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
        self.terminated = False
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.exit_code = 0


    def init_UI(self):
        self.setWindowTitle("Оператор")
        self.setWindowIcon(QtGui.QIcon('Logo.ico'))
        self.ts.btn_connect.clicked.connect(self.chek_UID)
        self.ts.btn_stop.clicked.connect(self.stop_mon)

    def copy_text(self):
        self.ts.label_satus.setText("Чтение данных")
        text = self.ts.lineEdit_2.text()              # чтение с Edit
        host = text
        text = self.ts.lineEdit_3.text()              # чтение с Edit
        sender = text
        text = self.ts.lineEdit_4.text()              # чтение с Edit
        secret = text






        if (host != '') or (sender != '') or (secret != ''):
            # self.create_task()
            self.ts.label_satus.setText("Система активна")
            self.ts.label_satus.setStyleSheet("color: #ee3300")

            self.ts.progressBar.setProperty("value", 0)
            for i in range(int(secret)):

                if self.terminated:
                    print("execution aborted")
                    self.ts.progressBar.setValue(0)
                    self.terminated = False
                    return

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
            print('Ошибка чтения данных')
            # тут должно быть что-то типо получены ли данные или нет, если не получчили то ждём пока будут


    def DB_create(self):
        print("Тут вот базы мутятся")
        connection = sqlite3.connect('db/BaseConnect.db')
        connection.close()

        # загружаем данные в db
        with sqlite3.connect('db/BaseConnect.db') as db:
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

        connection = sqlite3.connect('db/BaseConnect.db')
        connection.close()

 # загружаем данные в db
        with sqlite3.connect('db/BaseConnect.db') as db:
            cursor = db.cursor()

        flagCnB = 0

        arm = []
        arm.clear()
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



#  Проверка галочки пользователя
        use = []
        use.clear()
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

#  Создали запрос

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

    def chek_UID(self):
        self.ts.label_satus.setText("Проверка параметров работы")
        flagUID_1 = False
        flagUID_2 = False
        flagUID_3 = False

        #  Проверка галочки АРМ
        if self.ts.checkBox.isChecked() == True or self.ts.checkBox_2.isChecked() == True or self.ts.checkBox_3.isChecked() == True or self.ts.checkBox_4.isChecked() == True:
            flagUID_1 = True
        else:
            self.ts.label_satus.setText("Выберире ARM")
            # print('Выберире ARM')

        #  Проверка галочки пользователя
        if self.ts.checkBox_9.isChecked() == True or self.ts.checkBox_10.isChecked() == True or self.ts.checkBox_11.isChecked() == True or self.ts.checkBox_12.isChecked() == True:
            flagUID_2 = True
        else:
            self.ts.label_satus.setText("Выберире Пользователя")
            # print('Выберире Пользователя')

        #  Проверка зполнеия полей
        if self.ts.lineEdit_2.text() != "" and self.ts.lineEdit_3.text() != "" and self.ts.lineEdit_4.text() != "":
            flagUID_3 = True
        else:
            self.ts.label_satus.setText("Заполните параметры отправки")
            # print('Заполните параметры отправки')

        if self.ts.lineEdit_2.text() == ['A-Z']:
            self.ts.label_satus.setText("Буква")



        if flagUID_1 == True and flagUID_2 == True and flagUID_3 == True:
            self.start_mon()

    def start_mon(self):
        self.ts.label_satus.setText("Загрузка программы")

        # Создаем поток
        self.terminated = False
        thread = threading.Thread(target=self.copy_text, daemon=True)
        # Запускаем поток
        thread.start()

        # Ожидаем завершения потока
        # thread.join()
        # print("Главный поток завершен")
    def stop_mon(self):
        self.terminated = True
        self.ts.label_satus.setStyleSheet("color: #ffffff")
        self.ts.label_satus.setText("Система остановлена")



app = QtWidgets.QApplication([])
application = Cor()
application.show()
sys.exit(app.exec())