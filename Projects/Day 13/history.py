class History:

    def __init__(self):
        self.history = []

    def save(self, expression):
        self.history.append(expression)

    def show(self):

        if len(self.history) == 0:
            print("\nNo history available.")
            return

        print("\n----- HISTORY -----")

        for item in self.history:
            print(item)

    def clear(self):
        self.history.clear()
        print("History cleared successfully.")