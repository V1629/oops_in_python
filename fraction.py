#ek class banayenge jo fraction pe operation hote hain wo handle krega
class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def  __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den=self.den*other.den

        return "{}/{}".format(new_num,new_den)
    def  __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den=self.den*other.den

        return "{}/{}".format(new_num,new_den)

x=Fraction(3,4)
y=Fraction(4,3)
print(x+y)  # Output: 25/12
print(x-y)


