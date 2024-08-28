class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __sizeof__(self):
        return self.size

    def __iadd__(self, other):
        if isinstance(other, list):
            for item in other:
                self.add(item)
        else:
            self.add(other)
        return self

    def __isub__(self, other):
        if isinstance(other, list):
            for item in other:
                self.remove(item)
        else:
            self.remove(other)
        return self

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

    def __eq__(self, other):
        if isinstance(other, DoublyLinkedList):
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

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        self.size += 1

    def remove(self, data, raise_error=False):
        current = self.head

        while current is not None:
            if current.data != data:
                current = current.next
                continue

            if current == self.head:
                self.head = current.next
                if self.head is not None:
                    self.head.previous = None
            elif current == self.tail:
                self.tail = current.previous
                if self.tail is not None:
                    self.tail.next = None
            else:
                current.previous.next = current.next
                current.next.previous = current.previous

            self.size -= 1

            return

        if raise_error:
            raise ValueError(f'{data} not found')

    def __str__(self):
        return ' -> '.join(str(item) for item in self)
