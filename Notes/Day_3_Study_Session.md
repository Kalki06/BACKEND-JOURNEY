# Day 3 Study Session

## Day 2 Progress Summary

### Coding Practice

-   Took user input using `input()`
-   Used `int()` and `float()` conversions
-   Performed arithmetic operations
-   Built a rectangle area calculator

### Logic Building

Learned: - `str` - `int` - Datatype mismatch - Type conversion using
`int()`

### Mini Project

Built a basic calculator supporting: - Addition - Subtraction -
Multiplication - Division - Invalid choice handling

### Challenge Answer

-   `x` → `str`
-   `y` → `int`

------------------------------------------------------------------------

# Mentor Feedback

-   Coding Practice: 8.5/10
-   Good use of input, arithmetic operators, and f-strings.
-   Calculator project worked correctly.
-   Reflection question: What happens when dividing by zero?

------------------------------------------------------------------------

# Day 3 Study Plan

## Learning

Comparison operators: - `==` - `!=` - `>` - `<` - `>=` - `<=`

Goal: Understand that comparison expressions return Boolean values
(`True` / `False`).

## Coding Practice

### Exercise 1

Compare two numbers: - Greater - Smaller - Equal

### Exercise 2

Voting eligibility: - Age ≥ 18 → Eligible - Otherwise → Not eligible

### Exercise 3

Determine whether a number is: - Positive - Negative - Zero

------------------------------------------------------------------------

## Logic Building Questions

Predicted outputs:

-   Q1: True
-   Q2: False
-   Q3: False
-   Q4: True
-   Q5: True

------------------------------------------------------------------------

## Mini Project

Student Pass Checker

Rules: - Marks ≥ 40 → Pass - Otherwise → Fail

Grades: - 90+ → Grade A - 75--89 → Grade B - 60--74 → Grade C - 40--59 →
Grade D - Below 40 → Fail

------------------------------------------------------------------------

# Your Day 3 Solutions

## Coding Practice

### Number Comparison

``` python
num1 = int(input("Enter first number : "))
num2 = int(input("Enter Second number : "))

print(f"Greater : {num1 > num2}")
print(f"Smaller : {num1 < num2}")
print(f"Equal : {num1 == num2}")
```

### Voting Eligibility

``` python
age = int(input("Enter your age : "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

### Positive / Negative / Zero

``` python
num = int(input("Enter a number : "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

------------------------------------------------------------------------

## Logic Building Answers

-   Q1 → True
-   Q2 → False
-   Q3 → False
-   Q4 → True
-   Q5 → True

------------------------------------------------------------------------

## Mini Project

``` python
marks = int(input("Enter your marks : "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
elif marks < 40:
    print("Fail")
else:
    print("Invalid input")
```

------------------------------------------------------------------------

## Challenge Answers

``` text
1. True
2. False
3. True
4. False
```

------------------------------------------------------------------------

# Mentor Review

## Coding Practice

✅ 10/10

## Logic Building

✅ 5/5 correct

## Mini Project

Works correctly.

Suggested improvement: Combine the pass/fail and grading logic into a
single `if-elif-else` chain so only one final message is printed.

Example goal: Instead of:

    Pass
    Grade A

Print only:

    Grade A

------------------------------------------------------------------------

# Overall Assessment

  Area              Score
  --------------- -------
  Coding            10/10
  Logic             10/10
  Syntax            10/10
  Effort            10/10
  Understanding      9/10

Overall: **9.8/10**

------------------------------------------------------------------------

# Progress Summary

## Day 1

-   Variables
-   Input
-   Output

## Day 2

-   Arithmetic operators
-   Type conversion
-   Calculator

## Day 3

-   Comparison operators
-   Boolean values
-   `if`, `elif`, `else`
-   Decision making

------------------------------------------------------------------------

# Preview of Day 4

Topics: - `and` - `or` - `not`

Optional challenge:

Admission Checker

Input: - Age - Percentage

Rules: - Age ≥ 18 - Percentage ≥ 60

If both are true:

    Eligible for admission

Otherwise:

    Not eligible
