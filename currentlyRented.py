# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'currentlyRented.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_currentlyRented(object):
    def setupUi(self, currentlyRented):
        currentlyRented.setObjectName("currentlyRented")
        currentlyRented.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(currentlyRented)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 80, 601, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sub_rented_books_list = QtWidgets.QListView(self.gridLayoutWidget)
        self.sub_rented_books_list.setObjectName("sub_rented_books_list")
        self.gridLayout.addWidget(self.sub_rented_books_list, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        currentlyRented.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(currentlyRented)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        currentlyRented.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(currentlyRented)
        self.statusbar.setObjectName("statusbar")
        currentlyRented.setStatusBar(self.statusbar)

        self.retranslateUi(currentlyRented)
        QtCore.QMetaObject.connectSlotsByName(currentlyRented)

    def retranslateUi(self, currentlyRented):
        _translate = QtCore.QCoreApplication.translate
        currentlyRented.setWindowTitle(_translate("currentlyRented", "MainWindow"))
        self.label.setText(_translate("currentlyRented", "Rented Books"))


