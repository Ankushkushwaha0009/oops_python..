class Atm : 
    def __init__(self) -> None:
        self.__pin = "" 
        self.__balance = 0  
        self.__menu()
        
        
    def get_pin(self) :
        return self.__pin

    
    
    def set_pin(self , new_pin)  :
          if type(new_pin) == str:
              self.__pin = new_pin
              print("Pin changed")
          else:
              print("Not Allowed")
                

    def __menu(self) :
        
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
               

    def create_pin(self)  : 
        self.__pin  = input("Enter your pin  : ") 
        print("Pin set sucessfully !!")

        
    
    def deposit(self)  :
        temp = input("Enter your pin : ") 
        if temp == self.__pin  : 
            amount = int(input("Enter your Amount  :"))
            self.__balance += amount 
        else:
            print("Invalid Pin")

            

    def withdraw(self)  :
        temp = input("Enter your pin : ") 
        if temp == self.__pin  : 
            amount = int(input("Enter the amount you want to withdraw : "))
            if amount <= self.__balance : 
                self.__balance -= amount
                print("Operation is successful")
            else:
                print("Insufficient funds ")
        else:
            print("Invalid Pin")

            

    def checkbalance(self)  :
        temp =  input("Enter your pin :  ")
        if temp == self.__pin  :
            print(f'your current balance is ${self.__balance}')
        else:
            print("Invalid pin ")

            
    
    def quit(self) : 
        print("Thanks for choosing this bank")

