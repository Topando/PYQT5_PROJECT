# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnswerOptionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnswerOption(object):
    def setupUi(self, AnswerOption):
        AnswerOption.setObjectName("AnswerOption")
        AnswerOption.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AnswerOption)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 791, 471))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 500, 91, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 500, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 500, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 500, 201, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        AnswerOption.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnswerOption)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        AnswerOption.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnswerOption)
        self.statusbar.setObjectName("statusbar")
        AnswerOption.setStatusBar(self.statusbar)

        self.retranslateUi(AnswerOption)
        QtCore.QMetaObject.connectSlotsByName(AnswerOption)

    def retranslateUi(self, AnswerOption):
        _translate = QtCore.QCoreApplication.translate
        AnswerOption.setWindowTitle(_translate("AnswerOption", "MainWindow"))
        self.label_2.setText(_translate("AnswerOption", "Введите ответ"))
        self.pushButton.setText(_translate("AnswerOption", "Записать ответ"))
        self.pushButton_2.setText(_translate("AnswerOption", "Вернуться на предыдущую страницу"))