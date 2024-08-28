from abc import ABC


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def __str__(self) -> str:
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def __str__(self) -> str:
        return str(self.root)
        pass


tree = BinarySearchTree()

for n in [10, 5, 15, 3, 7, 13]:
    tree.insert(n)
