from abc import ABC


class Node:
    def __init__(self, value):
        self.left: Node = None
        self.right: Node = None
        self.value = value
        self.height = 1

    def __str__(self) -> str:
        return str(self.value)


class AVLSearchTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root: Node | None, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if -1 <= balance <= 1:
            return root

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

    def get_height(self, root: Node | None) -> int:
        if root is None:
            return 0

        return root.height

    def get_balance(self, root: Node | None) -> int:
        if root is None:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, root: Node) -> Node:
        original_root = root

        # The left child of the original root becomes the new root
        new_root = original_root.left

        # The right subtree of the new root becomes the left subtree of the original root
        original_root.left = new_root.right

        # The original root becomes the right child of the new root
        new_root.right = original_root

        # Update the height of the original root and the new root
        original_root.height = 1 + max(self.get_height(original_root.left),
                                       self.get_height(original_root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),
                                  self.get_height(new_root.right))

        return new_root

    def left_rotate(self, root: Node) -> Node:
        original_root = root

        # The right child of the original root becomes the new root
        new_root = original_root.right

        # The left subtree of the new root becomes the right subtree of the original root
        original_root.right = new_root.left

        # The original root becomes the left child of the new root
        new_root.left = original_root

        # Update the height of the original root and the new root
        original_root.height = 1 + max(self.get_height(original_root.left),
                                       self.get_height(original_root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),
                                  self.get_height(new_root.right))

        return new_root

    def print_order(self):
        self._print_order(self.root)

    def _print_order(self, root: Node | None = None):
        if root is None:
            return

        self._print_order(root.left)
        print(root.value)
        self._print_order(root.right)

    def __str__(self) -> str:
        return str(self.root)
        pass


tree = AVLSearchTree()

for n in [10, 5, 15, 3, 7, 13]:
    tree.insert(n)

tree.print_order()
