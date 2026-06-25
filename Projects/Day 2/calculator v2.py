num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
choice = input("Which operation (+, -, *, /) do you want to perform : ")

if(choice == "+"):
   print(f"The sum of {num1} and {num2} is {num1 + num2}.")
elif(choice == "-"):
   print(f"The difference of {num1} and {num2} is {num1 - num2}.")
elif(choice == "*"):
    print(f"The product of {num1} and {num2} is {num1 * num2}.")
elif(choice == "/"):
    print(f"The quotient of {num1} and {num2} is {num1 / num2}.")
else:
    print("Invalid choice !!! ")
