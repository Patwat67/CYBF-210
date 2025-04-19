import sys
from time import time, sleep

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __sizeof__(self):
        mem = 8 # for 1 next pointer
        mem += sys.getsizeof(self.data)
        return mem

class DoubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

    def __sizeof__(self):
        mem = super().__sizeof__()
        mem += 8 # for additional prev pointer
        return mem

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
            temp = temp.next
        return ' -> '.join(str(data) for data in data)

    def __sizeof__(self):
        mem = 0
        temp = self.head
        while temp is not None:
            mem += sys.getsizeof(temp)
            temp = temp.next
        return mem

class LinkedListOptimized:
    def __init__(self):
        self.front = None
        self.tail = None
        self.count = 0

    def insert_left(self, data):
        node = Node(data)
        if self.count == 0:
            self.front = self.tail = node
        else:
            node.next = self.front
            self.front = node
        self.count += 1

    def insert_right(self, data):
        node = Node(data)
        if self.count == 0:
            self.front = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def delete_left(self):
        if self.count == 0:
            return IndexError
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
        self.count -= 1
        if self.count == 0:
            self.front = self.tail = None

    def delete_right(self):
        if self.count == 0:
            return IndexError
        last = self.front
        while last.next is not None and last.next.next is not None:
            last = last.next
        last.next = None
        self.count -= 1

    def peek_left(self):
        if self.count == 0:
            return IndexError
        else:
            return self.front.data

    def peek_right(self):
        if self.count == 0:
            return IndexError
        else:
            return self.tail.data

    def __str__(self):
        data = []
        temp = self.front
        while temp is not None:
            data.append(temp.data)
            temp = temp.next
        return ' -> '.join(str(data) for data in data)

    def __sizeof__(self):
        mem = 0
        temp = self.front
        while temp is not None:
            mem += sys.getsizeof(temp)
            temp = temp.next
        return mem

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
        data = []
        temp = self.front
        while temp is not None:
            data.append(temp.data)
            temp = temp.next
        return ' <-> '.join(str(data) for data in data)

    def __sizeof__(self):
        mem = 0
        temp = self.front
        while temp is not None:
            mem += sys.getsizeof(temp)
            temp = temp.next
        return mem

def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{func.__name__}{args}{kwargs} took {((end - start) * 1000):.2f}ms")
        return result
    return wrapper

@timer
def llisttest(n:int):
    print("\n---Linked list test---")
    l = LinkedList()
    print("Testing insertions...")
    for i in range(n):
        l.insert_left(None)
        l.insert_right(None)
    print(f"{(sys.getsizeof(l) / 1_000_000):.0f}MB of memory used")
    print("Testing deletions...")
    for i in range(n):
        l.delete_left()
        l.delete_right()

@timer
def llistoptimizedtest(n:int):
    print("\n---Optimized linked list test---")
    l = LinkedListOptimized()
    print("Testing insertions...")
    for i in range(n):
        l.insert_left(None)
        l.insert_right(None)
    print(f"{(sys.getsizeof(l) / 1_000_000):.0f}MB of memory used")
    print("Testing deletions...")
    for i in range(n):
        l.delete_left()
        l.delete_right()

@timer
def dllisttest(n:int):
    print("\n---Optimized doubly linked list test---")
    l = DoublyLinkedListOptimized()
    print("Testing insertions...")
    for i in range(n):
        l.insert_left(None)
        l.insert_right(None)
    print(f"{(sys.getsizeof(l) / 1_000_000):.0f}MB of memory used")
    print("Testing deletions...")
    for i in range(n):
        l.delete_left()
        l.delete_right()

def main():
    try:
        nodes = 1
        if nodes < 100000:
            llisttest(nodes)
        llistoptimizedtest(nodes)
        dllisttest(nodes)

        print("\n---Linked list visualization---")
        ll = LinkedList()
        ll.insert_left(1)
        print(ll)
        ll.insert_left(2)
        print(ll)
        ll.insert_right(3)
        print(ll)
        ll.delete_right()
        print(ll)
        ll.delete_left()
        print(ll)
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()