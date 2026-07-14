from calculator import Calculator
from history import History
from menu import Menu

calculator = Calculator()
history = History()
menu = Menu()

symbols = {
    1: "+",
    2: "-",
    3: "*",
    4: "/"
}

while True:

    menu.display()

    try:

        choice = int(input("\nEnter your choice: "))

        if choice == 7:
            print("Goodbye!")
            break

        elif choice == 5:
            history.show()
            continue

        elif choice == 6:
            history.clear()
            continue

        elif choice not in [1, 2, 3, 4]:
            print("Invalid choice.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = calculator.add(num1, num2)

        elif choice == 2:
            result = calculator.subtract(num1, num2)

        elif choice == 3:
            result = calculator.multiply(num1, num2)

        elif choice == 4:
            result = calculator.divide(num1, num2)

        print(f"\nResult = {result}")

        expression = f"{num1} {symbols[choice]} {num2} = {result}"

        history.save(expression)

    except ValueError:
        print("\nPlease enter numbers only.")

    except ZeroDivisionError as e:
        print(f"\nError: {e}")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")