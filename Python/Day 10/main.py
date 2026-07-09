# Exercise 1
# Ask the user for a number.

# try:
#     num = int(input("Enter the number : "))
# except ValueError:
#     print("Please enter only integer.")

# Divide two numbers.
# Handle division by zero

# try:
#     num1 = int(input("Enter the first number : "))
#     num2 = int(input("Enter the second number : "))
#     try:
#         res = num1/ num2
#         print(res)
#     except ZeroDivisionError:
#         print("Division by zero is not possible.")

# except ValueError:
#     print("Invalid input")

# Exercise 3
# Open a file that doesn't exist.
# Instead of crashing, print:

# try:
#     with open ("notes.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not exist")


# Exercise 4
# Combine everything:
# Read a number
# Divide
# Print result
# Always print:
# Program Finished

# using finally.

try:
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    try:
        res = num1/ num2
        print(res)
    except ZeroDivisionError:
        print("Division by zero is not possible.")
except ValueError:
    print("Invalid input")

finally:
    print("Program Finished")