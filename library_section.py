# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library_section.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_librarySection(object):
    def setupUi(self, librarySection):
        librarySection.setObjectName("librarySection")
        librarySection.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(librarySection)
        self.centralwidget.setObjectName("centralwidget")
        self.ageTypes = QtWidgets.QListView(self.centralwidget)
        self.ageTypes.setGeometry(QtCore.QRect(150, 30, 521, 192))
        self.ageTypes.setObjectName("ageTypes")
        self.chooseCat_label = QtWidgets.QLabel(self.centralwidget)
        self.chooseCat_label.setGeometry(QtCore.QRect(90, 290, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chooseCat_label.setFont(font)
        self.chooseCat_label.setObjectName("chooseCat_label")
        self.sub_view_items_button = QtWidgets.QPushButton(self.centralwidget)
        self.sub_view_items_button.setGeometry(QtCore.QRect(280, 410, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sub_view_items_button.setFont(font)
        self.sub_view_items_button.setObjectName("sub_view_items_button")
        self.cats_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.cats_combobox.setGeometry(QtCore.QRect(430, 310, 151, 22))
        self.cats_combobox.setObjectName("cats_combobox")
        librarySection.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(librarySection)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        librarySection.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(librarySection)
        self.statusbar.setObjectName("statusbar")
        librarySection.setStatusBar(self.statusbar)

        self.retranslateUi(librarySection)
        QtCore.QMetaObject.connectSlotsByName(librarySection)

    def retranslateUi(self, librarySection):
        _translate = QtCore.QCoreApplication.translate
        librarySection.setWindowTitle(_translate("librarySection", "MainWindow"))
        self.chooseCat_label.setText(_translate("librarySection", "Choose Category"))
        self.sub_view_items_button.setText(_translate("librarySection", "View items"))


