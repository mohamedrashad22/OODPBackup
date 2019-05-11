class User:
    id = 0
    def Update(self,Name,Email):
        pass
    def __init__(self, name, age, phone, email, password):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.password = password
        self.id = User.id + 1
        User.id = User.id + 1


class Subscriber(User):
    def __init__(self,libraryID ,name, age, phone, email, password, credit_card_info, subscription_type, balance):
        super(Subscriber,self).__init__( name, age, phone, email, password)
        self.libraryID = libraryID
        self.credit_card_info = credit_card_info
        self.subscription_type = subscription_type
        self.balance = balance



class Admin(User):
    def __init__(self, name, age, phone, email, password):
        User.__init__(self, name, age, phone, email, password)

    def print_report(self):
        pass


class Login:
    __instance = None

    def getInstance(self):
        if Login.__instance == None:
            Login()
        return Login.__instance

    def __init__(self, User):
        if Login.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Login.__instance = User
