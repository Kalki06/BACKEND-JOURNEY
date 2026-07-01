# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# def add (num1, num2):
#     return num1 + num2

# print(add(num1, num2))

# num1 = int(input("Enter a number : "))

# def square(num):
#     return num * num

# print(square(num1))

# num1 = int(input("Enter a number : "))

# def iseven(num):
#     res = True

#     if(num % 2 != 0):
#         res = False
    
#     return res

# print(iseven(num1))

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def maximum(num1, num2):
    if(num1 > num2):
        return num1
    elif(num2 > num1):
        return num2
    else:
        return "both are equal"

print(maximum(num1, num2))