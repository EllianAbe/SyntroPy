**AVL Trees: A Self-Balancing Binary Search Tree**
=====================================================

An AVL tree is a type of self-balancing binary search tree that ensures the height of the tree remains relatively small by rotating nodes when the balance factor becomes too large. This leads to an efficient search, insertion, and deletion of nodes in the tree.

**Node Class**
---------------

The `Node` class represents a single node in the AVL tree. Each node has the following properties:

* `value`: The value stored in the node.
* `left`: The left child of the node.
* `right`: The right child of the node.
* `height`: The height of the node.

**AVLSearchTree Class**
-----------------------

The `AVLSearchTree` class represents the AVL tree itself. It has the following properties and methods:

* `root`: The root node of the tree.
* `insert(value)`: Inserts a new node with the given value into the tree.
* `right_rotate(root)`: Rotates the tree to the right at the given root node.
* `left_rotate(root)`: Rotates the tree to the left at the given root node.
* `get_height(root)`: Returns the height of the tree at the given root node.
* `get_balance(root)`: Returns the balance factor of the tree at the given root node.
* `print_order()`: Prints the values in the tree in order.

**Insertion**
-------------

When a new node is inserted into the tree, the `insert` method is called. This method recursively traverses the tree to find the correct location for the new node. Once the new node is inserted, the tree is rebalanced by rotating nodes if necessary.

**Rotation**
------------

The `right_rotate` and `left_rotate` methods are used to rebalance the tree when the balance factor becomes too large. These methods rotate the tree at the given root node, ensuring that the tree remains balanced.

**Balance Factor**
------------------

The balance factor of a node is calculated by subtracting the height of the right subtree from the height of the left subtree. If the balance factor becomes too large, the tree is rebalanced by rotating nodes.

**Example Use Case**
--------------------

Here is an example of creating an AVL tree and inserting values:
```python
tree = AVLSearchTree()

for n in [10, 5, 15, 3, 7, 13]:
    tree.insert(n)

tree.print_order()
```
This will create an AVL tree with the values 10, 5, 15, 3, 7, and 13, and print the values in order.

Note: This explanation is based on the provided code snippets and may not be a comprehensive explanation of AVL trees.