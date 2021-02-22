# Basic linked list implementation using functions

class LinkedList:
    def __init__(self):
        self.head= None
        
    # Printing the linked list
    def printll(self):
        temp = self.head
        while (temp):
            print(temp.data, end = " ")
            temp = temp.next
        
    # Inserting a node at the end    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head==None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            
            temp.next = new_node
            
    # Inserting at the beginning
    def insertbeg(self, new_data):
        
        new_node = Node(new_data)
        
        new_node.next = self.head
        self.head = new_node
        
    
    # Inserting in between
    def insertbet(self, prev_node, new_data):
        
        new_node = Node(new_data)
        
        new_node.next = prev_node.next
        prev_node.next= new_node
        
    # Deleting anode given the value to be deleted
    def delnode(self, key):
        temp = self.head
        
        # Check if the node to be deleted is the first node i.e. head
        if temp is not None and temp.data==key:
            self.head = temp.next
            temp.next = None     #Breaking the link
            return 
        
        while temp is not None:
            if temp.data==key:
                break
            prev = temp
            temp = temp.next
            
        # Check if the element was found or not
        if temp==None:      # Meaning that temp reached the last node but the key wasn't found
            return
        
        # Coming here means that the key is found somewhere in the linked list 
        # and we have reference of the key in temp and its previous value in prev
        prev.next = temp.next
        temp.next = None
        
        
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
    
# Creating Linked List       
linkedlist = LinkedList()

# Inserting 4 elements
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)

# Inserting 5 at the beginning
linkedlist.insertbeg(5)

# Inserting 18 after the second element
linkedlist.insertbet(linkedlist.head.next, 18)

# Deleting anelement from the middle of the linkedlist
linkedlist.delnode(18)
# Deleting element from the start i.e the head referenced element
linkedlist.delnode(5)

linkedlist.printll()

