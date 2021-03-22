# This is merge sort on a linked list
# The resturned head of the sorted list shows None



# This is merge sort on a linked list
# The resturned head of the sorted list shows None



class Node:
    def __init__(self, data):
        self.data= data
        self.next= None


class LinkedList:
    def __init__(self):
        self.head= None

    # Printing the linked list
    def printll(self, head):
        temp = head
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
            
            
    def getMiddle(self, head):
        if head==None and head.next==None:
            return self.head
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
        
    def merge_lists(self, a, b):
        
        if a==None:
            return b
            
        if b==None:
            return a 
        
        result = Node(0)
        tail = result
        
        while a and b:
            if a.data<b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            
            tail = tail.next 
        
        if not a:
            tail.next = b
        if not b:
            tail.next = a
            
        return result.next
        
    # Merge Sort on a linkedlist
    def merge_sort(self, head):
        
        if head==None or head.next== None:
            return 
        
        mid = self.getMiddle(head)
        nextToMid = mid.next
        
        mid.next = None
        L = self.merge_sort(head)
        R = self.merge_sort(nextToMid)
        
        return self.merge_lists(L,R)
            
            
# Creating Linked List       
linkedlist = LinkedList()

# Inserting 4 elements
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(2)
linkedlist.append(1)
linkedlist.append(5)
linkedlist.append(7)

linkedlist.printll(linkedlist.head)
print()

linkedlist.head = linkedlist.merge_sort(linkedlist.head)
linkedlist.printll(linkedlist.head)

