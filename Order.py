
import sys
import os
from datetime import  date
from abc import  ABCMeta, abstractmethod
# EmailClient.SendEmail(State , Email)
import sqlite3
from DataBaseActions import Ui_Dialog
class Order:
    def __init__(self, identification, listener, state, price):
        self.__identification = identification
        self.__cart = list()
        self.__listener = listener
        self.__state = state
        self.__price = price
        self.__RentalDate = date.today()

    def add_to_cart(self, component):
        self.__cart.append(component)

    def remove_from_cart(self, component):
        self.__cart.remove(component)

    def notify_listener(self):
        self.__listener.update()

    # start Getters and setters for properties
    def set_id(self, identification):
        self.__identification = identification

    def get_id(self):
        return self.__identification

    def set_RentalDate(self, RentalDate):
        self.__RentalDate = RentalDate

    def get_RentalDate(self):
        return self.__RentalDate

    def set_cart(self, cart):
        self.__cart = cart

    def get_cart(self):
        return self.__cart

    def set_listener(self, listener):
        self.__listener = listener

    def get_listener(self):
        return self.__listener

    def set_state(self, state):
        self.__state.SetState(state)
        self.notify_listener()

    def get_state(self):
        return self.__state

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


# End Getters and setters for properties
class Listener:
    def update(self):
        pass


class EmailClient (Listener):

    def update(self):
        print("Email sent to user ")



class OrderState:

    def __init__(self):
        self.__state = None

    def SetState(self,state,x,res):
        self.__state = state
        self.action(x,res)

    def action(self,x,res):
        self.__state.handel(x,res)


class StateHandlerBase(metaclass=ABCMeta):
    MyDataBase = Ui_Dialog()
    @abstractmethod
    def handel(self,x,res):
        pass



class Rented(StateHandlerBase):
    def handel(self,x,res):
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
        newBalnce = x.balance - res[8]
        self.c.execute("UPDATE Subscriber SET Balance = ? WHERE sub_Id = ?", (newBalnce, x.id))
        self.conn.commit()
        self.c.close()
        self.conn.close()
        self.conn2 = sqlite3.connect("test.db")

        self.c2 = self.conn2.cursor()

        self.c2.execute("UPDATE Content SET Avilable = 'False',state='Rented' WHERE content_Id = " + str((res[0])))
        self.conn2.commit()
        self.c2.close()
        self.conn2.close()
        print("doneee")


class Returned(StateHandlerBase):
    def handel(self):
        print("Order is renturned")


class Compsing(StateHandlerBase):
    def handel(self):
        print("Order is Compsing")


class Late(StateHandlerBase):
    def handel(x,res):
        for r in res:
            StateHandlerBase.MyDataBase.AddPanalty(r)
            StateHandlerBase.MyDataBase.UpdateBalance(r)


class Composed(StateHandlerBase):
    def handel(self):
        print("Order is late")
