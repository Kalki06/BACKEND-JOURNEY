# Day 4 Progress Report

## Time Available

**3 Hours**

------------------------------------------------------------------------

# Session 1: Loop Exercises

## 1. Print Numbers from 1 to 20

### Your Solution

``` python
for i in range(1, 21):
    print(i)
```

**Review:** ✅ Correct.

**Improvement:** `print(i)` is enough because `print()` automatically
adds a newline.

------------------------------------------------------------------------

## 2. Print All Even Numbers from 1 to 50

### Method 1

``` python
for i in range(0, 51, 2):
    print(i)
```

### Method 2

``` python
for i in range(0, 51):
    if i % 2 == 0:
        print(i)
```

**Review:** ✅ Both are correct.

**Thinking Question:** Which method performs fewer operations?

------------------------------------------------------------------------

## 3. Find the Sum of Numbers from 1 to 100

``` python
total = 0

for x in range(101):
    total += x

print(total)
```

**Review:** ✅ Correct.

------------------------------------------------------------------------

## 4. Multiplication Table

``` python
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")
```

**Review:** ✅ Perfect.

------------------------------------------------------------------------

# Session 2: Logic Building

## Problem 1: Even or Odd

### Pseudocode

1.  Take input.
2.  If `num % 2 == 0`
3.  Print **Even**
4.  Else print **Odd**

**Review:** ✅ Correct.

------------------------------------------------------------------------

## Problem 2: Largest of Three Numbers

### Pseudocode

1.  Take three numbers.
2.  Compare them.
3.  Print the largest.

**Review:** ✅ Correct.

### Edge Case

Consider:

    10 10 5

or

    5 5 5

How would your algorithm handle equality?

------------------------------------------------------------------------

## Problem 3: Count Vowels

### Your Pseudocode

1.  Take a string.
2.  Initialize `count = 0`.
3.  Loop through each character.
4.  Check whether it is a vowel.
5.  Increase count.
6.  Print count.

### Common Beginner Mistake

Avoid writing:

``` python
if ch == 'a' or 'i' or 'o' or 'u' or 'e':
```

Instead, think carefully about why non-empty strings evaluate as truthy.

------------------------------------------------------------------------

# Session 3: Calculator Project

### Current Version

Features:

-   Addition
-   Subtraction
-   Multiplication
-   Division
-   Division-by-zero handling
-   Invalid choice handling

**Review:** ⭐ 9/10

### Suggested Improvements

-   Replace operator input with a numbered menu.
-   Improve error message:

Instead of:

    No Number can be divide by 0.

Use:

    Division by zero is not allowed.

------------------------------------------------------------------------

# Mini Challenge

## Goal

Convert the calculator into a menu-driven application.

### Questions

#### 1. Which loop should be used?

**Answer:** `while`

------------------------------------------------------------------------

#### 2. How should the program stop?

``` python
if choice == 5:
    break
```

------------------------------------------------------------------------

#### 3. Where should `input()` go?

**Answer:** Inside the loop.

Reason: The user should be able to choose a new operation every time.

------------------------------------------------------------------------

# Program Flow

``` text
Start
    ↓
while True
    ↓
Show Menu
    ↓
Take Choice
    ↓
If choice == 5
    Break
    ↓
Take Numbers
    ↓
Perform Operation
    ↓
Repeat
```

------------------------------------------------------------------------

# Design Discussion

## Option A

Ask for numbers first, then menu.

**Works**, but asks for unnecessary input if the user wants to exit.

------------------------------------------------------------------------

## Option B (Preferred)

1.  Show menu
2.  Take choice
3.  Exit immediately if choice is 5
4.  Otherwise ask for numbers
5.  Perform operation

**Reason:** Better user experience.

------------------------------------------------------------------------

# Invalid Choice Handling

If the user enters:

    9

The program should:

    Invalid choice! Please try again.

Then return to the menu instead of exiting.

This is an example of **input validation**.

------------------------------------------------------------------------

# Day 4 Summary

## Completed

-   ✅ Loops
-   ✅ Logic-building pseudocode
-   ✅ Calculator Version 1
-   ✅ Understood `while`
-   ✅ Understood `break`
-   ✅ Discussed user experience
-   ✅ Learned input validation

------------------------------------------------------------------------

# Overall Feedback

  Category           Rating
  ------------------ ------------
  Loops              ⭐⭐⭐⭐⭐
  Logic Building     ⭐⭐⭐⭐☆
  Calculator         ⭐⭐⭐⭐⭐
  Code Readability   ⭐⭐⭐⭐☆

**Overall Score: 9.2 / 10**

------------------------------------------------------------------------

# Next Step (Day 5)

We'll learn **Functions** and refactor the calculator so that each
operation becomes its own function, making the code cleaner, reusable,
and easier to maintain.
