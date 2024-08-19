class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data
        return NotImplemented


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __sizeof__(self) -> int:
        self.size

    def __iadd__(self, other):
        self.append(other)

        return self

    def __isub__(self, other):
        self.delete(other)

        return self

    def __iter__(self):
        """Allow iteration over the LinkedList"""
        self.current = self.head
        return self

    def __next__(self):
        """Return the next item in the LinkedList"""
        if self.current is None:
            raise StopIteration

        data = self.current.data
        self.current = self.current.next
        return data

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            if self.size != other.size:
                return False

            current1 = self.head
            current2 = other.head

            while current1 and current2:
                if current1.data != current2.data:
                    return False

                current1 = current1.next
                current2 = current2.next

            return current1 is None and current2 is None

        return NotImplemented

    def append(self, data):
        """Add a node at the end of the LinkedList"""
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """Add a node at the beginning of the LinkedList"""
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def delete(self, data):
        """Delete a node with the given data"""
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                self.size -= 1
                return
            current = current.next

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return ' -> '.join(nodes)


# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list += 3

print(linked_list)
linked_list.prepend(0)
print(linked_list)
linked_list.delete(2)
linked_list -= 1
print(linked_list)

for i in linked_list:
    print(i)
