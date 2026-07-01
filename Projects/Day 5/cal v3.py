def menu():
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

def add(num1, num2):
    return(num1 + num2)

def sub(num1, num2):
    return(num1 - num2)

def multi(num1, num2):
    return(num1 * num2)

def div(num1, num2):
    if(num2 == 0):
        return "Division by 0 is not posible"
    else:
        return(num1 / num2)


while(True):

    print("Calculator\n")

    print(f"{menu()}\n")
    user_choice = int(input("Enter your choice in number : \n"))

    num1 = int(input("Enter the first  number : \n"))
    num2 = int(input("Enter the second number : \n"))

    if(user_choice == 1):
        res = add(num1, num2)
        print(res)
    elif(user_choice == 2):
        res = sub(num1, num2)
        print(res)
    elif(user_choice == 3):
        res = multi(num1, num2)
        print(res)
    elif(user_choice == 4):
        res = div(num1, num2)
        print(res)
    else:
        print("Please enter a valid choice !!")
    

    cont_or_not = input("Do another calculation? (y/n)\n")
    if(cont_or_not == 'n'):
        break
