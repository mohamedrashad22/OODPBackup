# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VeiwRentedBooks.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from DataBaseActions import Ui_Dialog
from  User import Login
global connection
connection = sqlite3.connect('test.db')


class Ui_Rent(object):
    MyDataBase = Ui_Dialog()

    def load_rented_content_view(self):
        self.x = Login.getInstance(self)
        #print(self.x.id)
        result = Ui_Rent.MyDataBase.ViewRent(self.x.id)
        print(result)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, columns_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(columns_data)))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(865, 458)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(105, 31, 661, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 380, 171, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.load_rented_content_view)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "View Rented Books"))


