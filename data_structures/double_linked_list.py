class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            temp.previous = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.previous
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.previous = before
        new_node.next = after
        before.next = new_node
        after.previous = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        temp.next.previous = temp.previous
        temp.previous.next = temp.next
        temp.next = None
        temp.previous = None
        self.length -= 1
        return temp

    def swap_first_last(self):
        if self.length == 0:
            return False
        head_value = self.head.value
        tail_value = self.tail.value
        self.head.value = tail_value
        self.tail.value = head_value
        return True

    def reverse(self):
        current_node = self.head
        while current_node:
            temp_next = current_node.next
            current_node.next = current_node.previous
            current_node.previous = temp_next
            current_node = temp_next

        temp = self.head
        self.head = self.tail
        self.tail = temp

    def is_palindrome(self):
        if self.length <= 1:
            return True
        forward_node = self.head
        backward_node = self.tail
        for i in range(self.length // 2):
            if forward_node.value != backward_node.value:
                return False
            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return None
        dummy = Node(0)
        dummy.next = self.head
        previous_node = dummy
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            second_node.previous = previous_node
            first_node.previous = second_node
            if first_node.next:
                first_node.next.previous = first_node
            self.head = first_node.next
            previous_node = first_node
        self.head = dummy.next
        if self.head:
            self.head.previous = None
