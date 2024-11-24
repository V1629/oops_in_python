#technically speaking python me method overloading kaam nhi krti hai par aap dimaag laga ke kaam krwa skte ho
class Geometry:

    def area(self,a,b=0):
        if b==0:
            print("circle",3.14*a)
        else:
            print("rectangle",a*b)

obj=Geometry()
obj.area(4)
obj.area(4,5)

#operator overloading=a feature in object-oriented programming (OOP) that allows you to redefine or "overload" the meaning of standard operators (like +, -, *, etc.) for user-defined types (e.g., classes). In Python, this is done by defining special methods (also called "magic methods" or "dunder methods") in a class.