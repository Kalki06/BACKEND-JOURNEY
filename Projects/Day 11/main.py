import calculator as ca
import menu as m
import history as h
operations = {
    1:ca.add,
    2:ca.sub,
    3:ca.multiply,
    4:ca.div
}

symbols = {
    1:'+',
    2:'-',
    3:'*',
    4:'/'
}

while(True):
    print("\nCALCULATOR\n")

    m.menu()

    try:
        user_choice = int(input("Enter your choice in numbers from the menu : "))
        print("\n")

        if(user_choice == 0):
            h.clear_history()
            break

        elif(user_choice == 5):
            try:
                h.show_history()
            except FileNotFoundError:
                print("File not found !!!\n")
        
        elif user_choice not in operations:
            print("Invalid Choice !!\n Try Again \n")
        
        else:
            try:
                num1 = int(input("Enter the First number : "))
                num2 = int(input("Enter the Second number : "))

                op = symbols[user_choice]

                result = operations[user_choice](num1, num2)
                print("\n")
                print(f"{result}\n")

                if not isinstance(result, str):
                    try:
                        with open ("history.txt", "a") as file:
                            file.write(f"{num1} {op} {num2} = {result}\n")
                    except FileNotFoundError:                   
                        print("File not found !!!!")
            except ValueError:
                print("Enter only valid integers only \n")
            
    except ValueError:
        print("Please Enter Valid Values Only.\n")