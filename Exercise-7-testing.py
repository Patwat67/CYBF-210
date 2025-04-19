from time import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.front = None
        self.tail = None
        self.count = 0

    def insert_right(self, data):
        node = Node(data)
        if self.count == 0:
            self.front = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def delete_right(self):
        if self.count == 0:
            return
        if self.count == 1:
            self.front = self.tail = None
        else:
            second_last = self.front
            while second_last.next != self.tail:
                second_last = second_last.next
            second_last.next = None
            self.tail = second_last
        self.count -= 1

    def get_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        temp = self.front
        for _ in range(index):
            temp = temp.next
        return temp.data

    def contains(self, value):
        temp = self.front
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def index_of(self, value):
        temp = self.front
        index = 0
        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
        return -1

    def is_empty(self):
        return self.count == 0

    def length(self):
        return self.count

    def __str__(self):
        data = []
        temp = self.front
        while temp:
            data.append(str(temp.data))
            temp = temp.next
        return ' -> '.join(data)

def list_test(l, n):
    start = time()
    for i in range(n):
        l.append(i)
    print(f"List initialized in {(time() - start):.2f} seconds!")

    start = time()
    for i in range(n):
        l[i] = i
    print(f"List indexed in {(time() - start):.2f} seconds!")

    start = time()
    for i in range(n):
        if i in l:
            l.index(i)
    print(f"List searched in {(time() - start):.2f} seconds!")

def linked_list_test(l, n):
    start = time()
    for i in range(n):
        l.insert_right(i)
    print(f"Linked list initialized in {(time() - start):.2f} seconds!")

    start = time()
    for i in range(n):
        l.get_at(i)
    print(f"Linked list indexed in {(time() - start):.2f} seconds!")

    start = time()
    for i in range(n):
        if l.contains(i):
            l.index_of(i)
    print(f"Linked list searched in {(time() - start):.2f} seconds!")

l = []
ll = LinkedList()
n = 10000

list_test(l, n)
print("\n-----------------------\n")
linked_list_test(ll, n)
print('\nDone!')
