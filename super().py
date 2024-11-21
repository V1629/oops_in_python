#some more examples of super function
class Phone:

    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price=price
        self.__brand=brand
        self.camera=camera

class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("inside smartphone constructor")

s=SmartPhone(2000,'Smasung',12,'Android',2)

print(s.os)
print(s.brand)