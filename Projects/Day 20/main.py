from calculator import Calculator
from history import History
from menu import Menu

cal = Calculator()
his = History()
menu = Menu()

symbols = {
    1 : "+",
    2 : "-",
    3 : "*",
    4 : "/",
    5 : "^",
    6 : "%"
}

while True:

    menu.display()

    try:
        choice = int(input("\nEnter your choice : "))
    except ValueError:
        print("Enter a valid number from the menu")
        continue

    if choice == 14:
        print("Goodbye !")
        break

    elif choice == 12:
        cal.memory_store()
        continue

    elif choice == 9:
        print(f"Last result = {cal.get_last_result()}")
        continue

    elif choice == 10:
        print(f"Memory = {cal.memory_recall()}")
        continue

    elif choice == 11:
        cal.memory_clear()
        print("-----Memory cleared-----")
        continue

    elif choice == 7:
        his.show()
        continue

    elif choice == 8:
        his.clear()
        continue

    elif choice == 13:
        last_result = his.undo()
        if last_result is None:
           cal.set_last_result(None)
        else:
           cal.set_last_result(last_result[1])
        continue

    elif choice not in symbols:
        print("Invalid choice.")
        continue

    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        result = cal.calculate(symbols[choice], num1,num2)

        print(f"\n Result = {result}")

        expression = f"{num1} {symbols[choice]} {num2} = {result}"

        his.save(expression, result)

    except ValueError:
        print("\nPlease enter numbers only.")
    except ZeroDivisionError as e:
        print(f"\n Error : {e}")