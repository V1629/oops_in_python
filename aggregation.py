class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.change_address(new_city,new_pin,new_state)

class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode = pincode
        self.state = state
    
    def change_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state=new_state


add=Address("kolkata",23010,"UP")
cust = Customer("vaibhav","Male",add)
cust.edit_profile("ankit","gurgaon",23008,"haryana")
print(cust.address.pincode)
#overall this code ye conclude krna chah rha hai ki customer class khud kaam nhi kr rha ....wah address class se kaam krwa rha
#usko address related koi bhi kaam krna hoga to bhi wo address class ke methods ko call krke krna hoga
#isi relation ko you call aggregation kehte hai