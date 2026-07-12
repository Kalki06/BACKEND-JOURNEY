# Day 12 Notes -- Introduction to Object-Oriented Programming (OOP)

## Progress Summary

Today you learned:

-   Introduction to Object-Oriented Programming (OOP)
-   Classes and Objects
-   Constructors (`__init__`)
-   Instance Attributes
-   Methods
-   Improving exception handling in your calculator
-   Planning DSA solutions before coding

------------------------------------------------------------------------

# What is OOP?

Object-Oriented Programming (OOP) is a programming style where we
organize code using **classes** and **objects**.

It helps us group related data and behavior together.

------------------------------------------------------------------------

# Class vs Object

## Class

A class is a blueprint.

Example:

``` python
class Student:
    pass
```

A class describes what an object should look like.

## Object

An object is an actual instance of a class.

Example:

``` python
student1 = Student()
```

You can create many objects from the same class.

------------------------------------------------------------------------

# Constructor (`__init__`)

The constructor runs automatically whenever an object is created.

Example:

``` python
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
```

Its purpose is to initialize the object's data.

------------------------------------------------------------------------

# Instance Attributes

Instance attributes belong to individual objects.

Example:

``` python
self.name
self.age
self.course
```

Each object stores its own values.

Example:

``` python
s1 = Student("Alice", 20, "BCA")
s2 = Student("Bob", 22, "B.Tech")
```

Changing `s1.name` does not affect `s2.name`.

------------------------------------------------------------------------

# Methods

Methods are functions inside a class.

Example:

``` python
def introduce(self):
    print(f"My name is {self.name}")
```

Methods usually operate on the object's data.

------------------------------------------------------------------------

# The `self` Keyword

`self` refers to the current object.

When calling:

``` python
s1.introduce()
```

Python automatically passes `s1` as the `self` parameter.

------------------------------------------------------------------------

# Calculator Class

You created a `Calculator` class containing:

-   add()
-   sub()
-   multiply()
-   div()

These methods work correctly.

However, notice that the calculator stores **no data**.

This raises an important design question:

> Should every group of functions become a class?

Not necessarily. If there is no object state, regular functions may be
simpler.

------------------------------------------------------------------------

# Student Class

Your `Student` class demonstrates proper OOP usage.

It includes:

-   Constructor
-   Attributes
-   Method (`introduce()`)

Example:

``` python
s1 = Student("Manjeet", 20, "BCA")
s1.introduce()
```

------------------------------------------------------------------------

# Improving the Calculator Project

Yesterday's issue:

``` python
try:
    num1 = int(input(...))
    num2 = int(input(...))
except ValueError:
    ...
```

The program continued even after invalid input.

Today's improvement:

-   Input
-   Calculation
-   Saving history

are all inside the same `try` block.

Now invalid input prevents the calculation from running.

------------------------------------------------------------------------

# Code Review Improvements

Prefer:

``` python
while True:
```

instead of

``` python
while(True):
```

Prefer:

``` python
if choice == 1:
```

instead of

``` python
if(choice == 1):
```

Use PascalCase for class names:

``` python
class Calculator:
class Student:
```

instead of

``` python
class calculator:
class student:
```

------------------------------------------------------------------------

# File Handling Reminder

Think about append mode:

``` python
with open("history.txt", "a"):
```

Question:

What happens if the file does not exist?

(Hint: Test it yourself.)

------------------------------------------------------------------------

# DSA Notes

## Problem 1 -- Largest Element

Algorithm:

1.  Initialize:

``` python
largest = numbers[0]
```

2.  Traverse the list.

3.  If current element is larger:

``` python
largest = element
```

Time Complexity:

**O(n)**

------------------------------------------------------------------------

## Problem 2 -- Count Target Occurrences

Algorithm:

1.  Initialize:

``` python
count = 0
```

2.  Traverse the list.

3.  If current element equals the target:

``` python
count += 1
```

Time Complexity:

**O(n)**

------------------------------------------------------------------------

# Key Lessons

-   Classes are blueprints.
-   Objects are instances of classes.
-   `__init__()` initializes object data.
-   `self` refers to the current object.
-   Not every problem requires a class.
-   Group related responsibilities together.
-   Fix bugs by restructuring code, not by adding more conditions.
-   Plan DSA solutions before writing code.

------------------------------------------------------------------------

# Questions to Think About

1.  Why doesn't creating two `Student` objects overwrite each other's
    data?
2.  Should a `Calculator` always be a class?
3.  What does opening a file in `"a"` mode do if the file doesn't exist?

------------------------------------------------------------------------

# Preparation for Day 13

Next topics:

-   Instance vs Class Attributes
-   Understanding `self` deeply
-   Multiple Objects
-   Small OOP Mini Project
