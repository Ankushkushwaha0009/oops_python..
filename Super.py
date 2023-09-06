# class Phone : 
#     def __init__(self , price , brand , camera) -> None:
#         print("Inside Phone constructor ")
#         self.__price = price
#         self.brand   = brand 
#         self.camera  = camera

#     def buy(self) :
#         print("Buying a phone")

# class SmartPhone(Phone) :
#     def buy(self) :
#         print("Buying a smartphone")
#         # parent ke method ko and constructor ko call kar sakte hoo ... 
#         # attributes bhi app access nahi kar sakte  ... 
#         super().buy()

# s = SmartPhone(2000 , 'Apple' , 13) 
# s.buy()


# -------- Super example with consutructor  ---------


# class Phone : 
#     def __init__(self , price , brand , camera) -> None:
#         print("Inside Phone constructor ")
#         self.__price = price
#         self.brand   = brand 
#         self.camera  = camera

# class SmartPhone(Phone) :
#     def __init__(self, price, brand, camera , os , ram) -> None:
#         # parent ko construtor ko call kar raha hai  .. 
#         super().__init__(price, brand, camera)
#         self.os  = os 
#         self.ram  = ram 
#         print("Inside the  SmartPhone constructor ")

# s = SmartPhone(2000 , 'Apple' , 13 , 'Android' , 10) 
# print(s.os)
# print(s.brand)


# -------Example on Super  ---- ----------- ---------
class Parent : 
    def __init__(self , num) -> None:
        self.__num = num 

    def get_num(self) : 
        return self.__num

class  Child(Parent)  :
    def __init__(self, num , val) -> None:
        # this should be your first statement ... 
        super().__init__(num)
        self.__val = val

    def get_val(self) : 
        return self.__val
    
son = Child(100 , 200)
print(son.get_num())
print(son.get_val())




