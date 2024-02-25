import sys
import paramiko
import sqlite3
import configparser
import ssh
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from Test import Ui_MainWindow
#from scp import SCPClient

connection = sqlite3.connect('BaseID.db')
connection.close()

# ssh.logging.basicConfig(filename='log_file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with sqlite3.connect('BaseID.db') as db:            # загружаем данные в db
    cursor = db.cursor()
    # создаём таблицы в db
    # quwery = """ CREATE TABLE IF NOT EXISTS protocols(id_prt INTEGER, prt TEXT)"""
    # quwery = """ CREATE TABLE IF NOT EXISTS hosts(id_host INTEGER, ip_host TEXT, prt_smtp TEXT, prt_ftp TEXT)"""
    quwery = """ CREATE TABLE IF NOT EXISTS map_arm(id_user INTEGER, UserN TEXT, ARM1_log TEXT, ARM1_pas TEXT,
                                                                                 ARM2_log TEXT, ARM2_pas TEXT,
                                                                                 SERV_log TEXT, SERV_pas TEXT)"""

    # заполняем поля в db
    # quwery1 = """ INSERT INTO protocols (id_prt, prt) VALUES(1, 'smtp')"""
    # quwery2 = """ INSERT INTO protocols (id_prt, prt) VALUES(2, 'ftp')"""

    # quwery1 = """ INSERT INTO hosts (id_host, ip_host, prt_smtp, prt_ftp) VALUES(1, '11.11.11.151', 'smtp', '0')"""
    # quwery2 = """ INSERT INTO hosts (id_host, ip_host, prt_smtp, prt_ftp) VALUES(2, '11.11.11.152', 'smtp', '0')"""

    quwery1 = """ INSERT INTO map_arm (id_user, UserN, ARM1_log, ARM1_pas, 
                                              ARM2_log, ARM2_pas,
                                              SERV_log, SERV_pas) 
                              VALUES(1, 'Alice', 'Arm1', 'Arm1qwer',
                                                 'Arm2', 'Arm2qwer',
                                                 '0', '0')"""
    quwery2 = """ INSERT INTO map_arm (id_user, UserN, ARM1_log, ARM1_pas, 
                                              ARM2_log, ARM2_pas,
                                              SERV_log, SERV_pas) 
                              VALUES(2, 'Bob', 'Arm1', 'Arm1qwer',
                                                 'Arm2', 'Arm2qwer',
                                                 '0', '0')"""


    # загружаем данные в db
    cursor.execute(quwery)
    cursor.execute(quwery1)
    cursor.execute(quwery2)
    ssh.logging.info(f"Загружены данные в db")

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


        self.exit_code = 0

    def init_UI(self):
        self.setWindowTitle("Оператор")
        #self.setWindowIcon('путь к фоточке')
        self.ts.pushButton.clicked.connect(self.copy_text)
        ssh.logging.info(f"Выполнена функция: init_UI")

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
          print(host)
          text = self.ts.lineEdit_3.text()              # чтение с Edit
          sender = text
          print(sender)
          text = self.ts.lineEdit_4.text()              # чтение с Edit
          secret = text
          print(secret)

          recipient = 'lynx'
          path_reseption = '/home/lynx/Desktop/test.txt'
          path_sender = '/home/lynx/Desktop/test02'
          ssh.connect(host=host, username=sender, password=secret)
          #programming = self.send(name=sender, sender_email=sender, recipient_email=recipient, password=secret)
          #progr = self.send(name=sender, sender_email=sender, recipient_email=recipient, password=secret)
          progr = ssh.execute('cd ~ | ./info.sh')

          print(progr)
          print ("Hi")
          code, output = ssh.execute('ls -l')
          for i in output:
          	print (i, end =" ")
          ssh.disconnect()



          # texTab = QtGui.QTextItem('dfsg')
          # self.ts.tableWidget_2.setItem(1, 1, texTab)
          #
          # self.ts.lineEdit_3.setText(text)              # запись в Edit






app = QtWidgets.QApplication([])
application = Cor()
application.show()
sys.exit(app.exec())
