class Computer : 
    def config(self) :
        print("19 , 16gb , 1tb") 

comp1 = Computer() 
comp2 = Computer() 

Computer.config(comp1)   
Computer.config(comp2) 

# but here it take comp1 as an argument 

comp1.config()  
comp2.config() 

