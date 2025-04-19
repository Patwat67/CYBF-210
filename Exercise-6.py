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
        if self.count == 0: # return none if list is empty
            return
        else: # creates temp pointer to track of the node to be deleted, then removes nodes next pointer and updates front pointer
            temp = self.front
            self.front = self.front.next
            temp.next = None
        self.count -= 1 # dec count then null front and tail pointer if list is now empty
        if self.count == 0:
            self.front = self.tail = None

    def delete_right(self):
        if self.count == 0:
            return
        last = self.front # makes a temp pointer "last" to walk the list
        while last.next is not None and last.next.next is not None: # walks list until second to last node
            last = last.next
        last.next = None # seconds second to last nodes next pointer to none
        self.count -= 1 # dec counter then clears front and tail pointers if list is empty
        if self.count == 0:
            self.front = self.tail = None

    def __str__(self): # handles visualizing the llist
        data = []
        temp = self.front # creates temp pointer to walk list
        while temp is not None:
            data.append(str(temp.data)) # converts node data to str and appends it to list
            temp = temp.next
        return ' -> '.join(data) # joins all data and visualizes it with a pointer

# Entrypoint
if __name__ == '__main__':
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