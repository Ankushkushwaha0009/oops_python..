'''
This is called method overriding ... 
polymorphism  : 
  1 . Method Overloading  
  2 . Method Overriding 
  3 . Operator Overloading .. 

'''

#Method Overriding 
class Phone : 
    def __init__(self , price  , brand , camera) -> None:
        
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera 

    def buy(self) :
        print('Buying a Phone')

class SmartPhone(Phone) :

    def buy(self):
        print('Buying a smartphone')

s  = SmartPhone(4003 , 'Apple' , 45)
s.buy() 
