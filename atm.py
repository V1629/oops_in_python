class Atm:
# __init__ = a constructor is a special method jiske andar jo code likhe honge wo automatically execute hote hain jb hum  object create karte hain

    def __init__(self):

        self__pin = ""
        self__balance = 0


        self.menu()
    
    def menu(self):

        user_input = input("""
                           Hello,how would you like to proceed?
                           1.enter 1 to create pin
                           2.enter 2 to deposit
                           3.enter 3 to withdraw
                           4.enter 4 to check balance
                           5. enter 5 to exit""" ) 
        if  user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.pin = input("enter your pin")
        print("pin set successfully")
        self.menu()
    def deposit(self):
        temp = input("enter yopur pin")
        if temp == self.pin:
            amount = float(input("enter the amount you want to deposit"))
            self.balance += self.balance+amount
            print("amount deposited successfully")
        else:
            print("invalid pin")
        self.menu()
    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = float(input("enter the amount you want to withdraw"))
            if amount > self.balance:
                print("insufficient balance")
            else:
                self.balance -= amount
                print("amount withdrawn successfully")
        else:
            print("invalid pin")
        self.menu()
    def check_balance(self):
        temp=input("enter your pin")
        if temp == self.pin:
            print("your balance is",self.balance)
        else:
            print("invalid pin")
        self.menu()
    
atm = Atm()
#pyhton me kuch special methods hote hain ,predefined hote hain
#identification=aage bhi double underscore aur aage bhi
#inko object calll nhi krta .ye given conditions pe call ho jate hain,ye jo upar self.menu() baar baar call kiye ho uska solution hai 
#kyu python me har methods ko self ki jarurat hai
#since ek hi class k edo methods ek dusre ko access nhi kr skte
#access krne ka ek hi tareeka hai>>>objects ke through
#what is an instance variable>>>class ke andar ka wo variable jiska value har object ke liye alag hota hai
#double underscor elaga ke values ko hide kr skte ho aur koi methods ko bhi
