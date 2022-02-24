import os
import hashlib
import json

class Hashing:
    
    __Salt= b'\xd2\xd5-\xc6\x1a\x0f\xb7G\x90-\x95zV\x8c\xe6\x94\x9eYd\xab\xb8H+tk#\x1a7^fV\x86'
    
    def __init__(self,UserName: str ,Password: str, *args, **kwargs) -> None:
        pass
    

    def encoding(self, NewPassword):
        key = hashlib.pbkdf2_hmac('sha256', NewPassword.encode('utf-8'), self.__Salt, 100_000)
        return str(key)
        
    def decoding(self):
        pass

class User(Hashing):
    Player_Detail= {"user":"","level":int,"money":int,"items":"","stocks":""}
    __Users_List= list()
    __The_User= any
    stocks:str= None
    items: str= None
    money: int= None
    
    def __init__(self, UserName: str ,Password: str,*args ,**kwargs) :
        super().__init__(UserName, Password, *args, **kwargs)
        self.UserNameGiven= UserName
        self.PasswordGiven= Password
        self.readUserPass()
    
    def readUserPass(self):
        try:
            MyFile= open('D:\\Coding\\Users\\Users_Pass.txt','r')
        except:
            raise FileExistsError("File has not been found!")    
        for i in MyFile:
            Temp=i.split(',')
            Temp2={Temp[0]:Temp[1].strip()}
            self.__Users_List.append(Temp2)
        MyFile.close()
        
        
    def FindTheUser(self):
        self.readUserPass()
        for i in range(len(self.__Users_List)):
            if self.UserNameGiven in self.__Users_List[i]:
                self.__The_User=self.__Users_List[i]
                Temp=list(self.__The_User.keys())
                Temp+=(list(self.__The_User.values()))
                self.__The_User= Temp
                return True
        else:
            return False    
        
        
        
    def checkpassword(self) -> bool:
        """
        self.__The_User[0]= username
        self.__The_User[1]= key
        """
        if self.__The_User[0]==self.UserNameGiven:
            NewKey= self.encoding(self.PasswordGiven)
            if NewKey==self.__The_User[1]:
                return True
            else:
                return False
            
            
    def readUserDetail(self):
        try:
            MyFile= open('D:\\Coding\\Users\\Users_Detail.txt','r')
        except:
            raise FileExistsError("File has not been found!")      
        for i in MyFile:
            Temp_dict=json.loads(i)
            if Temp_dict.get("user")== self.__The_User[0]:
                self.Player_Detail= Temp_dict
                break
            
        else:
                raise BaseException(" This user does not exist on the << Users_Detail.txt>> file")            
        MyFile.close()

class SignUp(User):
    
    
    def __init__(self, UserName: str, Password: str, *args, **kwargs) -> None:
        self.UserName=UserName
        self.Password=Password
        self.writeInTheFile()
    
    @property
    def UserName(self):
        return self.__UserName
    
    @UserName.setter
    def UserName(self, value):
        self.UserNameGiven=value
        if self.FindTheUser():
            raise ValueError ("This Username already exists!")
        elif len(value)<5:
            raise ValueError ("Length of username must be more than 4 characters")
        self.__UserName= value
    
    @property
    def Password(self):
        return self.__Password
    
    @Password.setter
    def Password(self, value):
        if len(value)<6:
            raise ValueError ("Length of you password must be more than 5 characters")
        self.__Password= value    
    
    def writeInTheFile(self) :
        try:
            with open('D:\\Coding\\Users\\Users_Pass.txt','a')as MyFile:
                self.__Password= self.encoding(self.__Password)
                MyFile.write(f"{self.__UserName},{self.__Password}\n")
        except:
            raise FileExistsError("File has not been found!")  
        try:
            self.Player_Detail["user"]=self.__UserName
            with open('D:\\Coding\\Users\\Users_Detail.txt','a')as MyFile:
                MyFile.write(str(self.Player_Detail))
                MyFile.write('\n')
                
        except:
            raise FileExistsError("File has not been found!")      

