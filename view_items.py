# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_items.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from  User import Login
from PyQt5 import QtCore, QtGui, QtWidgets
from DataBaseActions import Ui_Dialog ,Rent,Favorite,SubscriberAction

class Ui_viewItems(object):
    MyDataBase = Ui_Dialog()
    i = 0
    MyAction = SubscriberAction()
    def subRent(self):
        Ui_viewItems.MyAction = Rent()
        Ui_viewItems.MyAction.Action(self.x,self.res[Ui_viewItems.i][1])
    def subFav(self):
        Ui_viewItems.MyAction = Favorite()
        Ui_viewItems.MyAction.Action(self.x, self.res[Ui_viewItems.i][1])
    def Get_items(self):
        self.x = Login.getInstance(self)
        self.res = Ui_viewItems.MyDataBase.ViewContent()
        self.item_name_value_label.setText(str(self.res[0][1][1]))
        self.item_desc_value_label.setText((str(self.res[0][1][2])))
        self.item_price_value_label.setText(str(self.res[0][1][8]))
    def ViewNext(self):
        itr = Ui_viewItems.i + 1
        Ui_viewItems.i = Ui_viewItems.i + 1

        if (itr>=len(self.res)):
            print("No More items :))")
            return
        self.item_name_value_label.setText(str(self.res[itr][1][1]))
        self.item_desc_value_label.setText((str(self.res[itr][1][2])))
        self.item_price_value_label.setText(str(self.res[itr][1][8]))
    def setupUi(self, viewItems):
        viewItems.setObjectName("viewItems")
        viewItems.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(viewItems)
        self.centralwidget.setObjectName("centralwidget")
        self.book_name_label = QtWidgets.QLabel(self.centralwidget)
        self.book_name_label.setGeometry(QtCore.QRect(180, 50, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_name_label.setFont(font)
        self.book_name_label.setObjectName("book_name_label")
        self.item_name_value_label = QtWidgets.QLabel(self.centralwidget)
        self.item_name_value_label.setGeometry(QtCore.QRect(510, 50, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.item_name_value_label.setFont(font)
        self.item_name_value_label.setObjectName("item_name_value_label")
        self.item_desc_label = QtWidgets.QLabel(self.centralwidget)
        self.item_desc_label.setGeometry(QtCore.QRect(180, 140, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.item_desc_label.setFont(font)
        self.item_desc_label.setObjectName("item_desc_label")
        self.item_desc_value_label = QtWidgets.QLabel(self.centralwidget)
        self.item_desc_value_label.setGeometry(QtCore.QRect(510, 140, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.item_desc_value_label.setFont(font)
        self.item_desc_value_label.setObjectName("item_desc_value_label")
        self.next_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_item_button.setGeometry(QtCore.QRect(580, 440, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.next_item_button.setFont(font)
        self.next_item_button.setObjectName("next_item_button")
        self.rent_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.rent_item_button.setGeometry(QtCore.QRect(470, 340, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rent_item_button.setFont(font)
        self.rent_item_button.setObjectName("rent_item_button")
        self.favorite_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.favorite_item_button.setGeometry(QtCore.QRect(140, 340, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.favorite_item_button.setFont(font)
        self.favorite_item_button.setObjectName("favorite_item_button")
        self.item_price_label = QtWidgets.QLabel(self.centralwidget)
        self.item_price_label.setGeometry(QtCore.QRect(190, 220, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.item_price_label.setFont(font)
        self.item_price_label.setObjectName("item_price_label")
        self.item_price_value_label = QtWidgets.QLabel(self.centralwidget)
        self.item_price_value_label.setGeometry(QtCore.QRect(500, 220, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.item_price_value_label.setFont(font)
        self.item_price_value_label.setObjectName("item_price_value_label")
        viewItems.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(viewItems)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        viewItems.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(viewItems)
        self.statusbar.setObjectName("statusbar")
        viewItems.setStatusBar(self.statusbar)

        self.retranslateUi(viewItems)
        QtCore.QMetaObject.connectSlotsByName(viewItems)
        self.Get_items()
        self.next_item_button.clicked.connect(self.ViewNext)
        self.rent_item_button.clicked.connect(self.subRent)
        self.favorite_item_button.clicked.connect(self.subFav)

    def retranslateUi(self, viewItems):
        _translate = QtCore.QCoreApplication.translate
        viewItems.setWindowTitle(_translate("viewItems", "MainWindow"))
        self.book_name_label.setText(_translate("viewItems", "Item name"))
        self.item_name_value_label.setText(_translate("viewItems", "value"))
        self.item_desc_label.setText(_translate("viewItems", "Description"))
        self.item_desc_value_label.setText(_translate("viewItems", "value"))
        self.next_item_button.setText(_translate("viewItems", "Next Item"))
        self.rent_item_button.setText(_translate("viewItems", "Rent"))
        self.favorite_item_button.setText(_translate("viewItems", "Favorite"))
        self.item_price_label.setText(_translate("viewItems", "Price"))
        self.item_price_value_label.setText(_translate("viewItems", "value"))


