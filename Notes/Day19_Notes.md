# Day 19 Notes

## Topics Covered

-   `@property`
-   `@property.setter`
-   `@classmethod`
-   `@staticmethod`
-   Exception Handling
-   Sliding Window
-   Running Minimum (Best Time to Buy and Sell Stock)
-   Calculator Project Improvements

------------------------------------------------------------------------

## Python OOP

### `@property`

Access a method like an attribute.

``` python
@property
def balance(self):
    return self._balance
```

### `@property.setter`

Validate values before updating an attribute.

``` python
@balance.setter
def balance(self, amount):
    if amount >= 0:
        self._balance = amount
```

### `@classmethod`

Works with class variables.

``` python
@classmethod
def change_bank_name(cls, new_name):
    cls.bank_name = new_name
```

### `@staticmethod`

Utility methods that don't need `self` or `cls`.

``` python
@staticmethod
def is_valid_amount(amount):
    return amount > 0
```

------------------------------------------------------------------------

## Calculator Project

Structure:

    main.py
    calculator.py
    history.py
    menu.py

Responsibilities: - calculator.py → calculations, memory, last result -
history.py → history, clear, undo - menu.py → display menu - main.py →
user interaction and exception handling

------------------------------------------------------------------------

## DSA

### Sliding Window

    new_window = old_window
                 - outgoing
                 + incoming

-   Time: O(n)
-   Space: O(1)

### Running Minimum

    minimum = min(minimum, current)
    profit = current - minimum
    answer = max(answer, profit)

-   Time: O(n)
-   Space: O(1)

------------------------------------------------------------------------

## Key Takeaways

-   Protect data using properties.
-   Validate data with setters.
-   Use class methods for shared class data.
-   Use static methods for helper logic.
-   Raise exceptions for invalid operations.
-   Follow Single Responsibility Principle.
-   Sliding Window avoids recomputing sums.
-   Running Minimum solves optimization problems efficiently.

------------------------------------------------------------------------

# Day 19 Completed ✅
