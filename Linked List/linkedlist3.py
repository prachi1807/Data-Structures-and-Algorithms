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
    
    # Searching in a LL given the value to be searched recursively
    def search_key(self, head, key):
        current = head
        if current == None:
            return False
            
        if current.data == key:
            return True
        
        return self.search_key(current.next,key)
        
    # Search a node given its position from the end (Smort Apporoach)
    def seach_from_end(self, pos_from_end):
        
        # Idea is to take the reference pointer to the "pos_from_end" position from front while main points at head
        # Now move the main and reference till reference reaches the end
        
        ref = self.head
        main = self.head
        
        while pos_from_end!=0:
            ref = ref.next
            pos_from_end-=1
            
        while ref:
            ref = ref.next
            main = main.next
            
        return main.data
           
# Creating Linked List       
linkedlist = LinkedList()

# Inserting 4 elements
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)

# Searching a given value in the LL recursively
print(linkedlist.search_key(linkedlist.head, 1))

# Searching a value given it's position from the end
print(linkedlist.seach_from_end(1))

# Printing the linked list
linkedlist.printll()
