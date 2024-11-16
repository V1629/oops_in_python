class Atm:

    counter =1 #a static variable that is shared by all instances of the class and is different for every object
    def __init__(self):
        self._pin = ""  # Corrected from self__pin
        self._balance = 0  # Corrected from self__balance
        self.sno = Atm.counter
        Atm.counter += 1
        self.menu()

    @staticmethod
    def get_counter():
        return Atm.get_counter
    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("not allowed")
    
    def menu(self):
        user_input = input("""
                           Hello, how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           """) 
        if user_input == "1":
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
        self._pin = input("Enter your pin: ")
        print("Pin set successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self._pin:
            amount = float(input("Enter the amount you want to deposit: "))
            self._balance += amount  # Fixed incorrect addition
            print("Amount deposited successfully")
        else:
            print("Invalid pin")
        self.menu()

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self._pin:
            amount = float(input("Enter the amount you want to withdraw: "))
            if amount > self._balance:
                print("Insufficient balance")
            else:
                self._balance -= amount
                print("Amount withdrawn successfully")
        else:
            print("Invalid pin")
        self.menu()

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self._pin:
            print("Your balance is", self._balance)
        else:
            print("Invalid pin")
        self.menu()

# Create an instance of Atm
sbi= Atm()