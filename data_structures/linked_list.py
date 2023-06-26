class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = SLNode(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = SLNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next

            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None

            return temp

    def prepend(self, value):
        new_node = SLNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = SLNode(value)
            temp = self.get(index - 1)

            new_node.next = temp.next
            temp.next = new_node

            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        temp_slow = self.head
        temp_fast = self.head
        while temp_fast and temp_fast.next:
            temp_slow = temp_slow.next
            temp_fast = temp_fast.next.next
        return temp_slow

    def has_loop(self):
        temp_slow = self.head
        temp_fast = self.head
        while temp_fast and temp_fast.next:
            temp_slow = temp_slow.next
            temp_fast = temp_fast.next.next
            if temp_fast == temp_slow:
                return True
        return False


def find_kth_from_end(linked_list, value):
    temp_slow = temp_fast = linked_list.head
    for _ in range(value):
        if temp_fast is None:
            return None
        temp_fast = temp_fast.next

    while temp_fast:
        temp_slow = temp_slow.next
        temp_fast = temp_fast.next

    return temp_slow



