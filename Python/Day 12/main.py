# class calculator:
#     def add(self, a, b):
#         return a + b
    
#     def sub(self, a, b):
#         return a - b
    
#     def multiply(self, a, b):
#         return a * b
    
#     def div(self, a, b):
#         if(b == 0):
#             return "Division by zero is not valid"
#         else:
#             return a / b
    
# cal = calculator()

# a = cal.add(2,3)
# print(a)

# b = cal.sub(5, 1)
# print(b)

# c = cal.multiply(5, 5)
# print(c)

# d = cal.div(2, 0)
# print(d)

# e = cal.div(9, 3)
# print(e)

class student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"I study {self.course}.")

s1 = student("Manjeet", 20, "BCA")
s1.introduce()

"""
DSA 
Problem 1
Find the largest element in a list.

input
elements for the list

output
largest element of the list

approach
create a variable called largest_ele and initalize it with list[0]
now run a loop over the list and compare each element with the largest_ele if element > largest_ele -> largest_ele = element
outside loop print the argest_ele


Count how many times a number appears in a list.
input
elemnts of the list and the target value

output
count of the the taregt

appraoch
create a variable called count_target intizle it with 0
ten run aloop ove the list and inside list if elemnt == taget -> count_taget++
outside loop print thr count_target
"""

    