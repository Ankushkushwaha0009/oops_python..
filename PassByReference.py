# 
# class Customer : 
#     def __init__(self , name , gender) -> None:
#         self.name = name 
#         self.gender = gender 

# def greet(customer) :
#     if customer.gender == 'male' : 
#         print("hello" , customer.name , "sir")
#     else:
#         print("Hello" , customer.name , "mam")

#     cust2 = Customer('vishal' , 'male')
#     return cust2

# cust = Customer('Ankush' , 'female')
# print(cust.name)
# obj = greet(cust)
# print(obj.name , obj.gender)

'''
pass by reference 

'''
# class Customer : 
#     def __init__(self , name) -> None:
#         self.name = name 

# def greet(customer) :
#     # print(id(customer))
#     # customer.name = "Nitish"
#     print(customer.name)
   
# cust = Customer('Ankush')
# # print(id(cust))
# greet(cust)
# print(cust.name)


def Change(L) :
    print(id(L))
    L.append(5)
    print(id(L))

L1 = [1 , 2 , 3 ,  4]
print(id(L1))
print(L1)
Change(L1)
print(L1)