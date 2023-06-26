class DLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self, value):
        node = DLNode(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        new_node = DLNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1

    def pop(self):
        temp_value = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.length -= 1
        return temp_value.value


dll = DoubleLinkedList(1)
print(dll.pop())
print(dll.tail.value)
