#       # ----- Example 1 --- 
# class Parent  :
#     def __init__(self , num) -> None:
#         #this vale here will never intialized 
#         self.__num = num 

    
#     def get_num(self) :
#         #then also we are accessing this value without any intialization definately this will throw an  error 
#         return self.__num
    
# class Child(Parent)  :
#     def __init__(self, val  , num) -> None:
#         self.__val = val 

#     def get_val(self)  : 
#         return self.__val

# son = Child(100  , 10) 
# print("Parent Num  : " , son.get_num())

# ---- Example 2 ---- 

# class A : 
#     def __init__(self) -> None:
#         self.var1 = 100 

#     def display1(self , var1)  :
#         self.var2  = var1
#         print("..." , self.var2)
#         print("Class A  : " , self.var1)

# class B(A)  :
#     def display2(self , var1)  :
#         print("class B" , self.var1)

# obj = B() 
# obj.display1(1200)

#  ----  Example 3  

# class Parent  : 
#     def __init__(self , num ) -> None:
#         # protected --> this variable can be access inside the class  and child of this class will acess this variable  
#         self._num = num 

#     def get_num(self)  :
#         return self._num
    
# class Child(Parent)  : 

#     def __init__(self, val , num) -> None:
#         self._val = val 
#         self._num  = num

#     def get_val(self) : 
#         return self._val

# son = Child(100 , 10)
# print(son.get_num())

