marks = int(input("Enter your marks : "))

if(marks >= 40):
    print("Pass")
else:
    print("Fail")


if(marks >= 90):
    print("Grade A")
elif(marks >= 75):
    print("Grade B")
elif(marks >= 60):
    print("Grade C")
elif(marks >= 40):
    print("Grade D")
elif(marks < 40 ):
    print("Fail")
else:
    print("Invalid input")