import DND_User_Class as user
import os
from time import sleep
from termcolor import colored
import msvcrt
import logging

class Login:
    logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler('Users.log')
    f_handler.setLevel(logging.INFO)
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logger.setLevel(logging.INFO)



    def __init__(self,*args , **kwargs) -> None:
        self.Welcome()
    
    def SignUpUser(self):
        os.system("cls")
        self._User_Name= input("Please enter your username: ")
        os.system("cls")
        self._Password= input("Please enter your Password: ")
        
        This_user = user.SignUp(self._User_Name, self._Password)
        self.logger.info(f'{self._User_Name} signed up')
        os.system("cls")
        print(colored("Welcome to D&D !!!", 'red' , 'on_yellow'))
        self.Welcome()

    
    
    def loginUser(self) -> dict:
        os.system("cls")
        self._User_Name= input("Please enter your username: ")
        os.system("cls")
        self._Password= input("Please enter your Password: ")
        
        This_User=user.User(self._User_Name ,self._Password )
        
        if This_User.FindTheUser():
            if This_User.checkpassword():
                self.logger.info(f'{self._User_Name} logged in')
                return This_User.readUserDetail
                    
            else:
                print("Username or Password is not Correct!")
                exit(0)
        else:
            print("Username or Password is not Correct!")
            exit(0)
            
            
    def Welcome(self):
        os.system("cls")
        print(colored("Welcome To DND ! \n","grey",'on_yellow'))
        sleep(0.75)
        print("1.Login \n2.Signup\n")
        
        while True:
            User_Choice= msvcrt.getch()
            if User_Choice==b'1' or User_Choice==b'2':
                break

        if User_Choice==b'1':
            self.loginUser()

        if User_Choice==b'2':    
            self.SignUpUser()


