class History:

    def __init__(self):
        self.history = []

    def save(self, expression, res):
        self.history.append((expression, res))

    def show(self):

        if len(self.history) == 0:
            print("\nNo history available.")
            return

        print("\n ---- History ----")

        i = 1
        for item in self.history:
            print(f"{i}. {item[0]}\n")
            i+=1

    def clear(self):
        self.history.clear()
        print("History cleared successfully.")

    def undo(self):
        if len(self.history) == 0:
            print("No history available.")
            return

        last_item = self.history.pop()

        if len(self.history) == 0:
            return None

        return self.history[-1]