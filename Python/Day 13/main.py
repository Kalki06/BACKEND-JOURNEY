# class Student:
#     college = "GGSIPU"

#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def introduce(self):
#         print(f"Hi, I'm {self.name}, {self.age} years old.")
#         print(f"I am pursuing {self.course} at {self.college}.")

# s1 = Student("Manjeet", 20, "Bca")
# s2 = Student("Rohan", 21, "Bba")
# s3 = Student("Inderjeet", 22, "B.com")

# s1.introduce()
# s2.introduce()
# s3.introduce()

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance



    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than 0.")
            return

        self.balance -= amount
        print(f"₹{amount} withdrawal successfully.")
        print(f"Current Balance: ₹{self.balance}")

    def showBalance(self):
        print(f"Name = {self.owner}")
        print(f"Your Account Balance is : {self.balance}\n")



t1 = BankAccount("Manjeet", 500000)
amount = int(input("Enter the amount : "))
t1.deposit(amount)


t2 = BankAccount("Alice", 3000)
amount = int(input("Enter the amount : "))
t2.withdraw(amount)

t2.showBalance()

"""
Problem 1
Find the second largest element in a list.

input
elements for the list

output
second_largest_ele

approach
forst we will create two variable called sec_largest_ele and initialized it with None and another variable called largest_ele = list[o]
run loop over the list if element > largest_ele then sec_largest_element = largest element, largest_element = element
print(sec_largest_ele)


Problem 2
Reverse a list without using slicing ([::-1]).

input
elements for the list

output reverseed list

approach
create two varble i  = 0, j = len(list) - 1
then ran a while loop until i < j
swap(list[i], list[j])
i++
j--
"""