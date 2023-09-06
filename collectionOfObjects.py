class Customer :
    def __init__(self ,  name ,  age) -> None:
        self.name = name 
        self.age  = age

    def intro(self) : 
        print('I am' , self.name , 'and I am' , self.age , 'years old')

c1 = Customer('Nitish' , 23) 
c2 = Customer('Ankit'  , 34) 
c3 = Customer('Neha'   , 32) 

# list of objects 
l = [c1 , c2 , c3]
for i in l :
    i.intro()