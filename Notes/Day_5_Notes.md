# Day 5 Notes -- Functions, Code Review & Engineering Thinking

## Function Basics

### Why use functions?

-   Reuse code
-   Improve readability
-   Organize programs into smaller pieces
-   Make testing and debugging easier

### Function Structure

``` python
def add(a, b):
    return a + b
```

### Parameters vs Arguments

-   **Parameters**: Variables in the function definition (`a`, `b`).
-   **Arguments**: Actual values passed when calling the function
    (`add(5, 6)`).

### `return` vs `print`

Use `return` instead of `print` when possible.

Why? - The returned value can be reused. - Functions become more
flexible.

Example:

``` python
result = add(10, 20)
print(result)
```

------------------------------------------------------------------------

# Practice Completed

-   ✅ `add()`
-   ✅ `square()`
-   ✅ `iseven()`
-   ✅ `maximum()`

### Improvement

Current:

``` python
def iseven(num):
    res = True
    if num % 2 != 0:
        res = False
    return res
```

Challenge: Can this be written in one line?

Hint:

``` python
num % 2 == 0
```

------------------------------------------------------------------------

# Calculator Version 2

## Improvements Made

-   Menu function
-   Separate functions for each operation
-   `while` loop
-   Division by zero handling
-   Invalid menu handling

## Code Review

### Good

-   Small reusable functions
-   Cleaner organization
-   Uses `return`
-   Better than one large script

### Improvements

#### 1. Don't print `menu()`

Current:

``` python
print(f"{menu()}\n")
```

Reason: `menu()` prints the menu and returns `None`.

Instead:

``` python
menu()
```

#### 2. Validate the menu choice before asking for numbers.

Better flow:

1.  Show menu
2.  User selects option
3.  Validate choice
4.  Ask for numbers
5.  Perform calculation

#### 3. Prefer descriptive names

Instead of:

``` python
multi()
```

Use:

``` python
multiply()
```

------------------------------------------------------------------------

# Logic Building Lessons

## Largest Element

Don't use:

``` python
max(list)
```

Goal: Learn the algorithm yourself.

------------------------------------------------------------------------

## Counting Positive & Negative Numbers

Think about the edge case:

What should happen with `0`?

-   Positive?
-   Negative?
-   Neither?

------------------------------------------------------------------------

## Factorial

`res` should be inside the function.

Reason: Local variables are safer and prevent accidental modification.

------------------------------------------------------------------------

# DSA Thinking Process

Before coding every problem, answer:

1.  Input
2.  Output
3.  Approach
4.  Time Complexity
5.  Space Complexity

Example:

-   Input: List of numbers
-   Output: Maximum element
-   Approach: Traverse the list while tracking the current maximum
-   Time: O(n)
-   Space: O(1)

------------------------------------------------------------------------

# Engineering Discussion: Calculator History

## Option 1 -- Store Strings

``` python
history = [
    "5 + 6 = 11",
    "8 * 3 = 24"
]
```

### Pros

-   Easy to display
-   Simple for a CLI project

### Cons

-   Hard to analyze later
-   Parsing required for statistics

------------------------------------------------------------------------

## Option 2 -- Store Structured Data

``` python
{
    "num1": 5,
    "operator": "+",
    "num2": 6,
    "result": 11
}
```

### Pros

-   Easy to query
-   Better for databases
-   Easier to extend

### Cons

-   Slightly more complex

------------------------------------------------------------------------

# Important Lesson

Storage size is **not** the main reason to choose one representation
over another.

Backend engineers usually choose the representation that makes the data
easier to work with.

------------------------------------------------------------------------

# Displaying History

Initial thought: - Parse every string.

Better approach: - If the string is already formatted correctly, simply
iterate through the list and print each item.

Lesson:

> Don't transform data unless you have a reason to.

------------------------------------------------------------------------

# Engineering Mindset

## Beginner Thinking

> "How do I write this code?"

## Intermediate Thinking

> "How should I represent this data?"

## Senior Thinking

> "What is the simplest solution that solves the problem?"

A senior engineer removes unnecessary complexity instead of adding it.

------------------------------------------------------------------------

# Progress Summary

## Day 4

-   Loops
-   Conditionals
-   First calculator

## Day 5

-   Functions
-   `return`
-   Refactored calculator
-   Better code organization
-   Started thinking about data representation and software design

------------------------------------------------------------------------

# Key Takeaways

-   Prefer `return` over `print`.
-   Break large programs into functions.
-   Use descriptive function names.
-   Validate user input early.
-   Think about edge cases.
-   Don't use built-in functions when practicing algorithms.
-   Consider how data should be represented before coding.
-   Keep solutions as simple as possible.
