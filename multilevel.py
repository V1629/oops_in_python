class Product:
    def review(self):
        print("product customer review")

class Phone(Product):
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera=camera

    def buy(self):
        print("buying a phone")

    def return_phone(self):
        print("returning a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000,'Apple',12)
p=Phone(1000,'samsung',1)
s.buy()
s.review()
p.review()