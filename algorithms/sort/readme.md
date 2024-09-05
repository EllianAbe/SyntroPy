

**Bubble Sort Algorithms**
==========================

This file contains two implementations of the bubble sort algorithm in Python: `bubble_sort` and `swapped_bubble_sort`.

**Overview**
------------

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

**Implementations**
------------------

### bubble_sort

This implementation uses a nested loop to iterate through the list, comparing adjacent elements and swapping them if necessary.

```python
def bubble_sort(arr):
    arr = arr.copy()
    print(arr)

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
```

### swapped_bubble_sort

This implementation uses a while loop to iterate through the list, comparing adjacent elements and swapping them if necessary. The loop continues until no more swaps are needed, indicating that the list is sorted.

```python
def swapped_bubble_sort(arr):
    arr = arr.copy()
    print(arr)

    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print(arr)
```

**Example Use Cases**
---------------------

```python
input = [5, 3, 6, 2, 10]

bubble_sort(input)
print('*' * 20)
swapped_bubble_sort(input)
```

This will output the sorted list using both algorithms, with intermediate steps printed to the console.

**Note**
--------

These implementations have a time complexity of O(n^2), making them less efficient for large datasets. However, they can be useful for educational purposes or small datasets.