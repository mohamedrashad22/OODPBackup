from abc import  ABCMeta, abstractmethod
import smtplib
from email.mime.text import MIMEText

class AbstractEmnailSender(metaclass=ABCMeta):
    def __init__(self):
        self.msg =""
    def Send(self,Email):
        print(self.msg)
        #self.msg = MIMEText("""A new Book called is added to The Libaray Now""")
        # Gmail Sign In
        gmail_sender = 'odpproject2050@gmail.com'
        gmail_passwd = 'google2019'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)
        # Add the lsit to receptance
        listt = []
        listt.append(Email)
        recipients = listt
        self.msg['Subject'] = "subject line"
        self.msg['From'] = gmail_sender
        self.msg['To'] = ", ".join(recipients)
        try:
            server.sendmail(gmail_sender, recipients, self.msg.as_string())
            print('email sent')
        except:
            print('error sending mail')
        server.quit()
    @abstractmethod
    def SendNewItemAdded(self,Name,Email,cat,itemName):
        pass
    @abstractmethod
    def ConfirmRent(self,Name,Email,NewBalance):
        pass


class MessageA(AbstractEmnailSender):

    def SendNewItemAdded(self,Name,Email,cat,itemName):
        self.msg =MIMEText("Dear "+Name+","+" we have noticed your interest in "+cat+" So we have Some More For you "+itemName+ " we hope u like them Best Regards Maktabt El Hayah Team")
        self.Send(Email)
    def ConfirmRent(self,Name,Email,NewBalance):
        pass

class MessageB(AbstractEmnailSender):
    def SendNewItemAdded(self,Name,Email,cat,itemName):
        pass
    def ConfirmRent(self,Name,Email,NewBalance):
        self.msg =MIMEText("Dear "+Name+","+" we would like to let you know that YOUR ITEMS HAS Been Succssesfully RENTED and your new balance is "+str(NewBalance)+". Best Regards Maktabt El Hayah Team")
        self.Send(Email)



