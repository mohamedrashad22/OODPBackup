# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'favoriteitems.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_favoriteItems(object):
    def setupUi(self, favoriteItems):
        favoriteItems.setObjectName("favoriteItems")
        favoriteItems.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(favoriteItems)
        self.centralwidget.setObjectName("centralwidget")
        self.favorite_items_list = QtWidgets.QListView(self.centralwidget)
        self.favorite_items_list.setGeometry(QtCore.QRect(60, 60, 651, 451))
        self.favorite_items_list.setObjectName("favorite_items_list")
        self.favorite_items_label = QtWidgets.QLabel(self.centralwidget)
        self.favorite_items_label.setGeometry(QtCore.QRect(280, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.favorite_items_label.setFont(font)
        self.favorite_items_label.setObjectName("favorite_items_label")
        favoriteItems.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(favoriteItems)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        favoriteItems.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(favoriteItems)
        self.statusbar.setObjectName("statusbar")
        favoriteItems.setStatusBar(self.statusbar)

        self.retranslateUi(favoriteItems)
        QtCore.QMetaObject.connectSlotsByName(favoriteItems)
        self.favorite_items_list.add

    def retranslateUi(self, favoriteItems):
        _translate = QtCore.QCoreApplication.translate
        favoriteItems.setWindowTitle(_translate("favoriteItems", "MainWindow"))
        self.favorite_items_label.setText(_translate("favoriteItems", "Your Favorite Items"))


