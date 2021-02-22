# Some additional linked list functions

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None


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

    
# Creating Linked List       
linkedlist = LinkedList()

# Inserting 4 elements
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)

# Printing the linked list
linkedlist.printll()