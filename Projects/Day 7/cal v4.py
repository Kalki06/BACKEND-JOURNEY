history = []

def menu():
    print("0. Exit\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History")

def add(num1, num2):
    res = num1 + num2
    history.append(f"{num1} + {num2} = {res}")
    return(res)

def sub(num1, num2):
    res = num1 - num2
    history.append(f"{num1} - {num2} = {res}")
    return(res)

def multiply(num1, num2):
    res = num1 * num2
    history.append(f"{num1} * {num2} = {res}")
    return(res)

def div(num1, num2):
    if(num2 == 0):
        return "Division by 0 is not posible"
    else:
        res = num1 / num2
        history.append(f"{num1} / {num2} = {res}")
        return(res)

def add_history(num1, num2, op, res):
    history.append(f"{num1} {op} {num2} = {res}")

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
        for ele in history:
            print(ele)

    elif user_choice not in operations:
        print("Invalid choice. Try again.")
        continue


    else:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))

        result = operations[user_choice](num1, num2)
        print(result)


        

