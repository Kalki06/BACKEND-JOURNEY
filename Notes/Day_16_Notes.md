# Day 16 Notes -- Inheritance, `super()`, Method Overriding & Design

## Progress Summary

Today you learned:

-   Inheritance
-   `super()`
-   Method overriding
-   Basic polymorphism
-   Designing an Undo feature
-   Thinking about class responsibilities
-   Array problem-solving strategies

------------------------------------------------------------------------

# Inheritance

Inheritance allows one class to reuse code from another class.

``` python
class Animal:
    pass

class Dog(Animal):
    pass
```

`Dog` automatically gets the behavior of `Animal`.

### Benefits

-   Reuse existing code
-   Reduce duplication
-   Make programs easier to maintain

------------------------------------------------------------------------

# Parent and Child Classes

The original class is the **parent (base) class**.

The new class is the **child (derived) class**.

``` python
class Animal:
    ...

class Cat(Animal):
    ...
```

`Cat` inherits from `Animal`.

------------------------------------------------------------------------

# Using `super()`

Use `super()` to call methods from the parent class.

``` python
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
```

### Why use `super()`?

-   Reuses parent initialization
-   Avoids duplicate code
-   Keeps parent and child synchronized

------------------------------------------------------------------------

# Method Overriding

A child class can replace a parent method with its own implementation.

``` python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")
```

This is called **method overriding**.

------------------------------------------------------------------------

# Avoid Code Duplication

Instead of rewriting a parent method completely:

``` python
def print_info(self):
    super().print_info()
    print(f"Breed = {self.breed}")
```

Reuse the parent method whenever possible.

------------------------------------------------------------------------

# Calculator Project Improvements

## Undo Feature

The `History` class owns the undo functionality because undo is based on
the stored history.

``` text
History
 ├── save()
 ├── show()
 ├── clear()
 └── undo()
```

### Undo Logic

-   Remove the latest history entry.
-   If history becomes empty, `last_result` becomes `None`.
-   Otherwise, restore the previous result.

------------------------------------------------------------------------

# Class Responsibilities

Current design:

-   **Calculator** → performs calculations, stores memory and last
    result.
-   **History** → stores calculations and handles undo.
-   **Menu** → displays menu options.
-   **main.py** → coordinates the program.

Keeping responsibilities separate makes the code easier to extend.

------------------------------------------------------------------------

# Encapsulation Reminder

Instead of accessing attributes directly:

``` python
cal.memory
```

Prefer methods:

``` python
cal.memory_recall()
```

This hides implementation details from other parts of the program.

------------------------------------------------------------------------

# Python Naming Convention

Prefer snake_case:

``` python
print_info()
show_balance()
memory_store()
```

Avoid camelCase:

``` python
printInfo()
showBalance()
```

------------------------------------------------------------------------

# DSA Notes

## Problem 1 -- Move All Zeros to the End

Idea:

-   Use two pointers.
-   Keep track of where the next non-zero element should go.
-   Preserve the order of non-zero elements.

Think about edge cases such as:

``` text
[0, 0, 1]
[1, 0, 3, 0, 12]
```

------------------------------------------------------------------------

## Problem 2 -- Remove Duplicates from a Sorted Array

Since the array is sorted:

-   Compare adjacent elements.
-   Avoid unnecessary `pop()` operations because they shift elements.
-   Think about overwriting duplicates instead of deleting them
    immediately.

------------------------------------------------------------------------

# Code Review Feedback

## Good

-   Correct use of inheritance.
-   Correct use of `super()`.
-   Correct method overriding.
-   Good separation of responsibilities.
-   Undo feature updates `last_result`.
-   Continued using dictionary dispatch.

## Improvements

-   Reuse parent methods with `super()` instead of duplicating code.
-   Prefer encapsulation over direct attribute access.
-   Follow snake_case naming consistently.
-   Trace DSA algorithms on paper before coding to catch edge cases.

------------------------------------------------------------------------

# Key Takeaways

-   Inheritance helps reuse code.
-   `super()` calls the parent implementation.
-   Method overriding customizes inherited behavior.
-   Avoid duplicating logic already present in the parent class.
-   Design classes around clear responsibilities.
-   Think through algorithms before writing code.

------------------------------------------------------------------------

# Reflection Questions

1.  What problem does inheritance solve?
2.  When should you use inheritance?
3.  What does `super()` actually do?
4.  What is method overriding?
5.  Why should each class have a single responsibility?

------------------------------------------------------------------------

# Preparation for Day 17

Next focus:

-   Composition vs Inheritance
-   Better encapsulation
-   Refactoring `main.py`
-   More Array DSA problems
-   Improving calculator architecture
