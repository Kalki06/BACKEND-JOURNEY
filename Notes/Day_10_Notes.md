# Day 10 Notes -- Exception Handling

## Progress Summary

Today you learned:

-   Exception Handling in Python
-   `try`, `except`, `finally`
-   Handling invalid user input
-   Handling missing files
-   Making the CLI Calculator more robust
-   DSA: Finding the second largest element in **O(n)**

------------------------------------------------------------------------

# Exception Handling

## Why use Exception Handling?

Programs can crash when unexpected input or errors occur.

Exception handling allows the program to recover gracefully instead of
stopping.

------------------------------------------------------------------------

## Common Exceptions

  Exception             When it occurs
  --------------------- -------------------------------------------------
  `ValueError`          Invalid type conversion (e.g. `"abc"` to `int`)
  `ZeroDivisionError`   Division by zero
  `FileNotFoundError`   Opening a file that does not exist

------------------------------------------------------------------------

## Basic Syntax

``` python
try:
    # risky code
except ValueError:
    print("Invalid input")
finally:
    print("Program Finished")
```

### `finally`

Code inside `finally` always runs, whether an exception occurs or not.

------------------------------------------------------------------------

# Calculator V6 Improvements

Features added:

-   Protected menu input using `try` / `except`
-   Protected numeric input
-   Handled missing `history.txt`
-   Prevented crashes from invalid input

### Engineering Improvements to Make Later

-   Reduce deeply nested `try` blocks.
-   Avoid using `if result is not str`.
-   Handle variables that may not be created after an exception.
-   Improve edge-case handling.

------------------------------------------------------------------------

# DSA Practice

## Problem 1 -- Second Largest Element

### Naive Solution

Sort the list and return the second last element.

Time Complexity:

    O(n log n)

### Optimized Solution

Traverse the list once while maintaining:

-   `largest`
-   `second_largest`

Key idea:

-   If current element is greater than `largest`:
    -   Move `largest` into `second_largest`
    -   Update `largest`
-   Otherwise, if the element is between `largest` and `second_largest`,
    update `second_largest`.

Time Complexity:

    O(n)

### Important Lessons

-   Don't initialize `second_largest` to `0`.
-   `None` cannot be compared directly with integers.
-   Use:

``` python
float("-inf")
```

when you need a value smaller than every number.

Consider edge cases:

-   Empty list
-   One-element list
-   Duplicate largest values
-   All negative numbers

------------------------------------------------------------------------

## Problem 2 -- Reverse a List

Algorithm:

1.  Create an empty list.
2.  Traverse the original list from the last index to the first.
3.  Append each element.
4.  Return the new list.

Time Complexity:

    O(n)

------------------------------------------------------------------------

# Success Criteria Achieved

-   Understood `try`, `except`, and `finally`
-   Handled common runtime errors
-   Improved the calculator
-   Learned how to think about edge cases
-   Designed an O(n) algorithm for finding the second largest element

------------------------------------------------------------------------

# Preparation for Day 11

Next Topic:

-   Modules
-   Packages
-   Importing Python files
-   Organizing larger programs
