# Day 18 Notes -- Two Pointers, Dependency Injection & Better Encapsulation

## Progress Summary

-   Optimal Two Pointer solutions
-   Dependency Injection (DI)
-   Better encapsulation using getter/setter methods
-   Cleaner object-oriented design
-   Reviewing duplicated code
-   Thinking about consistent error handling

------------------------------------------------------------------------

## Two Pointer Pattern

Two pointers usually have different responsibilities:

-   Read pointer → scans the array
-   Write pointer → stores valid elements

Advantages: - O(n) time - O(1) extra space - No unnecessary shifting of
elements

------------------------------------------------------------------------

## LeetCode 26 -- Remove Duplicates

Algorithm: 1. Keep one pointer on the last unique value. 2. Scan the
array with another pointer. 3. Copy only new unique values.

Complexity: - Time: O(n) - Space: O(1)

------------------------------------------------------------------------

## LeetCode 27 -- Remove Element

Algorithm: 1. Scan every element. 2. Copy only values not equal to
`val`. 3. Return the new length.

Complexity: - Time: O(n) - Space: O(1)

------------------------------------------------------------------------

## Dependency Injection

Instead of creating an engine inside the Car class:

    self.engine = Engine()

Inject it from outside:

    engine = PetrolEngine()
    car = Car("Suzuki", engine)

Benefits: - Loose coupling - Easier testing - Easier replacement of
implementations - Better maintainability

------------------------------------------------------------------------

## Encapsulation

Instead of directly accessing:

    cal.last_result

Use:

    cal.get_last_result()
    cal.set_last_result(result)

Instead of:

    cal.memory

Use:

    cal.memory_recall()

------------------------------------------------------------------------

## Code Duplication

Repeated pattern:

    result = ...
    self.last_result = result
    return result

Repeated code often indicates an opportunity to refactor.

------------------------------------------------------------------------

## Error Handling

Current approach:

    return "Cannot divide by zero"

Future improvement: - Raise exceptions instead of returning error
strings. - Handle invalid operations (like "%") gracefully.

------------------------------------------------------------------------

## Naming Conventions

Prefer: - brand_name - start() - stop()

Avoid: - brandName - carStart() - carstop()

------------------------------------------------------------------------

## Bug Found

Inside carstop(), call:

    self.engine.stop()

instead of:

    self.engine.start()

------------------------------------------------------------------------

## Reflection Questions

1.  What is Dependency Injection?
2.  Why is it useful?
3.  Why are two pointers O(n)?
4.  Why is encapsulation important?
5.  How should calculate() handle invalid operations?

------------------------------------------------------------------------

## Preparation for Day 19

-   @property
-   @classmethod
-   @staticmethod
-   Custom Exceptions
-   Git Branching
-   Sliding Window
