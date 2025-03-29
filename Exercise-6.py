from time import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_left(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_right(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = node

    def delete_left(self):
        if self.head is None:
            return IndexError
        temp = self.head
        self.head = self.head.next
        temp.next = None

    def delete_right(self):
        if self.head is None:
            return IndexError
        last = self.head
        while last.next is not None and last.next.next is not None:
            last = last.next
        last.next = None

    def peek_left(self):
        if self.head is None:
            raise IndexError
        return self.head.data

    def peek_right(self):
        if self.head is None:
            raise IndexError
        last = self.head
        while last.next is not None:
            last = last.next
        return last.data

    def __str__(self):
        data = []
        temp = self.head
        while temp is not None:
            data.append(temp.data)
        return ' -> '.join(data for data in data)


class DoubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

class DoublyLinkedListOptimized:
    def __init__(self):
        self.front = None
        self.back = None

    def insert_left(self, data):
        node = DoubleNode(data)
        if self.front is None:
            self.front = self.back = node
        else:
            self.front.prev = node
            node.next = self.front
            self.front = node

    def insert_right(self, data):
        node = DoubleNode(data)
        if self.back is None:
            self.front = self.back = node
        else:
            self.back.next = node
            node.prev = self.back
            self.back = node

    def delete_left(self):
        if self.front is None:
            return
        else:
            temp = self.front
            if self.front.next is not None:
                self.front = self.front.next
                self.front.prev = None
            else:
                self.front = None
                self.back = None
            temp.next = None

    def delete_right(self):
        if self.back is None:
            return
        else:
            temp = self.back
            if self.back.prev is not None:
                self.back = self.back.prev
                self.back.next = None
            else:
                self.back = self.front = None
            temp.prev = None

    def peek_left(self):
        if self.front is None:
            raise IndexError
        else:
            return self.front.data

    def peek_right(self):
        if self.back is None:
            raise IndexError
        else:
            return self.back.data

    def __str__(self):
        values = []
        current = self.front
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return ' <-> '.join(values)

class LinkedListOptimized:
    def __init__(self):
        self.front = None
        self.tail = None

    def insert_left(self, data):
        node = Node(data)
        if self.front is None:
            self.front = self.tail = node
        else:
            self.front.next = node
            self.front = node

    def insert_right(self, data):
        node = Node(data)
        if self.tail is None:
            self.front = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete_left(self):
        if self.front is None:
            return IndexError
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None

    def delete_right(self):
        if self.front is None:
            return IndexError
        last = self.front
        while last.next is not None and last.next.next is not None:
            last = last.next
        last.next = None


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{func.__name__}{args}{kwargs} took", (end - start) * 1000, "ms")
        return result
    return wrapper

@timer
def llisttest(nodes:int):
    llist = LinkedList()
    for i in range(nodes):
        llist.insert_left(i)
        llist.insert_right(i)
    for i in range(nodes):
        llist.delete_left()
        llist.delete_right()

@timer
def dllisttest(nodes):
    dllist = DoublyLinkedListOptimized()
    for i in range(nodes):
        dllist.insert_left(i)
        dllist.insert_right(i)
        dllist.delete_right()
        dllist.delete_left()

@timer
def llistoptimizedtest(nodes):
    llist = LinkedListOptimized()
    for i in range(nodes):
        llist.insert_left(i)
        llist.insert_right(i)
    for i in range(nodes):
        llist.delete_left()
        llist.delete_right()

llist = LinkedList()
llistoptimized = LinkedListOptimized()

llist.insert_left(1)
llist.insert_right(2)
llist.insert_right(3)
llist.delete_right()
print(llist)

llistoptimized.insert_left(1)
llistoptimized.insert_right(2)
llistoptimized.insert_right(3)
llistoptimized.delete_right()
print(llistoptimized)
