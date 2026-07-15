# Day 15 Notes -- Class Methods, Static Methods & Object State

## Progress Summary

Today you learned:

-   Class variables
-   `@classmethod`
-   `@staticmethod`
-   Object state (`last_result` and `memory`)
-   Designing cleaner classes
-   Planning DSA algorithms before coding

------------------------------------------------------------------------

# Class Variable

A class variable is shared by every object of a class.

``` python
class BankAccount:
    bank_name = "ABC Bank"
```

Every account uses the same `bank_name` unless it is changed for the
whole class.

------------------------------------------------------------------------

# Instance Variables

Instance variables belong to one object.

``` python
def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
```

Each account has its own owner and balance.

------------------------------------------------------------------------

# Class Method

A class method works with the class itself instead of a specific object.

``` python
@classmethod
def change_bank_name(cls, new_name):
    cls.bank_name = new_name
```

Use a class method when you want to modify class-level data.

------------------------------------------------------------------------

# Static Method

A static method belongs logically to the class but doesn't use `self` or
`cls`.

``` python
@staticmethod
def is_valid_amount(amount):
    return amount > 0
```

Use it for helper functions related to the class.

------------------------------------------------------------------------

# Choosing Between Methods

  Method            Uses           First Parameter
  ----------------- -------------- -----------------
  Instance Method   Object data    `self`
  Class Method      Class data     `cls`
  Static Method     Helper logic   None

------------------------------------------------------------------------

# Calculator Improvements

## New Instance Attributes

``` python
self.last_result = None
self.memory = None
```

These represent the calculator's state.

-   `last_result` stores the latest calculation.
-   `memory` stores a value using memory functions.

------------------------------------------------------------------------

## Memory Functions

Methods added:

-   `memory_store()`
-   `memory_recall()`
-   `memory_clear()`

Memory belongs inside the `Calculator` class because it is part of the
calculator's state.

------------------------------------------------------------------------

# Dictionary Dispatch

Continue using:

``` python
operations = {
    1: cal.add,
    2: cal.sub,
    3: cal.multiply,
    4: cal.divide
}
```

Benefits:

-   Cleaner code
-   Easier to extend
-   Avoids long `if...elif` chains

------------------------------------------------------------------------

# Encapsulation Reminder

Instead of accessing attributes directly:

``` python
print(cal.memory)
```

Prefer using methods:

``` python
print(cal.memory_recall())
```

This hides internal implementation details and keeps classes easier to
maintain.

------------------------------------------------------------------------

# Code Review Notes

## Good

-   Correct use of class variables.
-   Correct use of `@classmethod`.
-   Correct use of `@staticmethod`.
-   Reused validation logic instead of duplicating code.
-   Calculator state stored using instance attributes.
-   Continued using dictionary dispatch.

## Improvements

### Withdraw

Prevent withdrawing more money than the available balance.

``` python
if amount > self.balance:
    print("Insufficient balance")
```

### Naming

Prefer snake_case:

``` python
show_balance()
```

instead of:

``` python
showBalance()
```

### Divide Method

Returning a string for division by zero forces callers to check:

``` python
isinstance(result, str)
```

A cleaner design is often to raise an exception and let the caller
handle it.

------------------------------------------------------------------------

# DSA Notes

## Problem 1 -- Largest Element

Algorithm:

1.  Set `largest` to the first element.
2.  Traverse the array.
3.  If the current element is larger, update `largest`.
4.  Return `largest`.

Time Complexity: **O(n)**

Space Complexity: **O(1)**

------------------------------------------------------------------------

## Problem 2 -- Second Largest Element

Basic idea:

1.  Keep two variables:
    -   `largest`
    -   `second_largest`
2.  Traverse the array.
3.  Update both values when necessary.

Important edge case:

    [10, 5, 9]

Make sure the algorithm updates `second_largest` even when an element is
smaller than `largest` but larger than the current `second_largest`.

------------------------------------------------------------------------

# Key Takeaways

-   Class variables are shared by all objects.
-   Instance variables belong to one object.
-   Use `@classmethod` for class-level changes.
-   Use `@staticmethod` for helper logic.
-   Store long-term object state as instance attributes.
-   Use methods to access internal state instead of exposing attributes
    directly.
-   Think about design before implementation.

------------------------------------------------------------------------

# Reflection Questions

1.  When should you use an instance method?
2.  When should you use a class method?
3.  When should you use a static method?
4.  Why does calculator memory belong to the `Calculator` class?
5.  Why is encapsulation useful?

------------------------------------------------------------------------

# Preparation for Day 16

Next topics:

-   Inheritance
-   `super()`
-   Method overriding
-   Polymorphism (introduction)
-   More Array DSA problems
