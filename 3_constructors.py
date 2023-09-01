# constructor is a as special type of method where we write the that code 
# which we are hiding from user means we are not giving any access to user to
# see that code  ... 

class Computer:
    def __init__(self):
        self.name = 'Navin'
        self.age = 89
    
    def update(self):
        # adress of c1 it means c1 object is passed inside a self 
        # print(id(self))
        self.name = "Ankush kushwaha "
        self.age = 100

c1 = Computer()
c2 = Computer()

# print(id(c1))
# c1.update()
print(c1.name)

# age will be modified in a c1 object 
c2.update() 

print(c1.age)
# print(c2.age)
print(c2.name)
print(c2.age)
