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
        
    # Takes the pointer of the node to be deleted as the parameter
    def delete_node(self, del_node):
        
        # Base case
        if self.head is None or del_node is None:
            return
        
        # If the node to be deleted is the head
        if del_node == self.head:
            
            # If the head of the DLL is to  be deleted and only 1 node is present in DLL
            if del_node.next == None:
                self.head = None
                return
                    
            # In any other case, DLL has more than one element
            self.head = del_node.next
            self.head.prev = None
            return
        
        # Deletion of the last node
        if del_node.next == None:
            del_node.prev.next = None
            del_node.prev = None    # Not really mandatory
            return
        
        # Deletion of a node in the middle
        del_node.prev.next = del_node.next
        del_node.next.prev = del_node.prev
        del_node = None
        
            
dll = DoublyLinkedList()

adding values at head
dll.add_at_head(4)
dll.add_at_head(3)
dll.add_at_head(2)
dll.add_at_head(1)

# Deleting nodes from DLL
# Delete head Node
dll.delete_node(dll.head)

# Delete middle Node
dll.delete_node(dll.head.next)

# Delete last Node
dll.delete_node(dll.head.next)

# Print dll
dll.printdll()
