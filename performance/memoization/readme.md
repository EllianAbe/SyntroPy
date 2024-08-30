**Memoization**
================

**Overview**
------------

Memoization is a programming technique used to speed up programs by storing the results of expensive function calls and reusing them when the same inputs occur again.

**How it Works**
----------------

Memoization works by storing the results of function calls in a cache, typically a hash table or dictionary. When a function is called with a set of inputs, the cache is checked to see if the result is already stored. If it is, the stored result is returned instead of recalculating it. If not, the result is calculated, stored in the cache, and returned.

**Benefits**
------------

*   Improves performance by reducing the number of expensive function calls
*   Reduces the time complexity of algorithms by avoiding redundant calculations
*   Simplifies code by eliminating the need for redundant calculations

**Example Use Case**
--------------------

Here is an example of using memoization to improve the performance of a recursive function:
```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```
This implementation of the Fibonacci function uses a dictionary `memo` to store the results of previous function calls. If the result is already stored, it is returned instead of recalculating it.

You can opt for just add a cache decorator:
```python
import functools

@functools.cache
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```

**Implementation**
-----------------

*   Create a cache to store the results of function calls
*   Check the cache before calculating a result
*   Store the result in the cache after calculating it
*   Return the stored result instead of recalculating it