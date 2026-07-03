student = {
    "name": "Kalki",
    "age": 21,
    "course": "BCA"
}

print(student["name"])
student["age"] = 20
print(student["age"])
student["city"] =  "Delhi"
print(student["city"])
student.pop("course")
print(student)

for key, value in student.items():
    print(key)

for key, value in student.items():
    print(value)

for key, value in student.items():
    print(f"{key} : {value}")

# DSA
"""
1. Find the smallest element in a list.
What is the input?
elements of the list
What is the output?
element
What is the approach?
intilize a variable with sys.maxint then loop over the list and compare all the elements if element is smaller than the current element than change that variable value with the elemnt 
outside loop return the vriable
What is the time complexity?
big O(n)

2.Count how many even and odd numbers are in a list.
What is the input?
element for the list
What is the output?
count of odd and even elemnt
What is the approach?
initailze two vaibles odd and even with zero
now loop over the list and each elemt % 2 == 0 -> even++ else odd++
outside loop return odd and even 
What is the time complexity?
big O(n)

3. Find the average of all numbers in a list.
What is the input?
elemnts for the list
What is the output?
avrage of sum
What is the approach?
create a variable name total and intialize it with 0 
then loop over the list and total = total + elemnt
then outsode loop create a variable avg = total/ len(list)
What is the time complexity?
bigO(n)
"""