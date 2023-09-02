class Customer : 
    def __init__(self , name , gender) -> None:
        self.name = name 
        self.gender = gender 


def greet(customer) :

    if customer.gender == 'male' : 
        print("hello" , customer.name , "sir")
    else:
        print("Hello" , customer.name , "mam")

    cust2 = Customer('vishal' , 'male')
    return cust2


cust = Customer('Ankush' , 'female')
print(cust.name)
obj = greet(cust)
print(obj.name , obj.gender)

