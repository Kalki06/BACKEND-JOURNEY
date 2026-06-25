print(" 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division")
choice = int(input("Enter your choice : "))

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if choice == 1:
    print("Sum of two numbers is : ", num1 + num2)
elif choice == 2:
    print("Difference of two numbers is : ", num1 - num2)
elif choice == 3:
    print("Product of two numbers is : ", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Division of two numbers is : ", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")