#how to inherit a constructor?
#ans:agar child class ke pass constructor nhi hai to ,jb hm uska object banayenge tb automatic parents class ka construcotr call hoga.

#kya parents class ke private members ko access kr paayegea?
#super() method use krke aap parent class ke constructor ko aur method ko invoke kr skte ho>>>>method overriding ke samay
#some expamples on super function
class Parent:
    def __init__(self, num):  # Added num parameter to the constructor
        self.__num = num  # Fixed the assignment to use the parameter

    def get_num(self):
        return self.__num
    
class Child(Parent):
    def __init__(self, num, val):
        super().__init__(num)  # Correctly calling the parent constructor with num
        self.__val = val
    
    def get_val(self):  # Corrected method name from get_value to get_val
        return self.__val
    

son = Child(100, 200)
print(son.get_num())  # This will print 100
print(son.get_val())  # Corrected method call to get_val
#agar child ke pass apna constructor hai to parents ka constructor invoke nhi hota hai