class Student :
    def __init__(self , name , age , id ):
        self.name = name
        self.age = age
        self.id = id
    def introduce(self):
        print(f"my name is {self.name} , i am {self.age} years old and my id is {self.id}")


# student = Student("Benz" , 19 , "42942167")
# student.introduce()

class Person (Student):
    def teach(self):
        print(f"{self.name} is teaching")
        print(f"He was {self.age} years old when he started  teaching")
       
class Intel (Student):
    def study(self):
        print(f"{self.name} is studying")
       
       

teacher = Person("Ben" , 24 , "9890")
teacher.teach()

student = Intel("Naomi" , 24 , "9890")
student.study()

    