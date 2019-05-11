# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subscriber_home.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from view_items import Ui_viewItems
from FavoritItem import Ui_View
from Panalties import Ui_Panalties
from rentItem import Ui_Rent
class Ui_subscriber_home(object):
    def GotoViewItems(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_viewItems()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()

    def GotoFav(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_View()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()
    def GotoRnt(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rent()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()
    def GotoPanalties(self):

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Panalties()
            self.ui.setupUi(self.window)
            # MainWindow.hide()
            self.window.show()
    def setupUi(self, subscriber_home):
        subscriber_home.setObjectName("subscriber_home")
        subscriber_home.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(subscriber_home)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(109, 30, 581, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.subhome_edit_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.subhome_edit_button.setObjectName("subhome_edit_button")
        self.verticalLayout.addWidget(self.subhome_edit_button)
        self.sub_home_choose_library_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sub_home_choose_library_button.setObjectName("sub_home_choose_library_button")
        self.verticalLayout.addWidget(self.sub_home_choose_library_button)
        self.sub_home_favorite_books_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sub_home_favorite_books_button.setObjectName("sub_home_favorite_books_button")
        self.verticalLayout.addWidget(self.sub_home_favorite_books_button)
        self.sub_home_currentlyRented_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sub_home_currentlyRented_button.setObjectName("sub_home_currentlyRented_button")
        self.verticalLayout.addWidget(self.sub_home_currentlyRented_button)
        #self.sub_home_returnDates_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #self.sub_home_returnDates_button.setObjectName("sub_home_returnDates_button")
        #self.verticalLayout.addWidget(self.sub_home_returnDates_button)
        self.sub_home_penalties_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sub_home_penalties_button.setObjectName("sub_home_penalties_button")
        self.verticalLayout.addWidget(self.sub_home_penalties_button)
        subscriber_home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(subscriber_home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        subscriber_home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(subscriber_home)
        self.statusbar.setObjectName("statusbar")
        subscriber_home.setStatusBar(self.statusbar)

        self.retranslateUi(subscriber_home)
        QtCore.QMetaObject.connectSlotsByName(subscriber_home)
        self.sub_home_choose_library_button.clicked.connect(self.GotoViewItems)
        self.sub_home_favorite_books_button.clicked.connect(self.GotoFav)
        self.sub_home_currentlyRented_button.clicked.connect(self.GotoRnt)
        self.sub_home_penalties_button.clicked.connect(self.GotoPanalties)

    def retranslateUi(self, subscriber_home):
        _translate = QtCore.QCoreApplication.translate
        subscriber_home.setWindowTitle(_translate("subscriber_home", "MainWindow"))
        self.subhome_edit_button.setText(_translate("subscriber_home", "Edit profile Info"))
        self.sub_home_choose_library_button.setText(_translate("subscriber_home", "Choose Library section"))
        self.sub_home_favorite_books_button.setText(_translate("subscriber_home", "Favorite Books [saved]"))
        self.sub_home_currentlyRented_button.setText(_translate("subscriber_home", "Currently rented"))
        #self.sub_home_returnDates_button.setText(_translate("subscriber_home", "Return dates"))
        self.sub_home_penalties_button.setText(_translate("subscriber_home", "Penalties"))


