# Noah Preston , CSC-231-001

class Node: # Node class for storing data and referencing nodes
    
    def __init__(self, data = None): 
        self.data = data # Initialize node
        self.next = None # Initialize the next node as none

    def __str__(self):
        return str(self.data)  # Return data as a string

class LinkedList: # LinkedList class for management of nodes

    def __init__(self): 
        self.head = None # First node of linked list
        self.tail = None # First node of linked list 
        self.size = 0 # Size of the linked list 

    def is_empty(self): # Returns True if list is empty, False if not
        return self.head is None

    def add(self, item): # Adding a new item at the head of the linked list 
        new_node = Node(item) # Create a new node 
        new_node.next = self.head # Link new node to previous node
        self.head = new_node # Update head to the new node
        if self.tail is None: # If list is empty then a new node is added to tail
            self.tail = new_node
        self.size += 1 # Increment

    def append(self, item): # Append a new node at the end of the linked list
        new_node = Node(item) # Create a new node
        if self.is_empty(): # If list is empty then new node is set to both head and tail
            self.head = self.tail = new_node
        else: 
            self.tail.next = new_node # Link the old tail to the new node
            self.tail = new_node # Update the tai to a new node
        self.size += 1 # Increment

    def pop(self, pos = None): # Remove and return an item from the linked list at the given position or last item 
        if self.is_empty():
            raise IndexError("Pop from an empty list.")
        if pos is None:
            pos = self.size - 1
        if not isinstance(pos, int) or pos < 0 or pos >= self.size:
            raise TypeError("Position must be an integer in an allowed range of numbers.")
        
        current = self.head
        if pos == 0:
            data = self.head.data
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = None
            for _ in range(pos):
                prev = current
                current = current.next
            data = current.data
            prev.next = current.next
            if current == self.tail:
                self.tail = prev
        self.size -= 1
        return data
        
    def search(self, item): # Search for an item in the linked list and return True if found, False if not
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item): # Remove the node from the linked list 
        current = self.head
        prev = None
        while current is not None:
            if current.data == item:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current == self.tail:
                    self.tail = prev
                self.size -= 1
                return
            prev = current
            current = current.next
        raise ValueError("Item is not found in list.")

    def __iter__(self): # Iterator for the linked list 
        current = self.head
        while current is not None:
            yield current
            current = current.next

   
