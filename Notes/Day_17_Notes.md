# Day 17 Notes -- Composition, Refactoring & Two Pointer Practice

## Progress Summary

Today you learned:

-   Composition
-   "Has-a" vs "Is-a" relationships
-   Refactoring responsibilities into classes
-   Improving calculator architecture
-   More practice with the Two Pointer pattern
-   Reviewing algorithm complexity

------------------------------------------------------------------------

# Composition

Composition means one object **contains** another object.

Example:

``` python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()
```

A **Car has an Engine**.

This is composition.

------------------------------------------------------------------------

# Composition vs Inheritance

## Inheritance

Use inheritance when there is an **Is-a** relationship.

``` text
Dog is an Animal
Cat is an Animal
```

Example:

``` python
class Animal:
    pass

class Dog(Animal):
    pass
```

------------------------------------------------------------------------

## Composition

Use composition when there is a **Has-a** relationship.

``` text
Car has an Engine
Computer has a CPU
House has Rooms
```

Composition usually creates more flexible programs.

------------------------------------------------------------------------

# Why Composition is Often Preferred

Advantages:

-   Less coupling between classes
-   Easier to replace components
-   Better code reuse
-   Easier to test
-   Easier to extend

------------------------------------------------------------------------

# Calculator Refactoring

## Before

`main.py` decided which operation to execute.

``` python
operations[choice](num1, num2)
```

------------------------------------------------------------------------

## After

The calculator owns the decision.

``` python
cal.calculate("+", 5, 3)
```

``` python
def calculate(self, operation, num1, num2):
    operations = {
        "+": self.add,
        "-": self.sub,
        "*": self.multiply,
        "/": self.divide
    }

    return operations[operation](num1, num2)
```

Benefits:

-   Cleaner `main.py`
-   Better abstraction
-   Easier to add new operations

------------------------------------------------------------------------

# Encapsulation Reminder

Avoid direct attribute access whenever possible.

Instead of:

``` python
cal.memory
```

Prefer:

``` python
cal.memory_recall()
```

Future improvement:

``` python
cal.get_last_result()
```

------------------------------------------------------------------------

# Code Duplication

Notice the repeated pattern:

``` python
result = ...
self.last_result = result
return result
```

Repeated code is a signal that future refactoring may be useful.

------------------------------------------------------------------------

# DSA Notes

## Remove Element

Your solution:

``` python
while val in nums:
    nums.remove(val)
```

Correct ✔

Complexity:

-   Worst case: **O(n²)**

Reason:

-   `remove()` searches for the value.
-   Removing shifts remaining elements.

Optimal interview solution:

Two pointers.

Time:

**O(n)**

------------------------------------------------------------------------

## Remove Duplicates from Sorted Array

Your solution used:

``` python
nums.pop(i)
```

Correct ✔

Complexity:

Worst case:

**O(n²)**

Reason:

Every `pop(i)` shifts later elements.

Optimal approach:

Overwrite duplicates using two pointers.

Time:

**O(n)**

------------------------------------------------------------------------

# Python Naming Conventions

Prefer `snake_case`.

Good:

``` python
show_brand()
start()
stop()
brand_name
```

Avoid:

``` python
carBrand()
carStart()
brandName
```

------------------------------------------------------------------------

# Better Composition Design

Instead of creating dependencies internally:

``` python
self.engine = Engine()
```

A more flexible design is:

``` python
engine = Engine()
car = Car("Suzuki", engine)
```

This makes it easier to replace the engine later.

This idea is called **Dependency Injection**.

------------------------------------------------------------------------

# Code Review Feedback

## Good

-   Correct use of composition
-   Calculator refactored successfully
-   Dictionary dispatch maintained
-   Cleaner separation of responsibilities
-   Correct DSA solutions

## Improvements

-   Use encapsulation consistently.
-   Follow snake_case naming.
-   Learn optimal O(n) two pointer solutions.
-   Consider exceptions instead of returning error strings.

------------------------------------------------------------------------

# Key Takeaways

-   Inheritance represents **Is-a**.
-   Composition represents **Has-a**.
-   Prefer composition unless inheritance is clearly appropriate.
-   Keep `main.py` focused on coordinating the program.
-   Refactoring improves maintainability.
-   Correct code is important, but efficient algorithms matter too.

------------------------------------------------------------------------

# Reflection Questions

1.  What is the difference between composition and inheritance?
2.  When should you use composition?
3.  Why is the refactored calculator cleaner?
4.  Why are `remove()` and `pop()` slower in these problems?
5.  How would you improve the calculator further?

------------------------------------------------------------------------

# Preparation for Day 18

Next topics:

-   Dependency Injection
-   `@property`
-   Better encapsulation
-   Refactoring repeated calculator code
-   Optimal Two Pointer algorithms
-   Git basics (repository, commits, history)
