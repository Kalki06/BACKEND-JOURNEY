class Calculator:

    def __init__(self):
        self.last_result = None
        self.memory = None

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 /  num2

    def memory_store(self):
        if self.last_result is None:
            print("No result to store.")
            return
        self.memory = self.last_result
        print("Memory stored successfully.")

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = None

    def get_last_result(self):
        return self.last_result

    def set_last_result(self, result):
        self.last_result = result

    def calculate(self, operation, num1, num2):
        operations = {
            "+": self.add,
            "-": self.sub,
            "*": self.multiply,
            "/": self.divide
        }
        if operation not in operations:
            raise ValueError("Invalid Operation")
        result =  operations[operation](num1, num2)
        self.set_last_result(result)
        return result
