class Calculator:

    def __init__(self):
        self.last_result = None
        self.memory = None

    def add(self, num1, num2):
        result = num1 + num2
        self.last_result = result
        return result

    def sub(self, num1, num2):
        result = num1 - num2
        self.last_result = result
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.last_result = result
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        result = num1 /  num2
        self.last_result = result
        return result

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
        return operations[operation](num1, num2)