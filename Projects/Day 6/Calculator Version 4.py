history = []

def menu():
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History")

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

def add_history(num1, num2, op, res):
    history.append(f"{num1} {op} {num2} = {res}")
    return "saved"


    


while(True):

    print("Calculator\n")

    menu()
    user_choice = int(input("Enter your choice in number : \n"))

    if 1 <= user_choice <= 5:
        if(user_choice == 1):
            num1 = int(input("Enter the first  number : \n"))
            num2 = int(input("Enter the second number : \n"))
            res = add(num1, num2)
            print(res)
            mes = add_history(num1,num2, "+", res )
            print(mes)

        elif(user_choice == 2):
            num1 = int(input("Enter the first  number : \n"))
            num2 = int(input("Enter the second number : \n"))
            res = sub(num1, num2)
            print(res)
            mes = add_history(num1,num2, "-", res )
            print(mes)

        elif(user_choice == 3):
            num1 = int(input("Enter the first  number : \n"))
            num2 = int(input("Enter the second number : \n"))
            res = multi(num1, num2)
            print(res)
            mes = add_history(num1,num2, "*" ,res )
            print(mes)

        elif(user_choice == 4):
            num1 = int(input("Enter the first  number : \n"))
            num2 = int(input("Enter the second number : \n"))
            res = div(num1, num2)
            print(res)
            mes = add_history(num1,num2, "/" ,res )
            print(mes)

        else:
            for item in history:
                print(f"{item}\n")
        
        cont_or_not = input("Do another calculation? (y/n)\n")
        if(cont_or_not == 'n'):
            break

    else:
        print("Enter a Valid choice please !!! \n")
