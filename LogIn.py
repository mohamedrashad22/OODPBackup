# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subscriberLogIn.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from content import Library
from DataBaseActions import Ui_Dialog
from User import Login,Subscriber
from subscriber_home import Ui_subscriber_home
class Ui_subscriber_login(object):
    Mylibrary = Library("alex","alex")
    MyDataBase = Ui_Dialog()

    def GoToHomePage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_subscriber_home()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def SignIn(self):
        check , user =Ui_subscriber_login.MyDataBase.SignIn(self.log_email_textbox.text(),int(self.log_password_textbox.text()))
        sub = Subscriber(Ui_subscriber_login.Mylibrary.id,user[3],user[5],user[1],user[2],user[4],user[6],user[7],user[8])
        l = Login(sub)

        if (check is True):
            print("Welcome Back ..")
            self.GoToHomePage()

        else:
            print("Incorrect Data!")


    def setupUi(self, subscriber_login):

        subscriber_login.setObjectName("subscriber_login")
        subscriber_login.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(subscriber_login)
        self.centralwidget.setObjectName("centralwidget")
        self.log_email = QtWidgets.QLabel(self.centralwidget)
        self.log_email.setGeometry(QtCore.QRect(170, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log_email.setFont(font)
        self.log_email.setObjectName("log_email")
        self.log_password = QtWidgets.QLabel(self.centralwidget)
        self.log_password.setGeometry(QtCore.QRect(170, 230, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log_password.setFont(font)
        self.log_password.setObjectName("log_password")
        self.log_email_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.log_email_textbox.setGeometry(QtCore.QRect(370, 161, 231, 31))
        self.log_email_textbox.setObjectName("log_email_textbox")
        self.log_password_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.log_password_textbox.setGeometry(QtCore.QRect(370, 230, 231, 31))
        self.log_password_textbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_password_textbox.setObjectName("log_password_textbox")
        self.log_in = QtWidgets.QPushButton(self.centralwidget)
        self.log_in.setGeometry(QtCore.QRect(290, 340, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log_in.setFont(font)
        self.log_in.setObjectName("log_in")
        subscriber_login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(subscriber_login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        subscriber_login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(subscriber_login)
        self.statusbar.setObjectName("statusbar")
        subscriber_login.setStatusBar(self.statusbar)

        self.retranslateUi(subscriber_login)
        QtCore.QMetaObject.connectSlotsByName(subscriber_login)
        self.log_in.clicked.connect(self.SignIn)

    def retranslateUi(self, subscriber_login):
        _translate = QtCore.QCoreApplication.translate
        subscriber_login.setWindowTitle(_translate("subscriber_login", "MainWindow"))
        self.log_email.setText(_translate("subscriber_login", "Email"))
        self.log_password.setText(_translate("subscriber_login", "Password"))
        self.log_in.setText(_translate("subscriber_login", "Log In"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
uii = Ui_subscriber_login()
uii.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

print("yessss")