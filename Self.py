# jis Object ke sath kam kar rahe ho wahi self hota hai  ... 
class Student  : 
    def __init__(self) -> None:
        # print(id(self))
        self.myage()
    
    def myname(self) :
        print("my name is ankush ") 

    def myage(self) :
        print("my age is 20")


S = Student() 
Student.myname(S)

# print(id(S))
# S1 = Student()
# print(id(S1)) 

