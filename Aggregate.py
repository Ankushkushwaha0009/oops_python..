class Customer : 
    def __init__(self , name , gender , addres) -> None:
        self.name = name 
        self.gender  = gender
        self.address = addres 
    
    def edit_profile(self , new_name , new_city  , new_pin  , new_state)  :
        self.name  = new_name 
        self.address.change_address(new_city , new_pin , new_state)

class Address :
    def __init__(self , city , pincode , state) -> None:
        self.city  = city 
        self.pincode = pincode
        self.state = state 

    def change_address(self , new_city , new_pin , new_state) :
        self.city = new_city
        self.pincode = new_pin
        self.state  = new_state

add = Address('kolkata' , 74734 , ' west-bengal ')
cust = Customer('Nitish' , 'Male' ,  add)
cust.edit_profile('Ankit' ,'Gurgaon' , 1256153 , "haryana")

print(cust.address.city)

