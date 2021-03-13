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
            
            
    def getMiddle(self, headRef):
        if headRef==None:
            return
        
        slow = headRef
        fast = headRef
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
        
    def merge_lists(self, a, b):
        
        result = None
        
        if a==None:
            return b
        if b==None:
            return a
        
        if a.data<b.data:
            result = a
            result.next = self.merge_lists(a.next, b)
        else:
            result = b
            result.next = self.merge_lists(b.next, a)
            
        return result
            
            
    # Merge Sort on a linkedlist
    def merge_sort(self, headRef):
        
        if self.head==None or self.head.next== None:
            return 
        
        mid = self.getMiddle(headRef)
        nextToMid = mid.next
        
        mid.next = None
        L = self.merge_sort(headRef)
        R = self.merge_sort(nextToMid)
        
        sorted_list = self.merge_lists(L,R)
        return sorted_list
            
            
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
print(linkedlist.head)
print()

linkedlist.printll(linkedlist.merge_sort(linkedlist.head))
