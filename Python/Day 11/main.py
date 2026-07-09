import cal as cal
import greeting as greet

a = cal.add(10, 12)
print(a)

b = cal.sub(12,10)
print(b)

c = cal.multiply(50, 50)
print(c)

d = cal.div(10, 0)
print(d)

e = cal.div(10, 2)
print(e)

print(greet.meeting("Manjeet"))
print(greet.bye("Manjeet"))

"""
DSA Practice (45–60 minutes)
Problem 1
Reverse a list without using:
reverse()
slicing ([::-1])
Think about traversing the list from the last index to the first.
What is the input?
string 
What is the output?
reversed string

we will run a loop over the string for ch in range(len(string), 1) inside loop we will save each ch into another variable like reversed_string + ch

Problem 2

Find the smallest element in a list using O(n).
Before coding, answer:
What is the input?
elements for the list
What is the output?
smallest ele
What variable will you maintain while traversing the list?
we will create a vaiable named smallest_ele = list [0]

run a for loop over the list
and then compare each elemnt with smallest_ele if elemnt of list < smallest_element -> smallest_ele = elemnt 
"""