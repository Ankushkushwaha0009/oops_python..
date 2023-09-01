class Atm : 
    def __init__(self) -> None:
        self.pin = "" 
        self.balance = 0  
        self.menu()

    def menu(self) :
        q = True 
        while q : 
            print("--------***----------")
            user_input = input(""" 
                Hello How would like you to proceed
                1.Enter 1 to Create Pin 
                2.Enter 2 to deposit
                3.Enter 3 to withdraw
                4.Enter 4 to checkbalance
                5.Enter 5 to Exit 
                print("*****************")
            """)

            if user_input == "1"   : 
                self.create_pin()
            elif user_input == "2" :
                self.deposit()
            elif user_input == "3" :
                self.withdraw()
            elif user_input == "4" :
                self.checkbalance()
            else :
                self.quit()
                q = False 

    def create_pin(self)  : 
        self.pin  = input("Enter your pin  : ") 
        print("Pin set sucessfully !!")
    
    def deposit(self)  :
        temp = input("Enter your pin : ") 
        if temp == self.pin  : 
            amount = int(input("Enter your Amount  :"))
            self.balance += amount 
        else:
            print("Invalid Pin")

    def withdraw(self)  :
        temp = input("Enter your pin : ") 
        if temp == self.pin  : 
            amount = int(input("Enter the amount you want to withdraw : "))
            if amount <= self.balance : 
                self.balance -= amount
                print("Operation is successful")
            else:
                print("Insufficient funds ")
        else:
            print("Invalid Pin")

    def checkbalance(self)  :
        temp =  input("Enter your pin :  ")
        if temp == self.pin  :
            print(f'your current balance is ${self.balance}')
        else:
            print("Invalid pin ")
    
    def quit(self) : 
        print("Thanks for choosing this bank")
    
    def dhkhhf(self)  :
        pass 

a = Atm() 

