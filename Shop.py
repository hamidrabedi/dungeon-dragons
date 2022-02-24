import os
import items as Item

class Shop:

    
    def __init__(self, money,P_items, *args, **kwargs):
        self.P_items= P_items
        self.money = money
        
        self.ShowPlayer()
        
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, value):
        if type(value) != int:
            print("Money must be an integer!")
            # raise ValueError('money must be an integer')
        else:
            self.__money = value
    @property
    def P_items(self):
        return self.__P_items
    @P_items.setter
    def P_items(self, value):

        if type(value)!=str:
            print("Items must be an str object")
        else:
            value= value.split(',')
            self.__P_items= value
    
    
    
    def playerItems(self):
        pass
    
    def ShowPlayer(self):
        self.Items_List= Item.items.itemslist(self)
        self.Items_Price= Item.items.itemsprice(self)
        
        os.system('cls')
        print(f"Your Items: {','.join(self.P_items)}")
        print("What do you want to buy?")
        for i in range(len(self.Items_List)):
            print(f'{i+1}. {self.Items_List[i]}')

        
    def Buy(self):
        pass
    
    
test= Shop(100_000, 'atomic blade, red daddy')




