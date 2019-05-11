# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'penalties.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.book_name_list = QtWidgets.QListView(self.centralwidget)
        self.book_name_list.setGeometry(QtCore.QRect(90, 230, 256, 192))
        self.book_name_list.setObjectName("book_name_list")
        self.book_penalty_label = QtWidgets.QLabel(self.centralwidget)
        self.book_penalty_label.setGeometry(QtCore.QRect(490, 160, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.book_penalty_label.setFont(font)
        self.book_penalty_label.setObjectName("book_penalty_label")
        self.book_penalty_list = QtWidgets.QListView(self.centralwidget)
        self.book_penalty_list.setGeometry(QtCore.QRect(420, 230, 256, 192))
        self.book_penalty_list.setObjectName("book_penalty_list")
        self.book_name_label = QtWidgets.QLabel(self.centralwidget)
        self.book_name_label.setGeometry(QtCore.QRect(160, 160, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.book_name_label.setFont(font)
        self.book_name_label.setObjectName("book_name_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.book_penalty_label.setText(_translate("MainWindow", "Penalty"))
        self.book_name_label.setText(_translate("MainWindow", "Book Name"))


