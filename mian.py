import sys
import time
import paramiko
import sqlite3
import random
import threading
import queue
import _thread
import configparser

from PyQt6 import QtGui
from GUI import Ui_MainWindow
from PyQt6 import QtWidgets, QtCore
from matplotlib import pyplot, animation

from RequestsFactory import *
from Consumer import Consumer
from Producer import Producer
import pyqtgraph as pg


# График
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


class Cor(QtWidgets.QMainWindow):

    arm_rand = ""
    passwor_rand = ""
    user_rand = ""
    db = 'db/BaseConnect.db'


    def __init__(self):
        super(Cor, self).__init__()
        self.real = False
        self.producing_thread = None
        self.consumer = None
        self.producer = None
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
        self.add_conLine()
        self.ts.btn_connect.clicked.connect(self.start_mon)
        self.ts.btn_stop.clicked.connect(self.stop_mon)
        self.ts.btn_conf.clicked.connect(self.donw_config)
        self.ts.btn_conf_add.clicked.connect(self.add_config)
        self.ts.btn_conf_del.clicked.connect(self.del_config)
        self.ts.chb_imitate.toggled.connect(self.upd_work_type)

    def upd_work_type(self):
        self.real = not self.ts.chb_imitate.isChecked()

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

        connection = sqlite3.connect(self.db)
        connection.close()

        # загружаем данные в db
        with sqlite3.connect(self.db) as db:
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
            self.ts.label_satus.setText("Выберите ARM")
            # print('Выберире ARM')

        #  Проверка галочки пользователя
        if self.ts.checkBox_9.isChecked() == True or self.ts.checkBox_10.isChecked() == True or self.ts.checkBox_11.isChecked() == True or self.ts.checkBox_12.isChecked() == True:
            flagUID_2 = True
        else:
            self.ts.label_satus.setText("Выберите Пользователя")
            # print('Выберире Пользователя')

        #  Проверка зполнеия полей
        if self.ts.le_delay.text() != "" and self.ts.le_num_of_thr.text() != "" and self.ts.le_num_of_msgs.text() != "":
            flagUID_3 = True
        else:
            self.ts.label_satus.setText("Заполните параметры отправки")
            # print('Заполните параметры отправки')

        if self.ts.le_delay.text() == ['A-Z']:
            self.ts.label_satus.setText("Буква")

        if flagUID_1 == True and flagUID_2 == True and flagUID_3 == True:
            self.start_mon()

    def donw_config(self):
        print("Загрузка конфига")
        config = configparser.ConfigParser()  # создаём объекта парсера
        config.read("Conf.ini")  # читаем конфиг
        donw_param = self.ts.comboBox_2.currentText()

        self.ts.le_delay.setText(str(config[donw_param]['Inter']))  # запись из ini в Edit
        self.ts.le_num_of_thr.setText(str(config[donw_param]['KolvoPot']))
        self.ts.le_num_of_msgs.setText(str(config[donw_param]['Post']))
        self.ts.le_chk_int.setText(str(config[donw_param]['InterChek']))
        self.ts.le_timeout.setText(str(config[donw_param]['Timeout']))
        if int(config[donw_param]['ARM1']) == 1:
            self.ts.checkBox.setChecked(True)
        else:
            self.ts.checkBox.setChecked(False)

        if int(config[donw_param]['ARM2']) == 1:
            self.ts.checkBox_2.setChecked(True)
        else:
            self.ts.checkBox_2.setChecked(False)

        if int(config[donw_param]['ARM3']) == 1:
            self.ts.checkBox_3.setChecked(True)
        else:
            self.ts.checkBox_3.setChecked(False)

        if int(config[donw_param]['ARM4']) == 1:
            self.ts.checkBox_4.setChecked(True)
        else:
            self.ts.checkBox_4.setChecked(False)

        if int(config[donw_param]['Alice']) == 1:
            self.ts.checkBox_9.setChecked(True)
        else:
            self.ts.checkBox_9.setChecked(False)

        if int(config[donw_param]['Bob']) == 1:
            self.ts.checkBox_10.setChecked(True)
        else:
            self.ts.checkBox_10.setChecked(False)

        if int(config[donw_param]['Claire']) == 1:
            self.ts.checkBox_11.setChecked(True)
        else:
            self.ts.checkBox_11.setChecked(False)

        if int(config[donw_param]['David']) == 1:
            self.ts.checkBox_12.setChecked(True)
        else:
            self.ts.checkBox_12.setChecked(False)

        self.ts.label_satus.setText("Файл конфигурации загружен")

    def add_config(self):
        config = configparser.ConfigParser()

        if self.ts.Conf_edit.text() != "":
            sector = self.ts.Conf_edit.text()

            self.ts.comboBox_2.addItem(sector)
            config.add_section(sector)

            Inter = self.ts.le_delay.text()
            config.set(sector, 'Inter', Inter)

            KolvoPot = self.ts.le_num_of_thr.text()
            config.set(sector, 'KolvoPot', KolvoPot)

            Post = self.ts.le_num_of_msgs.text()
            config.set(sector, 'Post', Post)

            InterChek = self.ts.le_chk_int.text()
            config.set(sector, 'InterChek', InterChek)

            timeout = self.ts.le_timeout.text()
            config.set(sector, 'timeout', timeout)

            if self.ts.checkBox.isChecked() == True:
                config.set(sector, 'ARM1', '1')
            else:
                config.set(sector, 'ARM1', '0')

            if self.ts.checkBox_2.isChecked() == True:
                config.set(sector, 'ARM2', '1')
            else:
                config.set(sector, 'ARM2', '0')

            if self.ts.checkBox_3.isChecked() == True:
                config.set(sector, 'ARM3', '1')
            else:
                config.set(sector, 'ARM3', '0')

            if self.ts.checkBox_4.isChecked() == True:
                config.set(sector, 'ARM4', '1')
            else:
                config.set(sector, 'ARM4', '0')

            if self.ts.checkBox_9.isChecked() == True:
                config.set(sector, 'Lynx', '1')
            else:
                config.set(sector, 'Lynx', '0')

            if self.ts.checkBox_10.isChecked() == True:
                config.set(sector, 'Fox', '1')
            else:
                config.set(sector, 'Fox', '0')

            config.sections()
            with open('Conf.ini', 'a') as config_file:
                config.write(config_file)
        else:
            self.ts.label_satus.setText("Введите название присета конфигурации")




        config.read('Conf.ini')

        conf_id = config['SETTINGS']['conf_id']
        del_arr = [0] * int(conf_id)

        # копирование блока settings часть с имеющимися присетами
        i = 0
        while i < int(conf_id):
            we = str(i + 1)
            del_arr[i] = config['SETTINGS'][we]
            i = i + 1
        # print(del_arr)

                                # добавление сета в общий список
        del_arr.append(sector)

        # удаление выбранного сектора и блока settings
        config.remove_section('SETTINGS')
        with open('Conf.ini', 'w') as config_file:
            config.write(config_file)

        # создали  блок settings и поле с кол-вом готовых сетов
        config.add_section('SETTINGS')
        config.set('SETTINGS', 'conf_id', str(len(del_arr)))



        # записали поля с оставшимися сетами
        print(del_arr)
        i = 1
        while i <= len(del_arr):
            we = str(i)
            config.set('SETTINGS', we, del_arr[i - 1])
            print(i)
            i = i + 1



        # сохранение изменений
        config.sections()
        with open('Conf.ini', 'w') as config_file:
            config.write(config_file)

        self.ts.Conf_edit.clear()
        self.ts.comboBox_2.clear()
        self.add_conLine()
        self.ts.label_satus.setText("Cет конфигурации сохранен")

    def del_config(self):
        config = configparser.ConfigParser()
        config.read('Conf.ini')
        conf_del = self.ts.comboBox_2.currentText()

        conf_id = config['SETTINGS']['conf_id']
        del_arr = [0] * int(conf_id)

        # копирование блока settings часть с имеющимися присетами
        i = 0
        while i < int(conf_id):
            we = str(i+1)
            del_arr[i] = config['SETTINGS'][we]
            i = i+1
        # print(del_arr)

        del_arr.remove(conf_del)

        # удаление выбранного сектора и блока settings
        config.remove_section('SETTINGS')
        config.remove_section(conf_del)
        with open('Conf.ini', 'w') as config_file:
            config.write(config_file)

        # создали  блок settings и поле с кол-вом готовых сетов
        config.add_section('SETTINGS')
        config.set('SETTINGS', 'conf_id', str(len(del_arr)))
        # записали поля с оставшимися сетами
        print(del_arr)
        i = 1
        while i <= len(del_arr):
            we = str(i)
            config.set('SETTINGS', we , del_arr[i-1])
            print(i)
            i = i+1

        config.sections()
        with open('Conf.ini', 'w') as config_file:
            config.write(config_file)

        self.ts.comboBox_2.clear()
        self.add_conLine()

        self.ts.label_satus.setText("Настройки конфигурации сохранен")

    def add_conLine(self):
        config = configparser.ConfigParser()  # создаём объекта парсера
        config.read("Conf.ini")
        conf_id = config['SETTINGS']['conf_id']
        # print(conf_id)

        i = 1
        while i <= int(conf_id):
            self.ts.comboBox_2.addItem(config['SETTINGS'][str(i)])
            i = i+1

    def start_mon(self):
        if self.check_input():
            self.ts.label_satus.setText("Загрузка программы")
            self.terminated = False
            print(self.real)
            if self.real:
                num_of_threads = int(self.ts.le_num_of_thr.text())
                num_of_msgs = int(self.ts.le_num_of_msgs.text())
                self.start_imit(num_of_msgs, num_of_threads)
            pb_thread = threading.Thread(target=self.update_progressbar, daemon=True)
            pb_thread.start()
            plot_thread = threading.Thread(target=self.update_plot, daemon=True)
            plot_thread.start()

    def stop_mon(self):
        self.terminated = True
        if self.real:
            self.producer.interrupted = True
            self.consumer.interrupted = True
        self.ts.label_satus.setStyleSheet("color: #ffffff")
        self.ts.label_satus.setText("Система остановлена")

    def start_imit(self, num_of_msgs, num_of_consumers):
        terminated = False
        messages = {}
        requests = queue.Queue()
        sent = []
        actions = ['Отправка', 'Получение']
        self.stat = []
        verbose = True
        picker = Picker(self.db)
        self.producer = Producer(picker, actions, sent)
        self.consumer = Consumer(self.db, messages, sent)
        # self.consumer.erase_mailboxes()
        safeprint = _thread.allocate_lock()
        self.producing_thread = threading.Thread(target=self.producer.produce,
                                            args=(num_of_msgs, messages, requests, safeprint, verbose, terminated))
        self.producing_thread.daemon = True
        self.producing_thread.start()
        self.consuming_threads = []
        for i in range(num_of_consumers):
            ct = threading.Thread(target=self.consumer.consume,
                                  args=(requests, self.stat, safeprint, terminated))
            ct.daemon = True
            ct.start()
            self.consuming_threads.append(ct)

    def check_input(self):
        self.ts.label_satus.setText("Проверка параметров работы")

        arm_selected = self.ts.checkBox.isChecked() or \
                    self.ts.checkBox_2.isChecked() or \
                    self.ts.checkBox_3.isChecked() or \
                    self.ts.checkBox_4.isChecked()

        user_selected = self.ts.checkBox_9.isChecked() or \
                    self.ts.checkBox_10.isChecked() or \
                    self.ts.checkBox_11.isChecked() or \
                    self.ts.checkBox_12.isChecked()

        fields_filled = (self.ts.le_delay.text() != '') and \
                        (self.ts.le_num_of_thr.text() != '') and \
                        (self.ts.le_num_of_msgs.text() != '') and \
                        (self.ts.le_chk_int.text() != '') and \
                        (self.ts.le_timeout.text() != '')
        if fields_filled:
            data_correct = int(self.ts.le_chk_int.text()) <= int(self.ts.le_timeout.text())
        if not arm_selected:
            self.ts.label_satus.setText("Выберите ARM")
            return False
        elif not user_selected:
            self.ts.label_satus.setText("Выберите Пользователя")
            return  False
        elif not fields_filled:
            self.ts.label_satus.setText("Заполните параметры отправки")
            return False
        elif not data_correct:
            self.ts.label_satus.setText("Интервал проверки превышает время имитации")
            return False
        return True

    def update_progressbar(self):
        self.ts.label_satus.setText("Имитация...")
        self.ts.label_satus.setStyleSheet("color: #ee3300")
        self.ts.progressBar.setValue(0)
        self.ts.progressBar.setMaximum(100)
        self.terminated = False
        timeout = int(self.ts.le_timeout.text()) * 60
        update_delay = timeout / 100
        for i in range(101):
            if self.terminated:
                print("execution aborted")
                self.ts.progressBar.setValue(0)
                self.terminated = False
                return
            time.sleep(update_delay)
            self.ts.progressBar.setValue(i)
        self.terminated = True
        self.ts.label_satus.setText("Имитация завершена")
        if self.real:
            self.producer.interrupted = True
            self.consumer.interrupted = True
            self.join_threads(self.producing_thread, self.consuming_threads)
            self.show_stat()

    def update_plot(self):
        timeout = int(self.ts.le_timeout.text()) * 60
        check_interval = int(self.ts.le_chk_int.text())
        probes = int(timeout / check_interval)
        print(probes)
        self.ts.GraphWidget.setXRange(0, probes + 1)
        self.set_grid(probes + 1)
        for i in range(probes):
            if self.terminated:
                return
            if self.real:
                print("Обработано:", self.consumer.processed)
                print("Отправлено:", self.consumer.sent_cnt)
                print("Принято:", self.consumer.received)
                print("Утеряно:", self.consumer.lost)
                print("Повреждено:", self.consumer.corrupted)
                self.y[i] = random.randint(0, 10) / 10
            else:
                self.y[i] = random.randint(0, 10) / 10
            self.line.setData(self.x, self.y)
            time.sleep(check_interval)

    def join_threads(self, producer_thread, consuming_threads):
        producer_thread.join()
        for ct in consuming_threads:
            ct.join()

    def show_stat(self):
        print("Статистика.")
        print("Обработано:", self.consumer.processed)
        print("Отправлено:", self.consumer.sent_cnt)
        print("Принято:", self.consumer.received)
        print("Утеряно:", self.consumer.lost)
        print("Повреждено:", self.consumer.corrupted)

    def set_grid(self, timeout):
        self.x = list(range(timeout))
        self.y = [1 for _ in range(timeout)]
        pen = pg.mkPen(color=(255, 0, 0))  # цвет контура в RGB
        self.ts.GraphWidget.clear()
        self.line = self.ts.GraphWidget.plot(
            self.x,
            self.y,
            name="Среднее значение",
            pen=pen,
        )


app = QtWidgets.QApplication([])
application = Cor()
application.show()
sys.exit(app.exec())