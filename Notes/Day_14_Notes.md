# Day 14 Notes -- Dictionary Dispatch and Encapsulation

## Progress Summary

Today you learned:

-   Dictionary dispatch using object methods
-   Cleaner OOP design
-   Introduction to encapsulation
-   Designing classes with clear responsibilities
-   Planning DSA solutions before coding

------------------------------------------------------------------------

# Dictionary Dispatch

Instead of writing long `if...elif` chains:

``` python
if choice == 1:
    result = calculator.add(a, b)
elif choice == 2:
    result = calculator.sub(a, b)
```

store object methods in a dictionary:

``` python
operations = {
    1: cal.add,
    2: cal.sub,
    3: cal.multiply,
    4: cal.divide
}

result = operations[choice](num1, num2)
```

## Advantages

-   Cleaner code
-   Easier to extend
-   Removes repetitive conditions
-   Common pattern in production Python

------------------------------------------------------------------------

# Method References

A method can be stored in a variable or dictionary without calling it.

``` python
x = cal.add
```

The method executes only when parentheses are used:

``` python
x(10, 20)
```

------------------------------------------------------------------------

# Encapsulation (Introduction)

Encapsulation means controlling how an object's data is accessed.

Instead of changing object data directly:

``` python
history.history.append("2 + 2")
```

prefer using methods:

``` python
history.save("2 + 2")
history.show()
history.clear()
```

This keeps the object's internal data safe and organized.

------------------------------------------------------------------------

# Calculator Improvements

Current structure:

``` text
main.py
│
├── Calculator
├── History
└── Menu
```

Improvements made:

-   Replaced `if...elif` with dictionary dispatch.
-   Used object methods inside a dictionary.
-   Simplified input validation with:

``` python
elif choice not in operations:
```

Future improvements:

-   Save history to a file automatically.
-   Add undo functionality.
-   Store `last_result`.
-   Add memory operations.

------------------------------------------------------------------------

# LibraryBook Class

Attributes:

-   title
-   author
-   available

Methods:

-   borrow()
-   return_book()
-   display()

## Improvements

Use:

``` python
if self.available:
```

instead of:

``` python
if self.available is True:
```

Use an `else` inside `display()` so only one status is printed.

Print a confirmation message after returning a book successfully.

------------------------------------------------------------------------

# Class Attributes Review

Example:

``` python
class Dog:
    species = "Dog"
```

Every object shares the class attribute until one object overrides it.

Example:

``` python
d1.species = "Wolf"
```

Output:

``` text
Wolf
Dog
Dog
```

Reason:

-   `d1.species` creates an instance attribute.
-   `d2` still uses the class attribute.
-   `Dog.species` remains unchanged.

------------------------------------------------------------------------

# DSA Notes

## Problem 1: Move All Zeros to the End

Idea:

-   Keep one pointer at the next position for a non-zero element.
-   Traverse the array.
-   Swap each non-zero element into the correct position.
-   Zeros naturally move to the end.

Time Complexity: **O(n)**

Space Complexity: **O(1)**

------------------------------------------------------------------------

## Problem 2: Frequency of Every Element

Use a dictionary.

Algorithm:

1.  Create an empty dictionary.
2.  Traverse the list.
3.  If the element already exists, increase its count.
4.  Otherwise, store it with count `1`.

Example:

``` python
freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
```

Time Complexity: **O(n)**

Space Complexity: **O(n)**

------------------------------------------------------------------------

# Code Review Checklist

-   Prefer snake_case for method names.
-   Avoid unnecessary `is True` and `is False`.
-   Keep exception order:
    1.  Specific exceptions
    2.  General `Exception`
-   Think about which class owns each responsibility.

------------------------------------------------------------------------

# Key Takeaways

-   Methods are objects and can be stored in dictionaries.
-   Dictionary dispatch is cleaner than long `if...elif` chains.
-   Encapsulation protects object state.
-   Instance attributes belong to one object.
-   Class attributes are shared by all objects unless overridden.

------------------------------------------------------------------------

# Reflection Questions

1.  What is dictionary dispatch?
2.  Why is it useful?
3.  What is encapsulation in your own words?
4.  When should data become an instance attribute?
5.  Which class should own the "Undo Last Calculation" feature, and why?

------------------------------------------------------------------------

# Preparation for Day 15

Next topics:

-   `@classmethod`
-   `@staticmethod`
-   Private attributes (convention)
-   More OOP design patterns
-   Additional DSA practice
