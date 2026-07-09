# Day 11 Notes -- Modules, Project Organization & DSA

## Progress Summary

Today you learned:

-   Python Modules
-   Importing modules
-   Organizing a project into multiple files
-   Separating responsibilities (Separation of Concerns)
-   Using dictionaries to map menu choices to functions
-   Basic project architecture
-   DSA planning with pseudocode

------------------------------------------------------------------------

# Python Modules

A module is a Python file (`.py`) that contains related functions,
classes, or variables.

Benefits:

-   Reuse code
-   Keep projects organized
-   Make programs easier to maintain

Example imports:

``` python
import calculator
import calculator as ca
from calculator import add
```

------------------------------------------------------------------------

# Project Structure

``` text
calculator_project/
│
├── calculator.py
├── history.py
├── menu.py
└── main.py
```

## Responsibilities

### calculator.py

Contains only calculation functions.

-   add()
-   sub()
-   multiply()
-   div()

No user input. No file handling. No menu printing.

------------------------------------------------------------------------

### menu.py

Responsible only for displaying the menu.

Example:

-   display menu
-   (optionally) get user choice

------------------------------------------------------------------------

### history.py

Responsible only for history management.

Functions:

-   show_history()
-   clear_history()
-   (future) save_history()

It should not perform calculations.

------------------------------------------------------------------------

### main.py

Acts as the controller of the application.

Responsibilities:

-   Show the menu
-   Read user input
-   Call calculator functions
-   Save/show/clear history
-   Control program flow

------------------------------------------------------------------------

# Function Dictionary

Instead of:

``` python
if choice == 1:
    ...
elif choice == 2:
    ...
```

Use:

``` python
operations = {
    1: ca.add,
    2: ca.sub,
    3: ca.multiply,
    4: ca.div
}
```

Benefits:

-   Cleaner code
-   Easier to add new operations
-   Less repetitive

------------------------------------------------------------------------

# Symbols Dictionary

``` python
symbols = {
    1: "+",
    2: "-",
    3: "*",
    4: "/"
}
```

Used for writing readable history entries.

------------------------------------------------------------------------

# Checking Data Types

Recommended:

``` python
if not isinstance(result, str):
    ...
```

`isinstance()` is preferred over `type()` for type checking.

------------------------------------------------------------------------

# Clearing a File

Opening a file in write mode (`"w"`) clears its contents.

Example:

``` python
with open("history.txt", "w"):
    pass
```

Writing an empty string also works:

``` python
with open("history.txt", "w") as file:
    file.write("")
```

------------------------------------------------------------------------

# Code Review Improvements

-   Prefer `while True:` over `while(True):`
-   Prefer `if choice == 1:` over `if(choice == 1):`
-   Keep each module focused on a single responsibility.
-   `operations` and `symbols` belong in `main.py`.
-   Avoid mixing calculations with history management.

------------------------------------------------------------------------

# DSA Practice

## Problem 1 -- Reverse a List

Idea:

-   Start from the last index.
-   Traverse to the first.
-   Build a new reversed list.

Time Complexity:

-   O(n)

Remember: For a list of length `n`, the last valid index is `n - 1`.

------------------------------------------------------------------------

## Problem 2 -- Smallest Element

Algorithm:

1.  Initialize:

``` python
smallest = numbers[0]
```

2.  Traverse the list.

3.  If current element is smaller:

``` python
smallest = element
```

Time Complexity:

-   O(n)

------------------------------------------------------------------------

# Key Lessons

-   Break large programs into smaller modules.
-   Give each module one clear responsibility.
-   `main.py` coordinates the application.
-   Dictionaries can store functions.
-   Think about edge cases before writing code.
-   Read DSA questions carefully before solving them.

------------------------------------------------------------------------

# Preparation for Day 12

Next Topic:

-   Object-Oriented Programming (OOP)
-   Classes
-   Objects
-   Attributes
-   Methods
-   When to use classes instead of functions
