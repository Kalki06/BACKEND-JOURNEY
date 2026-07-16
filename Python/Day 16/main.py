class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_Info(self):
        print(f"Name = {self.name}")
        print(f"age = {self.age}")

    def speak(self):
        print("some sound")


class Dog(Animal):

    def __init__(self, name, breed, age):
        super().__init__(name, age)
        self.breed = breed

    def print_Info(self):
        print(f"Name = {self.name}")
        print(f"age = {self.age}")
        print(f"Breed Name = {self.breed}")

    def speak(self):
        print("Bark")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("Meow")

d1 = Dog("Tommy", "Pitbull", 5)
d1.print_Info()
d1.speak()

c1 = Cat("Billu", 3)
c1.print_Info()
c1.speak()

"""
DSA

Problem 1
Move all zeros to the end.

Example:
Input:
[0,1,0,3,12]
Output:
[1,3,12,0,0]

we will create two variables i = 0 and j = 1
now will run a while loop on the list until i < len(list)
if(element[i] == 0 and element[j] != 0) -> swap(eleemnt[i] and element[j]), i++, j++
elif(element[j] == 0 and element[i] != 0 )i++, j++
elif(element[j] == 0 and element[i] == 0 )i++, j++
else-> j++


Problem 2
Remove duplicates from a sorted array.
we will create two variables i = 0 and j = 1
now will run a while loop on the list until j <= len(list)
inside loop if element[i] == element[j] -> pop[element[j]] j++
else i = j, j++
"""