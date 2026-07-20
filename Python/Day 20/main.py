class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, My name is {self.name} and my age is {self.age}")

class Student(Person):

    def __init__(self, name, age, roll_num):
        super().__init__(name, age)
        self.roll_num = roll_num

    def study(self):
        print("I am studing in class 6th")

student1 = Student("Abhi", 12, 9)
student1.introduce()