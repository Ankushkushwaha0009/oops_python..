# # clas B class A ko Inherit kar raha hai and class B ke padss constructor nahi  hai to
# # wo class A ke pass jayega and check karega  ... 
# class Phone : 
#     def __init__(self , price  , brand , camera) -> None:
#         print("Inside Phone Constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera 

#     # def buy(self)  :
#     #     print('Buying a Phone')
    
#     # def return_phone(self)  :
#     #     print('Returning a phone')

# # class FeaturePhone(Phone)  :
# #     pass

# class SmartPhone(Phone)     :
#     pass

# s  = SmartPhone(4003 , 'Apple' , 45)
# print(s.brand)

# ---------------Inheriting Private Members  ... 

'''
   child class object cannot be able to access the hidden or private member of  base class . . .
'''
class Phone : 
    def __init__(self , price  , brand , camera) -> None:
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera 

    def buy(self)  :
        print('Buying a Phone')
    
    def return_phone(self)  :
        print('Returning a phone')

class FeaturePhone(Phone) :
    pass

class SmartPhone(Phone) :
    def check(self)  :
        print(self.__price)

s  = SmartPhone(4003 , 'Apple' , 45)
s.check()