# Form implementation generated from reading ui file 'D:\FoxScript\Poligon\Form\Ver1.0\Test.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setMinimumSize(QtCore.QSize(720, 480))
        MainWindow.setMaximumSize(QtCore.QSize(720, 480))
        MainWindow.setBaseSize(QtCore.QSize(720, 480))
        MainWindow.setStyleSheet("background-color: #1f2327")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 10, 69, 22))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.comboBox.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.comboBox.setStyleSheet("    background-color: #2d3237;\n"
"    border: 1px solid #292d32;\n"
"    border-radius: 8px;\n"
"    color: #ffffff")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 10, 101, 16))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #ffffff")
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 40, 69, 22))
        self.comboBox_2.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.comboBox_2.setStyleSheet("    background-color: #2d3237;\n"
"    border: 1px solid #292d32;\n"
"    border-radius: 8px;\n"
"    color: #ffffff")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #ffffff")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 75, 211, 16))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #ffffff")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(11, 15, 191, 16))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #ffffff")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 45, 191, 16))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #ffffff")
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 70, 80, 25))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border: 2px solid #292d32;\n"
"border-radius: 8px;\n"
"color: #ffffff\n"
"")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 10, 80, 25))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 2px solid #292d32;\n"
"border-radius: 8px;\n"
"color: #ffffff\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 40, 80, 25))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border: 2px solid #292d32;\n"
"border-radius: 8px;\n"
"color: #ffffff\n"
"")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 350, 701, 121))
        self.tableWidget_2.setStyleSheet("QTableWidget{\n"
"    border: 2px solid #292d32;\n"
"    border-radius: 10px;\n"
"    color: #ee3300\n"
"}\n"
"\n"
"QTableWidget::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: #ee3300\n"
"}")
        self.tableWidget_2.setDragEnabled(False)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(2, 2, item)
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(500, 10, 69, 22))
        self.comboBox_3.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.comboBox_3.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.comboBox_3.setStyleSheet("    background-color: #2d3237;\n"
"    border: 1px solid #292d32;\n"
"    border-radius: 8px;\n"
"    color: #ffffff")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(500, 39, 69, 22))
        self.comboBox_4.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.comboBox_4.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.comboBox_4.setStyleSheet("    background-color: #2d3237;\n"
"    border: 1px solid #292d32;\n"
"    border-radius: 8px;\n"
"    color: #ffffff")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: #ee3300;\n"
"    border: 1px solid #9e2504;\n"
"    border-radius: 8px;\n"
"    color: #ffffff\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"     background-color: #b2321e;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Alice"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Bob"))
        self.label_2.setText(_translate("MainWindow", "Отправитель:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Alice"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Bob"))
        self.label_3.setText(_translate("MainWindow", "Получатель:"))
        self.label_7.setText(_translate("MainWindow", "Пароль:"))
        self.label_4.setText(_translate("MainWindow", "IP адрес ARM:"))
        self.label_6.setText(_translate("MainWindow", "Имя ARM:"))
        self.lineEdit_4.setText(_translate("MainWindow", ""))
        self.lineEdit_2.setText(_translate("MainWindow", ""))
        self.lineEdit_3.setText(_translate("MainWindow", ""))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Admin"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Alice"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bob"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ARM 1"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ARM 2"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ARM 3"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Почта"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NP"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "Adm1244&Pas1"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MainWindow", "Adm1244&Pas2"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("MainWindow", "Adm1244&Pas3"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("MainWindow", "Ali1244&Pas1"))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("MainWindow", "Ali1244&Pas2"))
        item = self.tableWidget_2.item(1, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget_2.item(2, 0)
        item.setText(_translate("MainWindow", "Bob1244&Pas1"))
        item = self.tableWidget_2.item(2, 1)
        item.setText(_translate("MainWindow", "Bob1244&Pas2"))
        item = self.tableWidget_2.item(2, 2)
        item.setText(_translate("MainWindow", "-"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.comboBox_3.setItemText(0, _translate("MainWindow", "ARM 1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "ARM 2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "ARM 3"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "ARM 1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "ARM 2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "ARM 3"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
