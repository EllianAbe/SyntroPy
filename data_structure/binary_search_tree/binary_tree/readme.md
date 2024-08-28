**Binary Search Tree**
=====================

A Binary Search Tree (BST) is a data structure in which each node has at most two children (i.e., left child and right child). Each node represents a value, and the left subtree of a node contains only values less than the node's value, while the right subtree of a node contains only values greater than the node's value.

**Node Class**
---------------

The `Node` class represents a single node in the BST. Each node has the following properties:

* `value`: The value stored in the node.
* `left`: The left child of the node.
* `right`: The right child of the node.

**BinarySearchTree Class**
-----------------------

The `BinarySearchTree` class represents the BST itself. It has the following properties and methods:

* `root`: The root node of the tree.
* `insert(value)`: Inserts a new node with the given value into the tree.
* `__str__()`: Returns a string representation of the tree.

**Insertion**
-------------

When a new value is inserted into the tree, the `insert` method is called. This method recursively traverses the tree to find the correct location for the new node.

**Example Use Case**
--------------------

Here is an example of creating a BST and inserting values:
```python
tree = BinarySearchTree()

for n in [10, 5, 15, 3, 7, 13]:
    tree.insert(n)

print(tree)
```
This will create a BST with the values 10, 5, 15, 3, 7, and 13, and print the tree.

**Note**
--------

This implementation of a BST does not handle duplicate values. If you try to insert a value that already exists in the tree, it will be ignored.

**Future Development**
---------------------

*   Handling duplicate values
*   Implementing deletion of nodes
*   Implementing traversal methods (e.g., inorder, preorder, postorder)