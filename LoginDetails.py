import hashlib, string, secrets
from getpass import getpass
class LoginDetails:
    __uuid:str
    __username:str
    __password:str
    __salt:str
    __data:str
    
    def __init__(self, uuid='', username='', password='', salt='', data=''):
        self.__uuid = uuid
        self.__username = username
        self.__password = password
        self.__salt = salt
        self.__data = data
        
    def getuuid(self):
        return self.__uuid
    def setuuid(self):
        alphabet = string.ascii_letters + string.digits
        tmp=''
        n=10
        for i in range(n):
            tmp += "".join(secrets.choice(alphabet) for i in range(6))
            if i<(n-1):
                tmp += "-"
        self.__uuid = tmp
        
    def getusername(self):
        return self.__username
    def setusername(self,username):
        self.__username=username
        
    def getpassword(self):
        return self.__password
    def setpassword(self,password):
        self.__password=password
    
    def getdata(self):
        return self.__data
    def setdata(self,data):
        self.__data=data
        
    def getsalt(self):
        return self.__salt
    def setsalt(self):
        alphabet = string.ascii_letters + string.digits
        self.__salt= "".join(secrets.choice(alphabet) for i in range(128))
        
    def SetInfo(self):
        self.setusername(input("Enter username: "))
        self.setuuid()
        self.setsalt()
        tmp = (getpass("Enter a password: ") + self.getsalt()).encode()
        self.setpassword(hashlib.sha3_512(tmp).hexdigest())
        self.setdata(input("Enter secret data: "))
    
    # def SetInfo(self):
    #     alphabet = string.ascii_letters + string.digits
    #     tmp123 = "".join(secrets.choice(alphabet) for j in range(8))
    #     self.setuuid()
    #     self.setsalt()
    #     self.setusername(tmp123)
    #     tmp = (tmp123 + self.getsalt()).encode()
    #     self.setpassword(hashlib.sha3_512(tmp).hexdigest())
    #     self.setdata(tmp123)