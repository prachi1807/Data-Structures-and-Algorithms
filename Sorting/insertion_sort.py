# Simple idea here is to check if each element in the non-sorted section of the array is smaller than the end of sorted section
# If yes,  insert that value at a proper place in the sorted array
# O(n^2) time
# Suitable only when array is small or when the array is almost sorted


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while arr[j]>key and j>=0:
            arr[j+1] = arr[j]
            j = j-1
            
        arr[j+1] = key
            
    return arr

arr = [64, 34, 25, 12, 22, 11, 90] 
print(insertion_sort(arr))


#**********************************************************************************************************************

# Insertion sort on a LL
# Insertion sort on a LL makes use of an additional list and does not modify the LL in place
def insertion_sort(self):
        if self.head == None:
            return
        
        start = Node(0)
        current = self.head
        
        while current:
            dummy = start
            while dummy.next and current.data > dummy.next.data :
                dummy = dummy.next
            
            next_node = current.next
            current.next = dummy.next
            dummy.next = current
            
            current = next_node
            
        self.head = start.next
