# Form implementation generated from reading ui file 'D:\FoxScript\Ver_2.0\MyWork\Test.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        MainWindow.setBaseSize(QtCore.QSize(1024, 600))
        MainWindow.setStyleSheet("background-color: #1f2327")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(99, 137, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
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
        self.label_2.setGeometry(QtCore.QRect(10, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #ffffff")
        self.label_2.setObjectName("label_2")
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
        self.lineEdit_4.setText("")
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
        self.lineEdit_2.setText("")
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
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 410, 1001, 141))
        self.tableWidget_2.setStyleSheet("QTableWidget{\n"
"    border: 2px solid #292d32;\n"
"    border-radius: 10px;\n"
"    color: #ee3300\n"
"}\n"
"\n"
"QTableWidget::chunk{\n"
"    border: 2px solid #292d32;\n"
"    border-radius: 10px;\n"
"    background-color: #ee3300\n"
"}")
        self.tableWidget_2.setDragEnabled(False)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
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
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 10))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_2.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_2.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_2.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_2.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_2.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_2.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_2.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_2.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_2.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_2.setItem(2, 6, item)
        self.btn_connect = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_connect.setGeometry(QtCore.QRect(230, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.btn_connect.setFont(font)
        self.btn_connect.setStyleSheet("QPushButton{\n"
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
        self.btn_connect.setCheckable(False)
        self.btn_connect.setChecked(False)
        self.btn_connect.setObjectName("btn_connect")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 15, 41, 20))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #ffffff")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 75, 41, 20))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #ffffff")
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 100, 80, 25))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border: 2px solid #292d32;\n"
"border-radius: 8px;\n"
"color: #ffffff\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 105, 41, 20))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #ffffff")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 105, 211, 16))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #ffffff")
        self.label_11.setObjectName("label_11")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 180, 91, 161))
        self.frame.setStyleSheet("border: 2px solid #292d32;\n"
"border-radius: 8px;\n"
"color: #ffffff\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 91, 21))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ffffff")
        self.label_5.setObjectName("label_5")
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBox.setGeometry(QtCore.QRect(11, 33, 66, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setTabletTracking(False)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(11, 63, 66, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(11, 93, 66, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(11, 123, 66, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, 180, 91, 161))
        self.frame_2.setStyleSheet("border: 2px solid #292d32;\n"
"border-radius: 8px;\n"
"color: #ffffff\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 91, 21))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #ffffff")
        self.label_13.setObjectName("label_13")
        self.checkBox_9 = QtWidgets.QCheckBox(parent=self.frame_2)
        self.checkBox_9.setGeometry(QtCore.QRect(11, 33, 66, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(parent=self.frame_2)
        self.checkBox_10.setGeometry(QtCore.QRect(11, 63, 66, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(parent=self.frame_2)
        self.checkBox_11.setGeometry(QtCore.QRect(11, 93, 66, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setText("")
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(parent=self.frame_2)
        self.checkBox_12.setGeometry(QtCore.QRect(11, 123, 66, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 560, 1001, 31))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setTabletTracking(False)
        self.progressBar.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.progressBar.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.progressBar.setToolTip("")
        self.progressBar.setStatusTip("")
        self.progressBar.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid #292d32;\n"
"    border-radius: 10px;\n"
"    color: #ffffff\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: #ee3300\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.btn_stop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(230, 310, 141, 31))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.btn_stop.setFont(font)
        self.btn_stop.setStyleSheet("QPushButton{\n"
"    background-color: #2d3237;\n"
"    border: 1px solid #292d32;\n"
"    border-radius: 8px;\n"
"    color: #ffffff\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"     background-color: #454b51;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.btn_stop.setObjectName("btn_stop")
        self.GraphWidget = PlotWidget(parent=self.centralwidget)
        self.GraphWidget.setGeometry(QtCore.QRect(380, 10, 631, 391))
        self.GraphWidget.setStyleSheet("border: 2px solid #292d32;\n"
"border-radius: 8px;\n"
"color: #ffffff\n"
"")
        self.GraphWidget.setObjectName("GraphWidget")
        self.label_satus = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_satus.setGeometry(QtCore.QRect(20, 370, 351, 21))
        font = QtGui.QFont()
        font.setFamily("GOST type B")
        font.setPointSize(12)
        self.label_satus.setFont(font)
        self.label_satus.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label_satus.setStyleSheet("color: #ffffff")
        self.label_satus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_satus.setObjectName("label_satus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "smtp"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ftp"))
        self.comboBox.setItemText(2, _translate("MainWindow", "http"))
        self.label_2.setText(_translate("MainWindow", "Протоколы:"))
        self.label_7.setText(_translate("MainWindow", "Кол-во отправленных писем:"))
        self.label_4.setText(_translate("MainWindow", "Интервал отправки писем:"))
        self.label_6.setText(_translate("MainWindow", "Количество потков:"))
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
        item.setText(_translate("MainWindow", "ARM 4"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SMTP"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "FTP"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "HTTP"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(0, 4)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(1, 4)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(2, 1)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(2, 2)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(2, 3)
        item.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_2.item(2, 4)
        item.setText(_translate("MainWindow", "+"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.btn_connect.setText(_translate("MainWindow", "Подключиться"))
        self.label_8.setText(_translate("MainWindow", "сек."))
        self.label_9.setText(_translate("MainWindow", "шт."))
        self.label_10.setText(_translate("MainWindow", "мин."))
        self.label_11.setText(_translate("MainWindow", "Интервал проверки:"))
        self.label_5.setText(_translate("MainWindow", "ПЭВМ:"))
        self.checkBox.setText(_translate("MainWindow", "ARM 1"))
        self.checkBox_2.setText(_translate("MainWindow", "ARM 2"))
        self.checkBox_3.setText(_translate("MainWindow", "ARM 3"))
        self.checkBox_4.setText(_translate("MainWindow", "ARM 3"))
        self.label_13.setText(_translate("MainWindow", "Польз."))
        self.checkBox_9.setText(_translate("MainWindow", "Lynx"))
        self.checkBox_10.setText(_translate("MainWindow", "Fox"))
        self.checkBox_12.setText(_translate("MainWindow", "Admin"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.btn_stop.setText(_translate("MainWindow", "Стоп"))
        self.label_satus.setText(_translate("MainWindow", "Ожидание..."))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
