# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subscribersingup.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from User import Subscriber
from content import Library
from DataBaseActions import Ui_Dialog
import sqlite3
import sys
#connection = sqlite3.connect('ODP.db')
class Ui_subscriber_signup(object):
    Mylibrary = Library("mido","mido")
    MyDataBase = Ui_Dialog()
    def SignUp(self):

        if (self.sign_name_textbox.text()!="" and self.sign_age_textbox.text()!="" and self.sign_phone_textbox.text()!="" and self.sign_email_textbox.text()!="" and self.sign_password_textbox.text()!="" and self.sign_visa_textbox.text()!="" and self.sign_balance_textbox.text()!=""):
            sbscriber = Subscriber(Ui_subscriber_signup.Mylibrary.id,str(self.sign_name_textbox.text()), int(self.sign_age_textbox.text()),int(self.sign_phone_textbox.text()), self.sign_email_textbox.text(),self.sign_password_textbox.text(), self.sign_visa_textbox.text(),str(self.sign_subType_combobox.currentText()),int( self.sign_balance_textbox.text()))
            Ui_subscriber_signup.MyDataBase.SignUp(sbscriber)
        else:
            print("Incomplete Data!")



    def setupUi(self, subscriber_signup):
        subscriber_signup.setObjectName("subscriber_signup")
        subscriber_signup.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(subscriber_signup)
        self.centralwidget.setObjectName("centralwidget")
        self.sign_name_label = QtWidgets.QLabel(self.centralwidget)
        self.sign_name_label.setGeometry(QtCore.QRect(80, 70, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_name_label.setFont(font)
        self.sign_name_label.setObjectName("sign_name_label")
        self.sign_email_label = QtWidgets.QLabel(self.centralwidget)
        self.sign_email_label.setGeometry(QtCore.QRect(80, 160, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_email_label.setFont(font)
        self.sign_email_label.setObjectName("sign_email_label")
        self.sign_pass_label = QtWidgets.QLabel(self.centralwidget)
        self.sign_pass_label.setGeometry(QtCore.QRect(60, 240, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_pass_label.setFont(font)
        self.sign_pass_label.setObjectName("sign_pass_label")
        self.sign_age_label = QtWidgets.QLabel(self.centralwidget)
        self.sign_age_label.setGeometry(QtCore.QRect(80, 310, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_age_label.setFont(font)
        self.sign_age_label.setObjectName("sign_age_label")
        self.sign_phone_label = QtWidgets.QLabel(self.centralwidget)
        self.sign_phone_label.setGeometry(QtCore.QRect(40, 410, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_phone_label.setFont(font)
        self.sign_phone_label.setObjectName("sign_phone_label")
        self.sign_visa_label = QtWidgets.QLabel(self.centralwidget)
        self.sign_visa_label.setGeometry(QtCore.QRect(490, 190, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_visa_label.setFont(font)
        self.sign_visa_label.setObjectName("sign_visa_label")
        self.sign_balance_label = QtWidgets.QLabel(self.centralwidget)
        self.sign_balance_label.setGeometry(QtCore.QRect(510, 300, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_balance_label.setFont(font)
        self.sign_balance_label.setObjectName("sign_balance_label")
        self.sign_name_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.sign_name_textbox.setGeometry(QtCore.QRect(190, 70, 151, 22))
        self.sign_name_textbox.setObjectName("sign_name_textbox")
        self.sign_email_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.sign_email_textbox.setGeometry(QtCore.QRect(190, 160, 151, 22))
        self.sign_email_textbox.setObjectName("sign_email_textbox")
        self.sign_password_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.sign_password_textbox.setGeometry(QtCore.QRect(190, 240, 151, 22))
        self.sign_password_textbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sign_password_textbox.setObjectName("sign_password_textbox")
        self.sign_age_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.sign_age_textbox.setGeometry(QtCore.QRect(190, 320, 151, 22))
        self.sign_age_textbox.setObjectName("sign_age_textbox")
        self.sign_phone_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.sign_phone_textbox.setGeometry(QtCore.QRect(190, 410, 151, 22))
        self.sign_phone_textbox.setObjectName("sign_phone_textbox")
        self.sign_visa_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.sign_visa_textbox.setGeometry(QtCore.QRect(460, 240, 181, 22))
        self.sign_visa_textbox.setObjectName("sign_visa_textbox")
        self.sign_balance_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.sign_balance_textbox.setGeometry(QtCore.QRect(460, 360, 181, 22))
        self.sign_balance_textbox.setObjectName("sign_balance_textbox")
        self.sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up.setGeometry(QtCore.QRect(500, 470, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_up.setFont(font)
        self.sign_up.setObjectName("sign_up")
        self.sign_subType_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.sign_subType_combobox.setGeometry(QtCore.QRect(490, 120, 111, 22))
        self.sign_subType_combobox.setObjectName("sign_subType_combobox")
        self.sign_subType_combobox.addItem("Overview")
        self.sign_subType_combobox.addItem("Moderator")
        self.sign_subType_combobox.addItem("Regular")
        self.sign_subType_label = QtWidgets.QLabel(self.centralwidget)
        self.sign_subType_label.setGeometry(QtCore.QRect(470, 60, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_subType_label.setFont(font)
        self.sign_subType_label.setObjectName("sign_subType_label")
        subscriber_signup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(subscriber_signup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        subscriber_signup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(subscriber_signup)
        self.statusbar.setObjectName("statusbar")
        subscriber_signup.setStatusBar(self.statusbar)

        self.retranslateUi(subscriber_signup)
        QtCore.QMetaObject.connectSlotsByName(subscriber_signup)
        #self.sign_up.clicked(self.SignUp())
        self.sign_up.clicked.connect(self.SignUp)

    def retranslateUi(self, subscriber_signup):
        _translate = QtCore.QCoreApplication.translate
        subscriber_signup.setWindowTitle(_translate("subscriber_signup", "MainWindow"))
        self.sign_name_label.setText(_translate("subscriber_signup", "Name"))
        self.sign_email_label.setText(_translate("subscriber_signup", "Email"))
        self.sign_pass_label.setText(_translate("subscriber_signup", "Password"))
        self.sign_age_label.setText(_translate("subscriber_signup", "Age"))
        self.sign_phone_label.setText(_translate("subscriber_signup", "Phone Number"))
        self.sign_visa_label.setText(_translate("subscriber_signup", "Visa Card Info"))
        self.sign_balance_label.setText(_translate("subscriber_signup", "Balance"))
        self.sign_up.setText(_translate("subscriber_signup", "Sign Up"))
        self.sign_subType_label.setText(_translate("subscriber_signup", "Subscription Type"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_subscriber_signup()
ui.setupUi(MainWindow)

#ui.SignUp()
MainWindow.show()
sys.exit(app.exec_())