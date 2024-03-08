import sys
import sqlite3
import configparser
import demetra_ssh as ssh
from PyQt6 import QtWidgets
from Logger import logging
from Test import Ui_MainWindow


class Cor(QtWidgets.QMainWindow):
    def __init__(self):
        super(Cor, self).__init__()
        self.ts = Ui_MainWindow()
        self.ts.setupUi(self)
        self.init_UI()
        self.handler = ssh.SSHHandler()
        self.exit_code = 0


    def init_UI(self):
        self.setWindowTitle("Оператор")
        self.ts.btn_connect.clicked.connect(self.test)
        logging.info(f"Выполнена функция: init_UI")
    def get_config(self):
        # Подгрузка значений из конфигов. ToDo: нарисовать кнопку и забиндить функцию на нее
        config = configparser.ConfigParser()  # создаём объекта парсера
        config.read("Conf.ini")  # читаем конфиг
        self.ts.lineEdit_2.setText(config["SetWork"]["Inter"])        # запись из ini в Edit
        self.ts.lineEdit_3.setText(config["SetWork"]["KolvoPot"])
        self.ts.lineEdit_4.setText(config["SetWork"]["Post"])
        logging.info(f"Пользовательские значения загружены из файла конфигурации")

    def test(self):
        tasks_interval = self.ts.lineEdit_2.text()
        print("Интервал между письмами: {0}".format(tasks_interval))
        num_of_threads = self.ts.lineEdit_3.text()
        print("Общее число потоков: {0}".format(num_of_threads))
        num_of_msgs = self.ts.lineEdit_4.text()
        print("Общее число писем: {0}".format(num_of_msgs))

        host = "11.11.11.151"
        sender = "alice"
        secret = "123qweR%"
        self.handler.connect(host=host, username=sender, password=secret)

        code, output = self.handler.execute('cd ~ | ./info.sh')
        # code, output = self.handler.execute('ls -l')
        print("code: {0}".format(code))
        for i in output:
            print(i, end=" ")
        self.handler.disconnect()


def create_db():
    connection = sqlite3.connect('./Мусор/BaseID.db')
    connection.close()
    with sqlite3.connect('BaseID.db') as db:  # загружаем данные в db
        cursor = db.cursor()
        # создаём таблицы в db
        query = """ CREATE TABLE IF NOT EXISTS map_arm(
            id_user INTEGER, 
            UserN TEXT, 
            ARM1_log TEXT, 
            ARM1_pas TEXT,
            ARM2_log TEXT, 
            ARM2_pas TEXT,
            SERV_log TEXT, 
            SERV_pas TEXT
        )"""

        # заполняем поля в db
        query1 = """ INSERT INTO map_arm (
            id_user, UserN, ARM1_log, ARM1_pas, ARM2_log, ARM2_pas, SERV_log, SERV_pas
            ) VALUES(1, 'Alice', 'Arm1', 'Arm1qwer','Arm2', 'Arm2qwer','0', '0')"""
        query2 = """ INSERT INTO map_arm (
        id_user, UserN, ARM1_log, ARM1_pas,ARM2_log, ARM2_pas,SERV_log, SERV_pas
        ) VALUES(2, 'Bob', 'Arm1', 'Arm1qwer','Arm2', 'Arm2qwer','0', '0')"""

        # загружаем данные в db
        cursor.execute(query)
        cursor.execute(query1)
        cursor.execute(query2)
        logging.info(f"Загружены данные в db")


if __name__ == '__main__':
    create_db()
    app = QtWidgets.QApplication([])
    application = Cor()
    application.show()
    sys.exit(app.exec())
