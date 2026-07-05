# Day 8 Notes -- Sets & Calculator Refactoring

## Progress Summary

Today you completed:

-   ✅ Learned Python Sets
-   ✅ Practiced common set operations
-   ✅ Refactored Calculator V4 using the Single Responsibility
    Principle
-   ✅ Practiced DSA algorithm design
-   ✅ Improved engineering thinking

------------------------------------------------------------------------

# Python Sets

## What is a Set?

A set is an unordered collection of unique elements.

### Key Characteristics

-   No duplicate values
-   Unordered (cannot access by index)
-   Fast membership checking using `in`

## Operations Practiced

### Create a Set

``` python
fruits = {"mango", "banana", "apple", "kiwi", "grapes"}
```

### Traverse

``` python
for fruit in fruits:
    print(fruit)
```

### Membership

``` python
print(user in fruits)
```

### Union

``` python
fruits.union(fruit2)
```

### Intersection

``` python
whole_numbers.intersection(even_numbers)
```

### Remaining Practice

-   Difference (`set1.difference(set2)`)

------------------------------------------------------------------------

# Calculator Refactoring

## Improvements

-   Math functions now only perform calculations.
-   History is stored in the main program.
-   Empty history is handled.
-   Dictionary dispatch is still used.

## Engineering Lesson

Each function should have **one responsibility**.

Instead of:

-   Calculate
-   Save history

Your functions now only:

-   Calculate
-   Return the result

The main loop is responsible for storing history.

------------------------------------------------------------------------

# Suggested Improvements

1.  Replace the `match` statement for history symbols with a dictionary
    mapping:

``` text
1 -> +
2 -> -
3 -> *
4 -> /
```

2.  Decide whether division-by-zero attempts should be stored in
    history.

3.  Complete the missing `difference()` set exercise.

4.  Convert an actual **list** into a set instead of creating a set
    directly.

Example:

``` python
numbers = [1, 2, 4, 5, 5, 6, 3, 2, 1, 7]
unique_numbers = set(numbers)
```

------------------------------------------------------------------------

# DSA Thinking Practice

## Problem 1 -- Largest Element

### Input

A list of numbers.

### Output

Largest element.

### Algorithm

1.  Initialize `maximum` with the first element.
2.  Traverse the list.
3.  Compare each element with `maximum`.
4.  Update `maximum` when a larger value is found.
5.  Print or return `maximum`.

**Time Complexity:** `O(n)`

------------------------------------------------------------------------

## Problem 2 -- Count Numbers Greater Than 50

### Input

A list of numbers.

### Output

Count of elements greater than 50.

### Algorithm

1.  Initialize `count = 0`.
2.  Traverse the list.
3.  If an element is greater than 50, increment `count`.
4.  Print or return `count`.

**Time Complexity:** `O(n)`

------------------------------------------------------------------------

# Mentor Feedback

## Overall Score

**9.8 / 10**

### Strengths

-   Cleaner calculator architecture
-   Good understanding of sets
-   Correct DSA reasoning before coding
-   Better separation of responsibilities
-   Consistent daily progress

### Focus for Next Session

-   File Handling
-   Saving calculator history to a file
-   Reading data from files
-   Writing data to files
-   Continue beginner DSA practice
