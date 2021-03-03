# Implementation of a Doubly Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def printdll(self):
        if self.head == None:
            return
        
        last = None
        print("Forward traversal: ", end= "")
        node = self.head
        while node:
            print(node.data, end=" ")
            last = node
            node = node.next
            
        print("Backward traversal: ",  end="")
        while last:
            print(last.data, end = " ")
            last = last.prev
            
    def add_at_head(self, new_val):
        
        new_node = Node(new_val)
        
        if self.head != None:
            new_node.next = self.head
            self.head.prev = new_node
    
        self.head = new_node
    
    def add_at_end(self, new_val):
        
        if self.head == None:
            self.add_at_head(new_val)
            return 
        
        new_node = Node(new_val)
        last = self.head
        while last.next:
            last = last.next
            
        new_node.prev = last
        last.next = new_node
        
        
    def add_after_node(self, prev_node, new_val):
        
        # i.e either linked list is empty or add at head
        if prev_node == None:
            self.add_at_head(new_val)
            return 
        
        # Previous node exists in the list but is the last node of dll
        if prev_node.next == None:
            self.add_at_end(new_val)
            return
        
        # The previous node is in between
        new_node = Node(new_val)
        
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        new_node.prev = prev_node
        prev_node.next = new_node
            
    def add_before_node(self, next_node, new_val):
        
        if next_node == self.head:
            self.add_at_head(new_val)
            return
        
        if next_node == None:   #Vague case
            return
        
        new_node = Node(new_val)
        
        next_node.prev.next = new_node
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        
            
        
        
dll = DoublyLinkedList()

# adding values at head
dll.add_at_head(4)
dll.add_at_head(3)
dll.add_at_head(2)
dll.add_at_head(1)

# Adding values at end
dll.add_at_end(5)
dll.add_at_end(6)

# Adding after second Node
dll.add_after_node(dll.head.next, 8)
# Adding after None, i.e start
dll.add_after_node(None, 9)

# Adding before the second element
dll.add_before_node(dll.head.next, 10)
# Adding before head
dll.add_before_node(dll.head, 11)

# Print dll
dll.printdll()
        
