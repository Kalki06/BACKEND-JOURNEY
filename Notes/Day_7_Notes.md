
# Day 7 Notes – Tuples, Dictionaries & Calculator V4

## Progress Summary

Today you completed:

- ✅ Tuples
- ✅ Dictionary fundamentals
- ✅ Dictionary iteration
- ✅ Function references
- ✅ Dictionary-based calculator dispatch
- ✅ Continued DSA algorithm planning

---

# Tuples

## What is a Tuple?

A tuple is an ordered collection that is **immutable**, meaning its elements cannot be changed after creation.

Example:

```python
cities = ("Delhi", "Chandigarh", "Amritsar", "Lucknow", "Jaipur")
```

## Operations Practiced

### Accessing Elements

```python
cities[0]
cities[-1]
```

### Traversing

```python
for city in cities:
    print(city)
```

### Length

```python
len(cities)
```

### Unpacking

```python
(city1, city2, city3, city4, city5) = cities
```

## Exercise Review

Completed:

- Created a tuple
- Printed elements
- Traversed using a loop
- Used `len()`
- Unpacked tuple values

---

# Dictionaries

## What is a Dictionary?

A dictionary stores data as **key-value pairs**.

Example:

```python
student = {
    "name": "Kalki",
    "age": 21,
    "course": "BCA"
}
```

## Operations Practiced

- Accessed values
- Updated a value
- Added a new key
- Removed a key
- Iterated through keys
- Iterated through values
- Printed key-value pairs

### Review Tip

When printing only keys, you can also write:

```python
for key in student:
    print(key)
```

or

```python
for key in student.keys():
    print(key)
```

---

# DSA Thinking Practice

## Problem 1 – Smallest Element

### Input

A list of numbers.

### Output

Smallest element.

### Approach

- Initialize a variable.
- Traverse the list.
- Compare each element.
- Update the smallest value.
- Return or print it.

### Mentor Note

Instead of using `sys.maxsize`, think about starting with the **first element** of the list.

### Time Complexity

`O(n)`

---

## Problem 2 – Count Even and Odd

### Approach

- Initialize `even = 0` and `odd = 0`.
- Traverse the list.
- If `element % 2 == 0`, increment `even`.
- Otherwise increment `odd`.

### Time Complexity

`O(n)`

---

## Problem 3 – Average

### Approach

- Initialize `total = 0`.
- Sum every element.
- Compute:

```python
average = total / len(numbers)
```

### Time Complexity

`O(n)`

---

# Calculator Version 4

## Major Improvement

Instead of a long `if/elif` chain, operations are stored in a dictionary.

```python
operations = {
    1: add,
    2: sub,
    3: multiply,
    4: div
}
```

Then the selected function is executed using:

```python
result = operations[user_choice](num1, num2)
```

## New Concepts Learned

- Functions are first-class objects.
- Functions can be stored inside variables and dictionaries.
- Retrieved functions can be executed with parentheses.

---

# Loop Control

## break

Used to exit the calculator.

```python
if user_choice == 0:
    break
```

## continue

Used to skip invalid choices and show the menu again.

```python
if user_choice not in operations:
    print("Invalid choice")
    continue
```

---

# Code Review

## Strengths

- Cleaner calculator design.
- Correct use of a dictionary for dispatch.
- Good use of `break` and `continue`.
- Better function names (`multiply`).
- Improved program flow.

## Suggested Improvements

### 1. Single Responsibility

Currently each math function both performs the calculation **and** saves history.

A cleaner design is:

- Math functions → only calculate.
- Main loop → save history.

### 2. Remove Unused Function

`add_history()` is no longer used.

Delete it after moving history handling to one place.

### 3. Empty History

Before printing history:

```python
if not history:
    print("No history available.")
```

### 4. Division by Zero

Decide whether failed calculations should be stored in history.

---

# Engineering Lessons

## Functions Are Values

A function can be stored inside a dictionary and called later.

## Dictionary Dispatch

Using a dictionary instead of a long `if/elif` chain makes code easier to extend and maintain.

## Single Responsibility

Each function should have one clear job.

---

# Mentor Feedback

## Overall Score

**9.3 / 10**

### Breakdown

| Area | Score |
|------|------:|
| Tuple Exercises | 10/10 |
| Dictionary Exercises | 9.5/10 |
| DSA Thinking | 9/10 |
| Calculator Design | 9.5/10 |
| Engineering Mindset | 9.5/10 |

Excellent progress. You are moving from writing Python syntax to designing cleaner programs.

---

# Next Session (Day 8)

- Learn Sets
- Refactor Calculator V4
- Continue DSA practice
- Make one Git commit
