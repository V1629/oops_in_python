class Phone:
    def __init__(self, brand, camera, price):
        self.brand = brand
        self.camera = camera
        self.price=price

    def buy(self):
        print("buying a phone")

  

class Product:
    def review(self):
        print("customer review")

class SmartPhone(Phone,Product):
    pass

s=SmartPhone(20000,"Apple",12)
s.buy()
s.review()
#ab problem ye hai ki buy method phone wala exexcute hoga ya product wala
#Ans:MRO=Method resolution order>>>>jo class ko pehle likhoge usko buy method execute hoga
#an additional info:self kon hai?
#self ....jo object banaoge ,whi object ka reference hai mtlb jo kaam object krega bahar se whi kaam self krega method ke andar se