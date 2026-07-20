# Day 20 Notes

## Topics Covered

-   Inheritance
-   Parent and Child Classes
-   `super()`
-   Constructor Inheritance
-   Method Overriding (Introduction)
-   LeetCode 53 (Brute Force)
-   Calculator Project Improvements

------------------------------------------------------------------------

## Inheritance

Inheritance lets a child class reuse the code of a parent class.

### Benefits

-   Reduces code duplication (DRY)
-   Improves code reuse
-   Easier maintenance
-   Models "is-a" relationships

Example:

``` python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass
```

------------------------------------------------------------------------

## Parent and Child Classes

``` python
class Person:
    ...

class Student(Person):
    ...
```

-   `Person` → Parent (Base) Class
-   `Student` → Child (Derived) Class

A Student **is a** Person.

------------------------------------------------------------------------

## `super()`

Use `super()` to call the parent constructor.

``` python
class Student(Person):

    def __init__(self, name, age, roll_num):
        super().__init__(name, age)
        self.roll_num = roll_num
```

------------------------------------------------------------------------

## Method Overriding

A child class can replace a parent's method by defining a method with
the same name.

``` python
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")
```

------------------------------------------------------------------------

## DSA

### LeetCode 53 -- Maximum Subarray

Brute-force idea:

``` python
for i in range(len(nums)):
    curr_sum = 0
    for j in range(i, len(nums)):
        curr_sum += nums[j]
```

Complexity: - Time: O(n²) - Space: O(1)

Important edge case:

If all numbers are negative, the answer is the largest (least negative)
value, not `0`.

------------------------------------------------------------------------

## Calculator Project

Completed: - Added Power (`^`) - Added Modulo (`%`) - Kept modular
structure: - calculator.py - history.py - menu.py - main.py

Suggested improvements: - Handle modulo by zero. - Number history
entries.

------------------------------------------------------------------------

## Key Takeaways

-   Inheritance avoids repeating code.
-   Child classes inherit methods and attributes.
-   `super()` initializes parent attributes.
-   Method overriding customizes inherited behavior.
-   Always consider edge cases in DSA.

------------------------------------------------------------------------

## Day 20 Completed ✅
