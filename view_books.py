# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_books.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewBooks(object):
    def setupUi(self, viewBooks):
        viewBooks.setObjectName("viewBooks")
        viewBooks.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(viewBooks)
        self.centralwidget.setObjectName("centralwidget")
        self.book_name_label = QtWidgets.QLabel(self.centralwidget)
        self.book_name_label.setGeometry(QtCore.QRect(180, 50, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_name_label.setFont(font)
        self.book_name_label.setObjectName("book_name_label")
        self.book_name_value_label = QtWidgets.QLabel(self.centralwidget)
        self.book_name_value_label.setGeometry(QtCore.QRect(510, 50, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_name_value_label.setFont(font)
        self.book_name_value_label.setObjectName("book_name_value_label")
        self.book_desc_label = QtWidgets.QLabel(self.centralwidget)
        self.book_desc_label.setGeometry(QtCore.QRect(180, 190, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_desc_label.setFont(font)
        self.book_desc_label.setObjectName("book_desc_label")
        self.book_desc_value_label = QtWidgets.QLabel(self.centralwidget)
        self.book_desc_value_label.setGeometry(QtCore.QRect(510, 190, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_desc_value_label.setFont(font)
        self.book_desc_value_label.setObjectName("book_desc_value_label")
        self.next_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_book_button.setGeometry(QtCore.QRect(580, 440, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.next_book_button.setFont(font)
        self.next_book_button.setObjectName("next_book_button")
        self.rent_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.rent_book_button.setGeometry(QtCore.QRect(470, 340, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rent_book_button.setFont(font)
        self.rent_book_button.setObjectName("rent_book_button")
        self.favorite_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.favorite_book_button.setGeometry(QtCore.QRect(140, 340, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.favorite_book_button.setFont(font)
        self.favorite_book_button.setObjectName("favorite_book_button")
        viewBooks.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(viewBooks)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        viewBooks.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(viewBooks)
        self.statusbar.setObjectName("statusbar")
        viewBooks.setStatusBar(self.statusbar)

        self.retranslateUi(viewBooks)
        QtCore.QMetaObject.connectSlotsByName(viewBooks)

    def retranslateUi(self, viewBooks):
        _translate = QtCore.QCoreApplication.translate
        viewBooks.setWindowTitle(_translate("viewBooks", "MainWindow"))
        self.book_name_label.setText(_translate("viewBooks", "Book name"))
        self.book_name_value_label.setText(_translate("viewBooks", "value"))
        self.book_desc_label.setText(_translate("viewBooks", "Description"))
        self.book_desc_value_label.setText(_translate("viewBooks", "value"))
        self.next_book_button.setText(_translate("viewBooks", "Next Book"))
        self.rent_book_button.setText(_translate("viewBooks", "Rent"))
        self.favorite_book_button.setText(_translate("viewBooks", "Favorite"))


