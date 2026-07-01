# Day 6 Notes – Lists, Algorithms & Calculator V3

## Progress Summary

Today you completed:

- ✅ Introduction to Lists
- ✅ Basic List Operations
- ✅ List Traversal with `for` loops
- ✅ Algorithm planning before coding
- ✅ Calculator Version 3 with History
- ✅ Continued developing an engineering mindset

---

# Lists

## What is a List?

A list is an ordered, mutable collection that can store multiple values.

Example:

```python
movies = ["Dhurandhar", "Sita Ramam", "Avengers"]
```

## Operations Practiced

### Accessing Elements

```python
movies[0]
movies[-1]
```

### Updating an Element

```python
movies[2] = "Avatar"
```

### Adding an Element

```python
movies.append("KGF")
```

### Removing an Element

```python
movies.pop(1)
```

### Traversing a List

```python
for movie in movies:
    print(movie)
```

---

# Exercise Review

Completed:

- Created a list of movies
- Printed list elements
- Updated an element
- Added a new movie
- Removed a movie
- Printed all movies using a loop

### Small Review Note

The exercise asked for the **first** and **last** movie.

Current code used:

```python
movies[1]
movies[4]
```

Remember:

- First element → `movies[0]`
- Last element → `movies[-1]`

---

# DSA Thinking Practice

## Problem 1 – Largest Element

### Input

A list of numbers

### Output

Largest number

### Approach

- Initialize a variable.
- Traverse the list.
- Compare each element.
- Update the current largest value.
- Print or return the result.

### Time Complexity

**O(n)**

### Mentor Improvement

Instead of initializing with `None` or using `sys`, think about starting with the **first element of the list**.

---

## Problem 2 – Count Positive, Negative and Zero

### Input

A list of numbers

### Output

Count of positive, negative and zero values

### Approach

- Initialize:
  - `positive = 0`
  - `negative = 0`
  - `zero = 0`
- Traverse the list.
- Update the correct counter.
- Print the counters.

### Time Complexity

**O(n)**

---

## Problem 3 – Sum of All Elements

### Input

A list of numbers

### Output

Sum of all elements

### Approach

- Initialize `total = 0`
- Traverse the list
- Add each element to `total`
- Return or print the result

### Time Complexity

**O(n)**

---

# Calculator Version 3

## New Feature

Added calculation history.

```python
history = []
```

Each calculation is stored like:

```text
5 + 6 = 11
8 * 3 = 24
```

History is displayed by simply iterating over the list.

### Engineering Lesson

> Don't transform data unless you have a reason to.

If the string already looks correct, simply display it.

---

# Code Review

## What Went Well

- Functions are small and focused.
- Added history using a list.
- Good separation of calculator operations.
- Good algorithm planning before coding.
- Correct use of loops.

---

## Suggested Improvements

### 1. Remove unnecessary return value

Current:

```python
def add_history(...):
    history.append(...)
    return "saved"
```

Returning `"saved"` is unnecessary because users don't need to see it.

---

### 2. Better Function Name

Instead of:

```python
multi()
```

Prefer:

```python
multiply()
```

Descriptive names improve readability.

---

### 3. Division by Zero

Currently failed division is also added to history.

Think about whether unsuccessful operations should be stored.

---

### 4. Reduce Repeated Code

This code appears four times:

```python
num1 = int(input(...))
num2 = int(input(...))
```

A helper function can remove this duplication.

---

### 5. Empty History

Before displaying history, check whether the list is empty.

Display:

```text
No history available.
```

instead of printing nothing.

---

# Engineering Mindset

Today's biggest lesson:

> The simplest correct solution is usually the best one.

Avoid adding complexity unless it solves a real problem.

---

# Progress Review

## Strengths

- Thinking before coding.
- Writing algorithms first.
- Better code organization.
- Comfortable using functions.
- Beginning to recognize duplicated code.

## Areas to Improve

- Reduce repetition.
- Choose descriptive names.
- Handle edge cases.
- Continue simplifying solutions.

---

# Mentor Feedback

Overall Score: **8.9 / 10**

### Breakdown

| Area | Score |
|------|------:|
| List Exercises | 9/10 |
| Algorithm Thinking | 9/10 |
| Functions | 9/10 |
| Calculator Design | 8.5/10 |
| Engineering Mindset | 9/10 |

Excellent progress. You're moving from writing Python syntax toward designing cleaner software.

---

# Next Session (Day 7)

Before starting Day 7:

- [ ] Remove the `"saved"` return value.
- [ ] Show `"No history available."` when history is empty.
- [ ] Create a helper function to read two numbers.
- [ ] Commit Calculator V3 to Git (if using Git).

Upcoming topics:

- Tuples
- Dictionaries
- More list practice
