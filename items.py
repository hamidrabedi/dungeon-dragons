import random

class items:
    HpRegen: int
    HP: int
    Damage: int
    Critical: int
    
    def __init__(self) -> None:
        self.itemslist()
        self.itemsprice()
    
    
    def itemslist(self) -> list:
        self.Items_list= ['lucky rainbow', 'red daddy', 'atomic blade']
        return self.Items_list
    
    def itemsprice(self) -> dict:
        self.Items_price= {'luckyrainbow_price': 20000 ,'reddaddy_price': 45000 ,'atomicblade_price': 30000}
        return self.Items_price
    
    def luckyrainbow(self):
        if random.randint(1,100) <30:
            self.Critical= 3
        else:
            self.Critical= 1
    
    def atomicblade(self):
        self.Damage+=200
    
    def reddaddy(self):
        self.HpRegen+= 2
        self.HP += 500
    
    
