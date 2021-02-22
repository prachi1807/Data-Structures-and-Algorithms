#This is the basic implementation of a linked list using python

class LinkedList:
    def __init__(self):
        self.head= None
        
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
# Initializing the linked list       
ll = LinkedList()

# Making the first node and pointing the  head of LinkedList to it
ll.head = Node(1)

# Making the next 2 nodes
second = Node(2)
third = Node(3)

# Connecting the second and third node to the LinkedList
ll.head.next = second
second.next=third

# inserting at the start
fourth = Node(4)
fourth.next = ll.head
ll.head= fourth

# Insert in between
fifth= Node(5)
fifth.next = second.next
second.next= fifth

# Insert at the end
sixth= Node(6)
start = ll.head
while start.next:
    start= start.next
    
start.next = sixth


# Printing the linked list
temp = ll.head
while (temp):
    print(temp.data, end = " ")
    temp = temp.next
    
