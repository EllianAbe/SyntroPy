

**Doubly Linked List Implementation**
=====================================

**Overview**
------------

This is a Python implementation of a doubly linked list data structure. A doubly linked list is a linear data structure where each node has two pointers, one pointing to the next node and one pointing to the previous node.

**Features**
------------

*   **Efficient insertion and deletion**: Elements can be added or removed from the list in O(1) time.
*   **Flexible iteration**: The list can be iterated in both forward and backward directions.
*   **Equality checking**: Two doubly linked lists can be compared for equality.

**Methods**
------------

*   `__init__`: Initializes a new doubly linked list.
*   `__sizeof__`: Returns the size of the linked list.
*   `__iadd__`: Adds one or more elements to the end of the linked list.
*   `__isub__`: Removes one or more elements from the linked list.
*   `__iter__`: Returns an iterator object for the linked list.
*   `__next__`: Returns the next element in the linked list.
*   `__eq__`: Compares two doubly linked lists for equality.
*   `add`: Adds a new element to the end of the linked list.
*   `remove`: Removes the first occurrence of an element from the linked list.

**Example Usage**
-----------------

```python
dll = DoublyLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)

print(dll)  # Output: 1 -> 2 -> 3

dll.remove(2)

print(dll)  # Output: 1 -> 3

dll2 = DoublyLinkedList()
dll2.add(1)
dll2.add(3)

print(dll == dll2)  # Output: True
```

**License**
----------

This implementation is licensed under the MIT License.