from calculator import Calculator
from history import History
from menu import Menu

cal = Calculator()
his = History()
menu = Menu()

operations = {
    1 : cal.add,
    2 : cal.sub,
    3 : cal.multiply,
    4 : cal.divide
}

symbols = {
    1 : "+",
    2 : "-",
    3 : "*",
    4 : "/"
}

while True:

    menu.display()

    try:
        choice = int(input("\nEnter your choice : "))

        if choice == 11:
            print("Goodbye !")
            break

        elif choice == 10:
            cal.memory_store()
            continue

        elif choice == 7:
            print(f"Last result = {cal.last_result}")
            continue

        elif choice == 8:
            print(f"Memory = {cal.memory}")
            continue

        elif choice == 9:
            cal.memory_clear()
            print("-----Memory cleared-----")
            continue

        elif choice == 5:
            his.show()
            continue

        elif choice == 6:
            his.clear()
            continue

        elif choice not in operations:
            print("Invalid choice.")
            continue

        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        result = operations[choice](num1, num2)

        print(f"\n Result = {result}")

        if not isinstance(result, str):
            expression = f"{num1} {symbols[choice]} {num2} = {result}"

            his.save(expression)

    except ValueError:
        print("\nPlease enter numbers only.")
    except ZeroDivisionError as e:
        print(f"\n Error : {e}")
    except Exception as e:
        print(f"\nUnexcepted Error: {e}")
