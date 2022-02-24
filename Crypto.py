import os
import requests
from bs4 import BeautifulSoup
import asyncio
import time 
import msvcrt
import sys

class Crypto:
    Coins=['bitcoin','ethereum' ,'litecoin' ,'dogecoin','cardano','xrp', 'solana' ]
    url :str
    Cryptos= dict()

    def __init__(self, *args , **kwargs) :
        pass
        
    async def request(self):    
        self.HTML= requests.get(self.url)

        
    async def Dump(self):
        for i in self.Coins:
            self.url = f'https://arzdigital.com/coins/{i}'
            await self.request()
            soup = BeautifulSoup(self.HTML.text , 'html.parser')
            temp= soup.find('div' , attrs={'class':'coinPrice'}).text
            self.Cryptos[i] = temp
            await asyncio.sleep(0.01)
        

class Calculate(Crypto):
    Assets: any
    def __init__(self, Assets, *args , **kwargs) -> None:
        self.Assets= Assets
        asyncio.run(self.main())
        
    async def showUserAssets(self):
        """
        changing user crypto assets type from a string to a dictionary
        
        show user current price of cryptos and his assets
        """
        if type(self.Assets)!=dict:
            Temp_user_Dict= dict()
            self.Assets=self.Assets.split(',')
            for i in self.Assets:
                Value, Key= i.split()
                Temp_user_Dict[Key]= Value
            self.Assets= Temp_user_Dict
        
        temp_asset= str()
        while True:
            await asyncio.sleep(0.01)
            j=0
            os.system('cls')
            for i in self.Cryptos.keys():
                for asset in self.Assets.keys():
                    if i==asset:
                        temp_asset= asset
                        print(f'{j+1}. {i} : {self.Cryptos[i]}  , You own {self.Assets[i]} {i} that worth ${self.calculate(self.Cryptos[i], self.Assets[i]):.2f}')
                        j+=1 
                if temp_asset!= i:
                    print(f'{j+1}. {i} : {self.Cryptos[i]}')
                    j+=1 
            if j==7:
                break

        
    def calculate(self, CryptoValue, Asset):
        Asset= float(Asset)
        return (float(''.join(CryptoValue.split('$').pop(1).split(','))) * Asset )
        
        
    async def main(self):
        start= time.time()
        
        task3 = asyncio.create_task(self.showUserAssets())
        task1= asyncio.create_task(self.Dump())
        task2= asyncio.create_task(self.request())
        
        await task1
        await task3
        

        end = time.time()
        print(end-start)
            

class Market(Calculate):
    User_Money= int
    def __init__(self, money , assets , *args , **kwargs):
        super().__init__(assets)
        self.User_Money= money
        
        self.PlayerChoose()

    @property
    def money(self):
        return self.User_Money
    @money.setter
    def money(self, value):
        if value ==int:
            self.User_Money= value
            
    def PlayerChoose(self):
        while True:
            
            self.Player_Choose= str()
            while True:
                sys.stdout.write("\x1b[2K")
                sys.stdout.write("\x1b[1A")
                print("\nPlease choose : ", self.Player_Choose,end='')
                temp_Choose= msvcrt.getch()
                temp_Choose= temp_Choose.decode('ASCII')
                if temp_Choose== "\x1b":
                    break
                elif temp_Choose== "\x08":
                    self.Player_Choose= self.Player_Choose[:-1]
                    
                elif temp_Choose.isnumeric() :
                    self.Player_Choose+= temp_Choose
                else:
                    break
                
            try:
                if temp_Choose=="\x1b":
                    break
                if 0<int(self.Player_Choose)<8:
                    self.Player_Choose=int(self.Player_Choose)
                    self.ShoppingCrypto()
                    break
                else:
                    print("\nPlease choose a number between 1 and 7")
            except:
                print("\nPlease choose a number between 1 and 7")        
                
                    
    def ShoppingCrypto(self):
        The_Crypto= self.Coins[self.Player_Choose-1]
        os.system('cls')
        print(f'{The_Crypto} : {self.Cryptos[The_Crypto]}')
        print(f'You have : ${self.User_Money}')    
        The_bool= False
        for i in self.Assets.keys():
                if The_Crypto== i:         
                    The_bool= True 
            
        while True:  
            os.system('cls')
            if The_bool:              
                print("What do you want to do?\n1.Buy\n2.sell")
            else:
                print("What do you want to do?\n1.Buy")
                
            temp_Choose= msvcrt.getch().decode('ASCII')
            if temp_Choose=='1':
                while True:
                    os.system('cls')
                    print(f'{The_Crypto} : {self.Cryptos[The_Crypto]}\nhow much do you want to buy?  ')
                    The_Amount= input()
                    if The_Amount.isnumeric():
                        The_Amount=float(The_Amount)
                        break
                    
                os.system('cls')
                print(f'You are going to buy {The_Amount} {The_Crypto} for { self.calculate(self.Cryptos[The_Crypto],The_Amount)}\nAre You Sure?\n1.Yes\n2.No')
                temp_Choose1= msvcrt.getch().decode('ASCII')
                if temp_Choose1=='1':
                    Cost= self.calculate(self.Cryptos[The_Crypto],The_Amount)
                    self.User_Money-= Cost
                    if The_Crypto in self.Assets.keys():
                        self.Assets[The_Crypto]= float(self.Assets[The_Crypto])+The_Amount
                        break
                    else:
                        self.Assets[The_Crypto]=str(The_Amount)
                        break
                else:break    
                    
            if temp_Choose=='2':
                while True:
                    os.system('cls')
                    print(f'{The_Crypto} : {self.Cryptos[The_Crypto]} (You have {self.Assets[The_Crypto]}) \nhow much do you want to sell?  ')
                    The_Amount= input()
                    if The_Amount.isnumeric():
                        The_Amount=float(The_Amount)
                        break
                os.system('cls')
                print(f'You are going to sell {The_Amount} {The_Crypto} for { self.calculate(self.Cryptos[The_Crypto],The_Amount)}\nAre You Sure?\n1.Yes\n2.No')
                temp_Choose1= msvcrt.getch().decode('ASCII')
                if temp_Choose1=='1':
                    Cost= self.calculate(self.Cryptos[The_Crypto],The_Amount)
                    self.User_Money+= Cost
                    if The_Crypto in self.Assets.keys():
                        self.Assets[The_Crypto]= float(self.Assets[The_Crypto])-The_Amount
                        break
                else:break
            if temp_Choose=="\x1b":
                break   
        self.__init__(self.User_Money, self.Assets)

