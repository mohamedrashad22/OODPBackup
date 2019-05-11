from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
from content import Content ,book,category,Library,author
from User import Subscriber

from abc import  ABCMeta, abstractmethod


class Nofification():

    Observers = list()
    def AddObserver(self,Observer):
        Nofification.Observers.append(Observer)
        print(Nofification.Observers[0])

    def RemoveObserver(self,Observer):
        Nofification.Observers.append(Observer)
        print(Nofification.Observers[0])

    def NotifiyObservers(self):
        for Observer in Nofification.Observers:
            Observer.Update(Observer[5],Observer[4])






class RentTypeFactory():
    def GetRentType(self,type):
        if(type=="Gold"):
            return GoldRentDate()
        else:
            return SilverRentDate()

class RentDate():
    Rentdate = datetime.date.today()
    def CalRentDate(self):
        pass


class SilverRentDate(RentDate):
    def CalRentDate(self):
       RentDate.Rentdate = RentDate.Rentdate + datetime.timedelta(21)


class GoldRentDate(RentDate):
    def CalRentDate(self):
        RentDate.Rentdate = RentDate.Rentdate + datetime.timedelta(90)
        return RentDate.Rentdate


class SubscriberAction():
    def Action(self):
        pass

class  Favorite(SubscriberAction):
    def Action(self,x,res):
        try:
            self.conn = sqlite3.connect("test.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO FavoriteContent (Subscriber_Id,content_Id)VALUES (?,?)",(x.id,res[0]))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print("added from favorit")
        except Exception:
            print("error")
class Rent(SubscriberAction):
    def Action(self,x,res):
        try :
            if(x.balance<res[8]):
                print("Error Balnce Not Enough")
                return

            RentType = RentTypeFactory()
            Date = RentType.GetRentType(x.subscription_type)
            self.conn1 = sqlite3.connect("test.db")
            self.c1 = self.conn1.cursor()
            self.c1.execute("INSERT INTO Rent (sub_Id,content_Id,Price,Rent_Date,Late) VALUES(?,?,?,?,?)",(x.id,res[0],res[8],Date.CalRentDate(),'False'))
            self.conn1.commit()
            self.c1.close()
            self.conn1.close()
            print("added from rent")
            CurState = OrderState()
            rent = Rented()
            CurState.SetState(rent,x,res)

        except Exception:
            print("Error")


class Ui_Dialog(object):

    def GetUsers(self,cat):
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
        Result = self.c.execute("SELECT * FROM FavoriteContent INNER JOIN Subscriber ON Subscriber.sub_Id = FavoriteContent.Subscriber_Id WHERE FavoriteContent.Content_Id = (SELECT Content.content_Id FROM Content WHERE Content.CategoryId = ( SELECT Category.category_Id FROM Category WHERE Category.Title ="+"'"+str(cat)+"'"+"))" )
        res = Result.fetchall()
        print(res)
        self.conn.commit()
        self.c.close()
        self.conn.close()
        return res

    def AddPanalty(self,res):
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
        newBalnce = res[3] + 50
        self.c.execute("UPDATE Rent SET Late = 'True' ,Price = ? WHERE sub_Id = ? AND Rent.content_Id = ?", (newBalnce, res[0],res[4]))
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def UpdateBalance(self,res):
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
        newBalnce = res[2] - 50
        self.c.execute("UPDATE Subscriber SET Balance = ? WHERE sub_Id = ?", (newBalnce, res[0]))
        self.conn.commit()
        self.c.close()
        self.conn.close()
    def GetLateItem(self):
        try:
            self.conn = sqlite3.connect("test.db")
            self.c = self.conn.cursor()
            Result = self.c.execute("SELECT Rent.sub_Id,  Subscriber.Email ,Subscriber.Balance ,Rent.Price , Rent.content_Id FROM Rent INNER JOIN Subscriber ON Subscriber.sub_Id = Rent.sub_Id WHERE Rent.Rent_Date <= "+"'"+str(datetime.date.today())+"'")
            res = Result.fetchall()
            print(res)
            self.conn.commit()
            self.c.close()
            self.conn.close()
            return res
        except Exception :
            print("moo")

    def SignUp(self,subscriber):
        #try:

            self.conn = sqlite3.connect("test.db")
            self.c = self.conn.cursor()

            self.c.execute("INSERT INTO Subscriber (sub_Id,Phone,Email,Name,Password,Age,CreditCardInfo,SubscriptionType,Balance,LibrayId) "
                           "VALUES (?,?,?,?,?,?,?,?,?,?)",
                           (3,subscriber.phone,subscriber.email,
                            subscriber.name,subscriber.password,subscriber.age,
                            subscriber.credit_card_info,subscriber.subscription_type,
                            subscriber.balance,subscriber.libraryID))
            #self.c.execute("INSERT INTO Subscriber (sub_Id,Phone,Email,Name,Password,Age,CreditCardInfo,SubscriptionType,Balance,LibrayId) VALUES (2,121,'mido','mohamed',2245,21,'5445','gold',122,1)")
            #print(result.fetchall())

            print("Successfully")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print("Inserted Successfully")
        #except Exception:
            print("Error check your data")


    def SignIn(self,email,password):

        #try:
            self.conn = sqlite3.connect("test.db")
            self.c = self.conn.cursor()
            Result = self.c.execute("SELECT * FROM Subscriber where Email = "+"'"+str(email)+"'" )
            row = Result.fetchone()
            self.conn.commit()
            self.c.close()
            self.conn.close()
            if (password==int(row[4])):
                return True ,row
            else:
                return False
        #except Exception:
            print("Error check your data")
    def ViewRent(self,id):
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
        Result = self.c.execute("SELECT Rent_Date , Content.Title FROM Rent INNER JOIN Content ON Content.content_Id = Rent.content_Id WHERE Rent.sub_Id ="+str(id))
        res = Result.fetchall()
        print(res)
        self.conn.commit()
        self.c.close()
        self.conn.close()
        return res

    def ViewRentedItems(self):
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
        Result = self.c.execute("SELECT Subscriber.Name, Content.Title ,Content.Description ,Content.Price , Rent_Date FROM Rent INNER JOIN Content ON Content.content_Id = Rent.content_Id INNER JOIN Subscriber ON Subscriber.sub_Id = Rent.sub_Id WHERE Rent.Late = 'False'")
        res = Result.fetchall()
        print(res)
        self.conn.commit()
        self.c.close()
        self.conn.close()
        return res
    def ViewLateRent(self):
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
        Result = self.c.execute("SELECT Subscriber.Name, Content.Title ,Content.Description ,Content.Price , Rent_Date FROM Rent INNER JOIN Content ON Content.content_Id = Rent.content_Id INNER JOIN Subscriber ON Subscriber.sub_Id = Rent.sub_Id WHERE Rent.Late = 'True'")
        res = Result.fetchall()
        print(res)
        self.conn.commit()
        self.c.close()
        self.conn.close()
        return res
    def ViewPanlties(self,id):
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
        Result = self.c.execute("SELECT Rent.Price , Content.Title FROM Rent INNER JOIN Content ON Content.content_Id = Rent.content_Id WHERE Rent.sub_Id ="+str(id))
        res = Result.fetchall()
        print(res)
        self.conn.commit()
        self.c.close()
        self.conn.close()
        return res
    def ViewFav(self,id):
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
        Result = self.c.execute("SELECT Content.content_Id ,Content.Title FROM FavoriteContent INNER JOIN Content ON Content.content_Id = FavoriteContent.Content_Id WHERE FavoriteContent.Subscriber_Id = "+str(id))
        res=Result.fetchall()
        print(res)
        self.conn.commit()
        self.c.close()
        self.conn.close()
        return res
    def AddConten(self,content):
            self.conn = sqlite3.connect("test.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO Content (content_Id,Title,Description,NumberOfCopies,Level,PublishDate,NumberOfPages,ContentType,Price,Avilable,state,LibrayId,CategoryId)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,? )",
            content.id,content.Title,content.Description,content.No_OF_Copies,content.Lvel,content.PublishDate,content.numberOfPaper,'Book',content.price,content.Avilable,content.LibraryID,content.CategoryID)
            #self.c.execute("INSERT INTO Content (content_Id,Title,Description,NumberOfCopies,Level,PublishDate,NumberOfPages,ContentType,Price,Avilable,state,LibrayId,CategoryId)VALUES(1,'TorabElMass','ActionBook',2,'Adult',5-10-2019,400,'Book',200,'True','init',1,1 )")
            self.conn.commit()
            self.c.close()
            self.conn.close()

            print("Added")
    def ViewContent(self):
        content = list()
        try:
            self.conn = sqlite3.connect("test.db")
            self.c = self.conn.cursor()
            Result = self.c.execute(" SELECT * FROM Content WHERE Content.Avilable = 'True'ORDER BY content_Id")
            for row in enumerate(Result):
                content.append(row)
            print(content)
            self.conn.commit()
            self.c.close()
            self.conn.close()
            return content
        except Exception:
            print("Error")
    def AddAuthor(self,author):
        try:
            self.conn = sqlite3.connect("test.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO Author (Author_ID ,Name,Bio)VALUES (?,?,?)",(author.ID,author.name,author.bio))
            self.conn.commit()
            self.c.close()
            self.conn.close()

        except Exception:
            print("Error")

    def ViewAuthors(self):
        Authors = list()
        try:
            self.conn = sqlite3.connect("test.db")
            self.c = self.conn.cursor()
            Result = self.c.execute("SELECT * FROM Author   ")
            for row in enumerate(Result):
                Authors.append(row)
            self.conn.commit()
            self.c.close()
            self.conn.close()
            return Authors
        except Exception:
            print("Error")

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
class Late(StateHandlerBase):
    def handel(self,x,res):
        for r in res:
            StateHandlerBase.MyDataBase.AddPanalty(r)
            StateHandlerBase.MyDataBase.UpdateBalance(r)



CurState = OrderState()
rent = Late()
a = Ui_Dialog()
dv = a.GetUsers("Action")
Nofification()
for r in dv:
    temp = Subscriber()


