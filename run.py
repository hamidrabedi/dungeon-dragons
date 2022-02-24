import os
from termcolor import colored
import random
import msvcrt
import math 

class Map:
    _Dimensions:int 
    _Locations= list()
    Player_position= tuple()
    Dragon_Position = tuple()
    DoorOfHeaven= tuple()
    ExtraLife= bool
    DoorOfHeaven= tuple
    
    def __init__(self, Dimensions , *args ,**kwargs) -> None:
        self.Dimensions = Dimensions
        
        self.Player_position= (self.get_random(self._Dimensions),self.get_random(self._Dimensions))
        self.Dragon_Position= (self.get_random(self._Dimensions),self.get_random(self._Dimensions))
        self.DoorOfHeaven= (self.get_random(self.Dimensions), self.get_random(self.Dimensions))
        
        self.createBoard()
        
    @property
    def Dimensions(self):
        return self._Dimensions
    
    @Dimensions.setter
    def Dimensions(self, value):
        try:
            value= int(value)
        except:
            raise ValueError("<Dimenstion> must be an integer !")
        if 1<value<41:
            self._Dimensions= value
        else:
            raise ValueError("<Dimension> must be between 1 and 40")    
    
    def get_random(self, value):
        return random.randint(0,value-1)
        
    def createBoard(self):
        os.system('cls')
        print(" _",end="")
        print(" _"*(self._Dimensions-1))
        Counter_while=0  
        while Counter_while!=self._Dimensions:
            for i in range(self._Dimensions+1):
                if i !=self._Dimensions:
                    if self.Player_position== (i,Counter_while):    
                        print("|",end="")
                        print(colored("X", "cyan"),end= "")
                    else: 
                        print("|_",end="")             
                else:
                    print("|",end= "\n")
            Counter_while+=1

class Location(Map):
    
    def __init__(self, Dimensions, *args, **kwargs) -> None:
        super().__init__(Dimensions, *args, **kwargs)

        self.Locations()
        self.main()
        
    def playerMovment(self,Choice:str) :
        Poslist = list(self.Player_position)
        if Choice == b's':
            Poslist[1] += 1
        elif Choice == b'a':
            Poslist[0] -= 1
        elif Choice == b'd':
            Poslist[0] += 1
        elif Choice == b'w':
            Poslist[1] -= 1
        print("\n")
        if Poslist[0] > self._Dimensions-1:
            print("You just hit the wall Brotha!!!")
            Poslist[0] -= 1
            print("Press any key to continue")
            msvcrt.getch()
        if Poslist[1] > self._Dimensions-1:
            print("You just hit the wall Brotha!!!")
            Poslist[1] -= 1
            print("Press any key to continue")
            msvcrt.getch()
        if Poslist[0] < 0:
            print("You just hit the wall Brotha!!!")
            Poslist[0] += 1
            print("Press any key to continue")
            msvcrt.getch()
        if Poslist[1] < 0:
            print("You just hit the wall Brotha!!!")
            Poslist[1] += 1
            print("Press any key to continue")
            msvcrt.getch()

        self.Player_position= tuple(Poslist)
    
    def dragonMovment(self):
        """
        This function will check if the distance of dragon and player
        is between 0-4 and there will be a chance that dragon makes a 
        move towards the player.
        
        unless there will be 10% chance for the dragon to get closer 
        to the player.
        """
        Poslist = list(self.Dragon_Position)
        X1, Y1 = self.Player_position
        X2, Y2 = self.Dragon_Position
        Temp1 = abs(Y2 - Y1)
        Temp2 = abs(X2 - X1)
        Float_Distance = math.sqrt((Temp1**2)+(Temp2**2))

        temp_dragon_position = Poslist.copy()
        Player_Dragon_Distance = [self.Dragon_Position[0]-self.Player_position[0], self.Dragon_Position[1]-self.Player_position[1]]
        ChanceToGetCloseToPlayer = random.randint(1, 100)

        if 3 < Float_Distance < 4 or Float_Distance == 3:
                if ChanceToGetCloseToPlayer < 41:
                    if abs(Player_Dragon_Distance[0]) >= abs(Player_Dragon_Distance[1]):
                        if Player_Dragon_Distance[0] > 0:
                            Poslist[0] -= 1
                        else:
                            Poslist[0] += 1
                    elif Player_Dragon_Distance[1] > 0:
                            Poslist[1] -= 1
                    else:
                        Poslist[1] += 1
        elif 2 < Float_Distance < 3 or Float_Distance == 2:
                if ChanceToGetCloseToPlayer < 61:
                    if abs(Player_Dragon_Distance[0]) >= abs(Player_Dragon_Distance[1]):
                        if Player_Dragon_Distance[0] > 0:
                            Poslist[0] -= 1
                        else:
                            Poslist[0] += 1
                    elif Player_Dragon_Distance[1] > 0:
                            Poslist[1] -= 1
                    else:
                        Poslist[1] += 1
        elif 0<Float_Distance<2 or Float_Distance==1: 
                if ChanceToGetCloseToPlayer<81:
                    if abs(Player_Dragon_Distance[0])>= abs(Player_Dragon_Distance[1]):
                        if Player_Dragon_Distance[0]>0:
                            Poslist[0]-=1
                        else:
                            Poslist[0]+=1
                    elif Player_Dragon_Distance[1]>0:
                            Poslist[1]-=1
                    else:
                        Poslist[1]+=1

        """
        if distance between dragon and player is not less that 4blocks :
        1. 10 % chance to get closer to player.
        2. Just a random move.
        """
        
        if temp_dragon_position==Poslist:
            if ChanceToGetCloseToPlayer>10:
                while True:          
                        x=random.randint(1,4)
                        if x==1:
                            if Poslist[1]!=0:
                                Poslist[1]-=1
                                break
                        elif x==2:
                            if Poslist[0]!=self._Dimensions-1:
                                Poslist[0]+=1
                                break
                        elif x==3:
                            if Poslist[1]!= self._Dimensions-1:
                                Poslist[1]+=1
                                break
                        elif x==4:
                            if Poslist[0]!=0:
                                Poslist[0]-=1
                                break    
                        print(Poslist)

            else:
                if abs(Player_Dragon_Distance[0])>= abs(Player_Dragon_Distance[1]):
                    if Player_Dragon_Distance[0]>0:
                            Poslist[0]-=1
                    else:
                            Poslist[0]+=1
                elif Player_Dragon_Distance[1]>0:
                            Poslist[1]-=1
                else:
                        Poslist[1]+=1

    def iswinner(self):
        if self.DoorOfHeaven==self.Player_position:
            os.system('cls')
            print("GG WP!\n Congrats You found the door! ! ")
            print("\n1.Play Again \n2.Quit the game\n")
            Choose=msvcrt.getch()

    def lostGame(self):
        if self.Player_position==self.Dragon_Position:
            os.system("cls")
            print("Dragon ate you and you lost!")
        
    def Locations(self):
        for i in range (self._Dimensions):
            for j in range(self._Dimensions):
                self._Locations.append((i,j))

    
    def main(self):
        while True:
            print(colored("Whats your move? (Use WASDA) :  ",'green'))
            Player_Choice= msvcrt.getch()
            self.playerMovment(Player_Choice)
            self.dragonMovment()
            self.createBoard()
            self.iswinner()
            self.lostGame()
        
test= Location(10)
