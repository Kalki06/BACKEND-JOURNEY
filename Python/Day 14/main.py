class LibraryBook:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self. available = available

    def borrow(self):
        if self.available is True:
            print("You can borrow the book\n")
            self.available = False
        else:
            print("Already Borrowed by someone else. \n")

    def return_book(self):
        if self.available is False:
            self.available = True
        else:
            print("Already available : ")

    def display(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        if self.available is True:
            print("Status : Available")
        print("Status : Not Available")

book1 = LibraryBook("Harry Potter", "J.K Roling", False)
book1.borrow()
book1.display()
book1.return_book()


"""
DSA
Problem 1
Move all zeros to the end.

Problem 2
Find the frequency of every element.

we will create a empty dictionary = {} then run a for loop over the list if element == dictionary[key] -> value++ else dictionary[element] : 1

return the dictionary
"""