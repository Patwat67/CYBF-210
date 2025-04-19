# Patrick Sullivan
# List vs linked list testing
# Tested and works on Python 3.12.1
from time import time

class Node: # Node class
    def __init__(self, data):
        self.data = data # stores node data
        self.next = None # stores pointer to next node

class LinkedList:
    def __init__(self):
        self.front = None # pointer to first node
        self.tail = None # pointer to last node
        self.count = 0 # counter for convenience

    def insert_left(self, data):
        node = Node(data) # creates a new node obj with supplied data
        if self.count == 0: # if ll is empty, set both pointers to it
            self.front = self.tail = node
        else: # else, set new nodes next to current front pointer, then update front pointer
            node.next = self.front
            self.front = node
        self.count += 1 # increment counter to reflect new node

    def insert_right(self, data):
        node = Node(data)
        if self.count == 0:
            self.front = self.tail = node
        else: # else, set tails next to new node, before updating new node
            self.tail.next = node
            self.tail = node
        self.count += 1

    def delete_left(self):
        if self.count == 0:  # early return if list is empty
            return
        temp = self.front  # save the front node
        self.front = self.front.next  # update the front pointer
        temp.next = None  # clear the next pointer
        self.count -= 1
        if self.count == 0:  # if list is empty now, clear tail as well
            self.tail = None

    def delete_right(self):
        if self.count == 0:
            return
        if self.count == 1:
            self.front = self.tail = None
        else:
            # Traversal would still happen to get the second-to-last node
            second_last = self.front
            while second_last.next != self.tail:
                second_last = second_last.next
            second_last.next = None
            self.tail = second_last
        self.count -= 1

    def insert_at(self, index, data):
        if index < 0 or index > self.count: # check if index is out of range
            raise IndexError("Index out of range")
        node = Node(data) # create a new node with given data
        if index == 0:
            self.insert_left(data)
        elif index == self.count:
            self.insert_right(data)
        else:
            temp = self.front
            for _ in range(index - 1): # walk to node before target index
                temp = temp.next
            node.next = temp.next # set new node's next to current next
            temp.next = node # update previous node's next to new node
            self.count += 1

    def delete_at(self, index):
        if index < 0 or index >= self.count: # check if index is out of range
            raise IndexError("Index out of range")
        if index == 0:
            self.delete_left()
        elif index == self.count - 1:
            self.delete_right()
        else:
            temp = self.front
            for _ in range(index - 1): # walk to node before target
                temp = temp.next
            to_delete = temp.next
            temp.next = to_delete.next # skip over the deleted node
            to_delete.next = None
            self.count -= 1

    def delete_value(self, value):
        if self.count == 0:
            return
        if self.front.data == value: # if value is at the front
            self.delete_left()
            return
        temp = self.front
        while temp.next is not None:
            if temp.next.data == value: # match found
                to_delete = temp.next
                temp.next = to_delete.next
                if to_delete == self.tail: # if tail was deleted, update tail
                    self.tail = temp
                to_delete.next = None
                self.count -= 1
                return
            temp = temp.next

    def get_at(self, index):
        if index < 0 or index >= self.count: # check if index is out of range
            raise IndexError("Index out of range")
        temp = self.front # start from front
        for _ in range(index): # walk list to index
            temp = temp.next
        return temp.data # return node's data at that index

    def get_left(self):
        if self.count == 0: # return None if list is empty
            return None
        return self.front.data # return data at front node

    def get_right(self):
        if self.count == 0: # return None if list is empty
            return None
        return self.tail.data # return data at tail node

    def contains(self, value):
        temp = self.front # walk through the list
        while temp is not None:
            if temp.data == value:
                return True # match found
            temp = temp.next
        return False # no match found

    def index_of(self, value):
        temp = self.front # start from front
        index = 0
        while temp is not None:
            if temp.data == value:
                return index # return index of first match
            temp = temp.next
            index += 1
        return -1 # return -1 if not found

    def is_empty(self):
        return self.count == 0 # returns True if list has no elements

    def clear(self):
        self.front = self.tail = None # reset pointers
        self.count = 0 # reset count to zero

    def length(self):
        return self.count # return current node count

    def __str__(self): # handles visualizing the llist
        data = []
        temp = self.front # creates temp pointer to walk list
        while temp is not None:
            data.append(str(temp.data)) # converts node data to str and appends it to list
            temp = temp.next
        return ' -> '.join(data) # joins all data and visualizes it with a pointer

def list_test(l: list, n: int):
    print(f"Initializing list with {n} elements...")
    s = time()
    for i in range(n):
        l.append(i)
    print(f"Initialized list in {(time() - s):.2f} seconds!")
    print("---")

    print(f"Indexing list with {n} elements...")
    s = time()
    for i in range(n):
        l[i] = i
    print(f"Indexed list in {(time() - s):.2f} seconds!")
    print("---")

    print(f"Searching list with {n} elements...")
    s = time()
    for i in range(n):
        if i in l:
            l.index(i)
    print(f"Searched list in {(time() - s):.2f} seconds!")

def linked_list_test(l: LinkedList, n: int):
    print(f"Initializing linked list with {n} elements...")
    s = time()
    for i in range(n):
        l.insert_right(i)
    print(f"Initialized linked list in {(time() - s):.2f} seconds!")
    print("---")

    print(f"Indexing linked list with {n} elements...")
    s = time()
    for i in range(n):
        l.get_at(i)  # Linked list indexing
    print(f"Indexed linked list in {(time() - s):.2f} seconds!")
    print("---")

    print(f"Searching linked list with {n} elements...")
    s = time()
    for i in range(n):
        if l.contains(i):
            l.index_of(i)
    print(f"Searched linked list in {(time() - s):.2f} seconds!")


if __name__ == "__main__":
    l = []
    ll = LinkedList()
    n = 10000 # number of elements to add to each list

    list_test(l, n)
    print("\n-----------------------\n")
    linked_list_test(ll, n)
    print('\nDone!')


