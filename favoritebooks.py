# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'favoritebooks.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_favoriteBooks(object):
    def setupUi(self, favoriteBooks):
        favoriteBooks.setObjectName("favoriteBooks")
        favoriteBooks.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(favoriteBooks)
        self.centralwidget.setObjectName("centralwidget")
        self.favorite_books_list = QtWidgets.QListView(self.centralwidget)
        self.favorite_books_list.setGeometry(QtCore.QRect(60, 60, 651, 451))
        self.favorite_books_list.setObjectName("favorite_books_list")
        self.favorite_books_label = QtWidgets.QLabel(self.centralwidget)
        self.favorite_books_label.setGeometry(QtCore.QRect(280, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.favorite_books_label.setFont(font)
        self.favorite_books_label.setObjectName("favorite_books_label")
        favoriteBooks.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(favoriteBooks)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        favoriteBooks.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(favoriteBooks)
        self.statusbar.setObjectName("statusbar")
        favoriteBooks.setStatusBar(self.statusbar)

        self.retranslateUi(favoriteBooks)
        QtCore.QMetaObject.connectSlotsByName(favoriteBooks)

    def retranslateUi(self, favoriteBooks):
        _translate = QtCore.QCoreApplication.translate
        favoriteBooks.setWindowTitle(_translate("favoriteBooks", "MainWindow"))
        self.favorite_books_label.setText(_translate("favoriteBooks", "Your Favorite Books"))


