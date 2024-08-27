Double Linked List
================

A Python implementation of a Double Linked List data structure.

Table of Contents
-----------------

* [Features](#features)
* [Methods](#methods)
* [Example Use Cases](#example-use-cases)
* [License](#license)
* [Contributing](#contributing)

Features
--------

*   **Dynamic size**: The Double Linked List can grow or shrink dynamically as elements are added or removed.
*   **Efficient insertion and deletion**: Elements can be inserted or deleted at any position in the Double Linked List in O(1) time.
*   **Flexible data structure**: The Double Linked List can be used to implement various data structures such as stacks, queues, and trees.

Methods
-------

*   `__init__`: Initializes an empty Double Linked List.
*   `__sizeof__`: Returns the size of the Double Linked List.
*   `__iadd__`: Adds one or more elements to the end of the Double Linked List.
*   `__isub__`: Removes one or more elements from the Double Linked List.
*   `__iter__`: Returns an iterator over the elements in the Double Linked List.
*   `__next__`: Returns the next element in the Double Linked List.
*   `__eq__`: Checks if two Double Linked Lists are equal.
*   `add`: Adds an element to the end of the Double Linked List.
*   `remove`: Removes an element from the Double Linked List.

Example Use Cases
-----------------

```python
# Create an empty Double Linked List
double_linked_list = DoubleLinkedList()

# Add elements to the Double Linked List
double_linked_list.add(1)
double_linked_list.add(2)
double_linked_list.add(3)

# Print the Double Linked List
print(double_linked_list)  # Output: [1, 2, 3]

# Remove an element from the Double Linked List
double_linked_list.remove(2)

# Print the Double Linked List
print(double_linked_list)  # Output: [1, 3]
```

License
-------

This implementation is licensed under the MIT License.

Contributing
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.