history = []

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
    


while(True):

    print("Calculator\n")

    menu()
    user_choice = int(input("Enter your choice in number : \n"))

    if(user_choice == 0):
        break

    elif user_choice == 5:
        if(len(history) != 0):
            for ele in history:
                print(ele)
        else:
            print("There is no History available")

    elif user_choice not in operations:
        print("Invalid choice. Try again.")
        continue


    else:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))

        result = operations[user_choice](num1, num2)
        print(result)
        match user_choice:
            case 1 :
                history.append(f"{num1} + {num2} = {result}")
            case 2:
                history.append(f"{num1} - {num2} = {result}")
            case 3:
                history.append(f"{num1} * {num2} = {result}")
            case 4:
                history.append(f"{num1} / {num2} = {result}")
            case _:
                history.append("error")

"""
dsa
1.Find the largest element in a list.
input = elements for the list
output = maximum element
approach = create a variable named maximum and initalize it with the first element of the list then run a loop over list and compare each element with that maximum if list[i] > maximum -> maximum = list[i]

2. Count how many numbers are greater than 50.
input = elements for the list
output = count of numbers which are greater than 50
approach  =  we will initaliza a variable name count with 0 then run a loop over list and compare each element if element > 50 -> count++;
outside loop print the count.
"""