class BankAccount :
    bank_name = "ABC Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):

        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid balance")

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self._balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Current Balance: ₹{self.balance}")
        else:
            print("Amount Should be greater than 0")

    def withdraw(self, amount):
        if BankAccount.is_valid_amount(amount):
            self._balance -= amount
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

Acc1.deposit(-1000)
