#agar aap ek function ko string,list . dictionary,etc de skte ho to aone class ka object bhi de skte ho as well as us functin se object return bhi kr skte ho
class Customer:
    def __init__(self, name,gender):
        self.name=name
        self.gender=gender

def greet(customer):
    if customer.gender == "Male":
        print("hello",customer.name,"sir")
    else:
        print("hello",customer.name,"mam")

    cust2=Customer("tanya","female")#ye bas ye skow kr rha hai ki wo object bhi return kr skta hai irrespective of the logic.
    return cust2




cust=Customer("vaibhav","Male")
new_cust=greet(cust)
print(new_cust.name)