# Upgrade your Calculator.
# Don't rewrite everything.
# Add exception handling around user input.

# It should handle:
# entering letters instead of numbers
# entering an invalid menu choice
# opening history.txt before it exists

# Think about this first:
# Where should the try block begin?
# What code belongs inside it?
# What specific exceptions do you expect?

def menu():
    print("0. Exit\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History")

def add(num1, num2):
    res = num1 + num2
    return(res)

def sub(num1, num2):
    res = num1 - num2
    return(res)

def multiply(num1, num2):
    res = num1 * num2
    return(res)

def div(num1, num2):
    try:
        res = num1/ num2
        return res
    except ZeroDivisionError:
        return "Division by Zero is not possible !! "




operations = {
    1:add,
    2:sub,
    3:multiply,
    4:div
}

symbols = {
    1:'+',
    2:'-',
    3:'*',
    4:'/'
}


while(True):

    print("Calculator\n")

    menu()
    try:
        user_choice = int(input("Enter your choice in number : \n"))

        if(user_choice == 0):
            break

        elif user_choice == 5:
            try:
                with open("history.txt", "r") as file:
                    content = file.read()
                    if(len(content) != 0):
                        print(content)
                    else:
                        print("There is no history available now. \n ")
            except FileNotFoundError:
                print("There is no such file.")

        elif user_choice not in operations:
            print("Invalid choice. Try again.")
            continue


        else:
            try:
                num1 = int(input("First number: "))
                num2 = int(input("Second number: "))
            except ValueError:
                print("Please enter integers only.")

            op = symbols[user_choice]

            result = operations[user_choice](num1, num2)
            print(f"{result}\n")

            if result is not str:
                try:
                    with open ("history.txt", "a") as file:
                        file.write(f"{num1} {op} {num2} = {result}\n")
                except FileNotFoundError:                   
                    print("File not found !!!!")

    except ValueError:
        print("Please enter the integer only\n")

"""
DSA
Problem 1
Find the second largest element in a list.
Before coding, write:

Input
elements for the list
Output
second largest element
Algorithm
can't comw up with solution there is one thing we can do is sort the list and the return the elemnt at list[n-2]
Time Complexity


Reverse a list without using list.reverse().
create a new lust called reversed_list = [];
then run a backward loop over the list like element in range(len(list): 1):
reversedlist .append[ element]
return the reversed list
"""