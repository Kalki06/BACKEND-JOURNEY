
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
    if(num2 == 0):
        return "Division by 0 is not posible"
    else:
        res = num1 / num2
        return(res)



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
    user_choice = int(input("Enter your choice in number : \n"))

    if(user_choice == 0):
        break

    elif user_choice == 5:
        with open("history.txt", "r") as file:
            content = file.read()
            if(len(content) != 0):
                print(content)
            else:
                print("There is no history avaliable now. \n ")

    elif user_choice not in operations:
        print("Invalid choice. Try again.")
        continue


    else:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        op = symbols[user_choice]

        result = operations[user_choice](num1, num2)
        print(result)
        with open ("history.txt", "a") as file:
            file.write(f"{num1} {op} {num2} = {result}\n")


"""
Problem 1
Find the smallest element in a list.

Input
elements for the list

Output
smallest number

Algorithm
first we will create a variable name smallest_element and initalize it with list[0]
than run a loop over list and compare each element with that variable is num < smallest_element -> smallest_element = num
outside loop we will print smallesr_elemnt

Time Complexity
Big O(n)

Problem 2
Count how many even numbers are present in a list.

Input
elements for the lsit

Output
count of even numbers 

Algorithm
forst we will create a variable name count_even = 0 than we will run a loop over list and check if num %2 == 0 -> count_even++
outside loop we will print the count_even

Time Complexity
Big O(n)
"""