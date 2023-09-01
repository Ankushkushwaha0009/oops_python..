class Computer : 
    def __init__(self , name , roll) -> None:
        self.name = name 
        self.roll = roll 
    def config(self , age) :
        print("Name is : " , self.name)
        print("Roll is : " , self.roll)
        print("age is  : " , age)

comp1 = Computer('ankush' , 90) 
comp2 = Computer('vishal' , 100) 
comp1.config(200)  
comp2.config(300) 



