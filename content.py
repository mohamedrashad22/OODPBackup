from enum import Enum
from datetime import  date

class  Level (Enum):
    Child = "Child_Level"
    Intermidate = "Intermidate_Level"
    Adult = "Adult_Level"


class IDisplay:

    def Display(self):
        pass


class Library(IDisplay):
    id = 1
    def __init__(self,name,address):
        self.__children = list()
        self.__Name=name
        self.__Address = address
        #self.__Users = list()
        self.id = Library.id
        Library.id = Library.id + 1

    def GetName(self):
        return self.__Name

    def GetContent(self):
        return self.__children
    def SetName(self,Name):
        self.__Name = Name


    def GetAddress(self):
        return self.__Address


    def SetAddress(self, Address):
        self.__Address = Address


    def Display(self):
        for child in self.__children:
            child.Display()

    def add(self, content):
        self.__children.append(content)

    def remove(self, content):
        self.__children.remove(content)





class Content(IDisplay):
    id = 6
    def __init__(self,Title,des,noCop,level,date,state,price,CatID,LibID):
        self.id = Content.id
        Content.id = Content.id + 1
        self.Title = Title
        self.Description = des
        self.No_OF_Copies = noCop
        self.Lvel = level
        self.PublishDate = date
        self.State = state
        self.price = price
        self.Avilable = True
        #self.__Author = author("Unknown","Unknown","Unknown","Unknown","Unknown","Unknown")
        self.CategoryID = CatID
        self.LibraryID = LibID

    def Display(self):
        pass

    def GetTitle(self):
        return self.__Title

    def SetTitle(self, Title):
        self.__Title = Title

    def GetCategory(self):
        return self.____Category

    def SetCategory(self, Category):
        self.__Category = Category

    def GetDescription(self):
        return self.__Description

    def SetDescription(self, Description):
        self.__Description = Description

    def GetDescription(self):
        return self.__Description

    def SetDescription(self, Description):
        self.__Description = Description


import random
import sys
import os
from abc import ABCMeta, abstractmethod


class category():
    id = 1
    def __init__(self, title, description):
        self.id = category.id
        category.id = category.id + 1
        self.title = title
        self.description = description

    def GetID(self):
        return self.__ID

    def SetID(self, ID):
        self.__ID = ID


    def GetTitle(self):
        return self.__title

    def SetTitle(self, title):
        self.__title = title

    def GetDescription(self):
        return self.__description

    def SetDescription(self, description):
        self.__description = description


class author():
    id = 2
    def __init__(self, bio, name):
        self.ID = author.id
        author.id = author.id + 1
        self.name = name
        self.bio = bio

    def GetID(self):
        return self.__ID

    def SetID(self, ID):
        self.__ID = ID



    def GetName(self):
        return self.__name

    def SetName(self, name):
        self.__name = name

    def GetBio(self):
        return self.__bio

    def SetBio(self, bio):
        self.__bio = bio


class book(Content):
    def __init__(self, numberOfPaper,Title,des,noCop,level,date,state,price,CatID,LibID):
        super(book,self).__init__(Title,des,noCop,level,date,state,price,CatID,LibID)
        self.numberOfPaper = numberOfPaper


    def Display(self):
        print("Book..")
        #print(super(book,self).GetTitle())

    def GetNumberOfPaper(self):
        return self.__numberOfPaper

    def SetNumberOfPaper(self, NumberOfPaper):
        self.__numberOfPaper = NumberOfPaper


class article(Content):
    def __init__(self, numberOfLines):
        super(article, self).__init__()
        self.__numberOfLines = numberOfLines

    def Display(self):
        print("Article..")

    def GetNumberOfLines(self):
        return self.__numberOfLines

    def SetNumberOfLines(self, NumberOfLines):
        self.__numberOfLines = NumberOfLines


class journal(Content):
    def __init__(self, numberOfLines):
        super(journal, self).__init__()
        self.__numberOfLines = numberOfLines

    def Display(self):
        print("Journal..")

    def GetNumberOfLines(self):
        return self.__numberOfLines

    def SetNumberOfLines(self, NumberOfLines):
        self.__numberOfLines = NumberOfLines


class digitalMedia(Content, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, Size):
        super(digitalMedia, self).__init__()
        self.__size = Size
    def Display(self):
        print("DigitalMedia..")

    def GetSize(self):
        return self.__size

    def SetSize(self, Size):
        self.__size = Size


class eBook(digitalMedia):
    def __init__(self, size):
        super(eBook, self).__init__(size)

    def Display(self):
        print("eBook", end=" ")
        super(eBook,self).Display()
class audioBook(digitalMedia):
    def __init__(self, size):
        super(audioBook, self).__init__(size)

    def Display(self):
        print("AudioBook", end=" ")
        super(audioBook,self).Display()
