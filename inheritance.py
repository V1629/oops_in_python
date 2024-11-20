class User:
    def login(self):
        print("login")
    
    def register(self):
        print("register")
    
class Student(User):
    def enroll(self):
        print("enroll")
    def review(self):
        print("review")

student = Student()
student.login()
student.register()
student.enroll()
student.review()
#even aap inheritance ka use krke parent class ka constructor bhi call kr skte ho
#child class ,parents class ke private members ko access nhi kr skta
 