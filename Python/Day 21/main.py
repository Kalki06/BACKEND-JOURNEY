# exercise 1
# class Animal:
#     def speak(self):
#         print("Animal Sound")

# class Dog(Animal):

#     def speak(self):
#         print("Bark")

# class Cat(Animal):

#     def speak(self):
#         print("Meow")

# d1 = Dog()
# c1 = Cat()

# d1.speak()
# c1.speak()

# exercise 2

# class Employee:

#     def __init__(self, name, salary):
#         self.name =  name
#         self.salary = salary

#     def display_info(self):
#         print(f"Name : {self.name}")
#         print(f"Salary : {self.salary}")

# # class Manager(Employee):

# #     def __init__(self, name, salary, department):
# #         super().__init__(name, salary)
# #         self.department = department

# #     def display_info(self):
# #         print(f"Name : {self.name}")
# #         print(f"Salary : {self.salary}")
# #         print(f"Department : {self.department}")

# exercise 3
# class Manager(Employee):

#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department

#     def display_info(self):
#         print(f"Name : {self.name}")
#         print(f"Salary : {self.salary}")
#         print(f"Department : {self.department}")

# m1 = Manager("Alice", 100000, "Marketing")
# m1.display_info()


# exercise 4
# class Animal:
#     def speak(self):
#         print("Animal Sound")

# class Dog(Animal):

#     def speak(self):
#         print("Bark")

# class Cat(Animal):

#     def speak(self):
#         print("Meow")

# d1 = Dog()
# c1 = Cat()

# d1.speak()
# c1.speak()

# print(
# isinstance(Dog, Animal),
# isinstance(d1, Dog),
# isinstance(d1, Animal),
# isinstance(c1, Animal))
# exercise 5
# print(issubclass(Dog, Animal))
# print(issubclass(Cat, Animal))
# print(issubclass(Animal, Dog))

# exercise 6

class Vehicle:

    def start(self):
        print("Vehicle has started")

    def stop(self):
        print("Vehicle has stopped")

class Bike(Vehicle):

    def start(self):
        print("Bike has started")

    def stop(self):
        print("Bike has stopped")

class Car(Vehicle):

    def start(self):
        print("Car has started")

    def stop(self):
        print("Car has stopped")

class Truck(Vehicle):

    def start(self):
        print("Truck has started")

    def stop(self):
        print("Truck has stopped")

b = Bike()
c = Car()
t = Truck()

b.start()
b.stop()

c.start()
c.stop()

t.start()
t.stop()

print(isinstance(t, Vehicle))
print(isinstance(Vehicle, Bike))
print(isinstance(Vehicle, Truck))
print(isinstance(t, Truck))
print(isinstance(Truck, Bike))

print(issubclass(Vehicle, Bike))
print(issubclass(Truck, Bike))
print(issubclass(Truck, Vehicle))
