# Notes.md

## Day 22

### Time Complexity Recap

-   One range sum query using a loop takes **O(N)** in the worst case.
-   For **Q** queries, total complexity is **O(Q × N)**.

### Prefix Sum

#### Definition

A Prefix Sum array stores the cumulative sum of elements from index `0`
to the current index.

Example:

``` python
arr = [2, 5, 1, 8, 3]
prefix = [2, 7, 8, 16, 19]
```

#### Construction

-   `prefix[0] = arr[0]`
-   `prefix[i] = prefix[i-1] + arr[i]`

Time Complexity: **O(N)** Space Complexity: **O(N)**

### Range Sum Query

If `L == 0`:

``` text
answer = prefix[R]
```

Otherwise:

``` text
answer = prefix[R] - prefix[L-1]
```

Query Complexity: **O(1)**

### Complexity Comparison

Without Prefix Sum: - Build: None - Query: O(N) - Total for Q queries:
O(Q × N)

With Prefix Sum: - Build: O(N) - Query: O(1) - Total: O(N + Q)

### Limitation

If `arr[i]` changes: - Prefix values before `i` remain unchanged. -
Prefix values from `i` onward must be recalculated. - Update complexity
becomes **O(N)**.

### Key Takeaways

-   Prefix Sum is excellent for many range-sum queries on a static
    array.
-   It is not ideal when the array is updated frequently.
-   This limitation motivates data structures like Fenwick Trees and
    Segment Trees.
