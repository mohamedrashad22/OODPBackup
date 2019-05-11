# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'returnDates.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_returnDates(object):
    def setupUi(self, returnDates):
        returnDates.setObjectName("returnDates")
        returnDates.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(returnDates)
        self.centralwidget.setObjectName("centralwidget")
        self.book_name_list = QtWidgets.QListView(self.centralwidget)
        self.book_name_list.setGeometry(QtCore.QRect(100, 160, 256, 192))
        self.book_name_list.setObjectName("book_name_list")
        self.return_date_list = QtWidgets.QListView(self.centralwidget)
        self.return_date_list.setGeometry(QtCore.QRect(430, 160, 256, 192))
        self.return_date_list.setObjectName("return_date_list")
        self.book_name_label = QtWidgets.QLabel(self.centralwidget)
        self.book_name_label.setGeometry(QtCore.QRect(170, 90, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.book_name_label.setFont(font)
        self.book_name_label.setObjectName("book_name_label")
        self.book_returnDate_label = QtWidgets.QLabel(self.centralwidget)
        self.book_returnDate_label.setGeometry(QtCore.QRect(490, 90, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.book_returnDate_label.setFont(font)
        self.book_returnDate_label.setObjectName("book_returnDate_label")
        returnDates.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(returnDates)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        returnDates.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(returnDates)
        self.statusbar.setObjectName("statusbar")
        returnDates.setStatusBar(self.statusbar)

        self.retranslateUi(returnDates)
        QtCore.QMetaObject.connectSlotsByName(returnDates)

    def retranslateUi(self, returnDates):
        _translate = QtCore.QCoreApplication.translate
        returnDates.setWindowTitle(_translate("returnDates", "MainWindow"))
        self.book_name_label.setText(_translate("returnDates", "Book Name"))
        self.book_returnDate_label.setText(_translate("returnDates", "Return Date"))


