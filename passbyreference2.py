#now main thing about passby reference
#this program shows--->class ke objects are also mutable like list,dict and sets 
#to mtlb aapke objects me changes ho skte hai agar aap kisi function me bhej rhe ho to .
#to isko prevent krne ke lie object ka clone ya list ka clone bhejna chahiye ,taaki original object me koi change na ho .
class Customer:
    def __init__(self,name):
        self.name = name

def greet(customer):
    print(id(customer))
    customer.name="Vaibhav"
    print(customer.name)
    print(id(customer))

cust=Customer("Ankita")

print(id(cust))
greet(cust)
print(cust.name)