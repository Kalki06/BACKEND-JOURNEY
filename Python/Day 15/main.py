class BankAccount :
    bank_name = "ABC Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Current Balance: ₹{self.balance}")
        else:
            print("Amount Should be greater than 0")

    def withdraw(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance -= amount
            print(f"₹{amount} withdrawal successfully.")
            print(f"Current Balance: ₹{self.balance}")
        else:
            print("Amount Should be greater than 0")

    def showBalance(self):
        print(f"Name = {self.owner}")
        print(f"Your Account Balance is : {self.balance}\n")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_valid_amount(amount):
        if amount > 0:
            return True
        return False

Acc1 = BankAccount("Alice", 5000)
print(Acc1.bank_name)
Acc1.change_bank_name("XYZ Bank")
print(Acc1.bank_name)

Acc1.deposit(5000)
Acc1.deposit(0)

Acc1.withdraw(0)
Acc1.withdraw(1000)

Acc1.showBalance()

"""
DSA
Problem 1
Find the largest element in an array.

create a varable name largest_ele and intialized it with list[0] then run a for loop over the list from 1->len(list) inside loop if element > largest_ele -> largest_ele = element
outside loop return the largest_ele


Problem 2
Find the second largest element in an array.

create two variables one largest_element = list[0] and sec_large_ele = None
now run a loop over the list inside loop if element > largest_ele -> sec_large_ele = largest_ele and largest_ele = element
outside loop return the second largest element
"""