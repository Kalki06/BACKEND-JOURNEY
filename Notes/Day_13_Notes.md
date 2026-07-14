# Day 13 Notes -- OOP Design and Class Attributes

## Progress Summary

Today you learned:

-   Instance attributes vs class attributes
-   Using multiple classes in one project
-   Separating responsibilities using OOP
-   Designing a project before writing code
-   Creating multiple objects
-   Writing DSA pseudocode before coding

------------------------------------------------------------------------

# Project Architecture

Your calculator project is now organized into multiple classes.

``` text
             main.py
          /     |      \
         /      |       \
        ▼       ▼        ▼
 Calculator   History   Menu
```

Each class has one responsibility.

-   **Calculator** → Performs calculations.
-   **History** → Stores, displays, and clears history.
-   **Menu** → Displays the menu.
-   **main.py** → Coordinates everything.

This follows the **Single Responsibility Principle (SRP)**.

------------------------------------------------------------------------

# Classes Used

## Calculator

Responsibility:

-   add()
-   subtract()
-   multiply()
-   divide()

The calculator currently has no object state, so using a class is mainly
for OOP practice.

In larger applications, a calculator might store:

-   last_result
-   memory
-   mode (Degrees/Radians)

------------------------------------------------------------------------

## History

Your History class stores data using an instance attribute.

``` python
self.history = []
```

Methods:

-   save()
-   show()
-   clear()

Currently, history is stored only in memory.

A future improvement is saving and loading history from `history.txt`.

------------------------------------------------------------------------

## Menu

The Menu class has one responsibility:

``` python
display()
```

It only prints the calculator menu.

------------------------------------------------------------------------

# Instance Attributes vs Class Attributes

## Instance Attribute

Belongs to each object individually.

Example:

``` python
self.name
self.age
self.balance
```

Each object stores its own values.

------------------------------------------------------------------------

## Class Attribute

Shared by every object.

Example:

``` python
college = "GGSIPU"
```

All Student objects use the same college unless an individual object
overrides it.

------------------------------------------------------------------------

# Student Class

You created:

-   class attribute:
    -   college
-   instance attributes:
    -   name
    -   age
    -   course

This demonstrates the difference between shared and individual data.

------------------------------------------------------------------------

# BankAccount Class

Attributes:

-   owner
-   balance

Methods:

-   deposit()
-   withdraw()
-   show_balance()

## Suggested Improvement

Before withdrawing money, check whether:

-   balance \>= withdrawal amount

to avoid negative balances.

Also follow PEP 8 naming:

``` python
show_balance()
```

instead of:

``` python
showBalance()
```

------------------------------------------------------------------------

# Object Creation

Objects are created from classes.

Example:

``` python
calculator = Calculator()
history = History()
menu = Menu()
```

Each object has its own data and methods.

------------------------------------------------------------------------

# Exception Handling

Good practice:

``` python
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
except Exception:
    ...
```

Handle specific exceptions before general ones.

------------------------------------------------------------------------

# Design Thinking

Before writing code, ask:

-   What objects exist?
-   What is each object's responsibility?
-   Does this object need to store data?
-   Should this be a class or just functions?

Not every program needs classes.

Choose classes when an object has meaningful state or when grouping
related behavior improves organization.

------------------------------------------------------------------------

# DSA Notes

## Problem 1

Find the second largest element.

Approach:

1.  Maintain two variables:
    -   largest
    -   second_largest
2.  Traverse the list.
3.  Update both variables when a larger element is found.

Think about duplicate values such as:

``` python
[10, 10, 5]
```

------------------------------------------------------------------------

## Problem 2

Reverse a list without slicing.

Approach:

1.  Initialize:
    -   i = 0
    -   j = len(list) - 1
2.  Swap list\[i\] and list\[j\].
3.  Increment i and decrement j.
4.  Continue while i \< j.

Time Complexity:

-   O(n)

Space Complexity:

-   O(1)

------------------------------------------------------------------------

# Code Review Improvements

-   Prefer snake_case for method names.
-   Add a balance check before withdrawal.
-   Consider using a dictionary of object methods instead of a long
    if-elif chain:

``` python
operations = {
    1: calculator.add,
    2: calculator.subtract,
    3: calculator.multiply,
    4: calculator.divide,
}
```

This keeps the code cleaner and easier to extend.

------------------------------------------------------------------------

# Key Lessons

-   A class is a blueprint.
-   An object is an instance of a class.
-   `self` refers to the current object.
-   Instance attributes belong to one object.
-   Class attributes are shared.
-   Good software separates responsibilities.
-   Think about design before implementation.

------------------------------------------------------------------------

# Reflection Questions

1.  When should you use a class instead of functions?
2.  Why is `owner` an instance attribute in BankAccount?
3.  Why is `college` a class attribute in Student?
4.  How does separating responsibilities make code easier to maintain?

------------------------------------------------------------------------

# Preparation for Day 14

Next topics:

-   Method dispatch using object methods
-   Encapsulation basics
-   Improving the calculator with cleaner OOP design
-   More DSA practice
