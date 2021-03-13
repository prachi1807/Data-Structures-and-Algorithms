# The idea behind merge sort is to break the array into halfs until its length is 1 and then recursively merge the 2 sorted arrays
# Code is oretty self explanatory
# Time complexity is O(nlogn) in all three cases as even  for a sorted array, all the steps will be performed
# Auxilary space = O(n)

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        
        i, j, k = 0, 0 , 0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k] = L[i]
                i += 1
                
            else:
                arr[k] = R[j]
                j += 1
                
            k += 1
            
        while i<len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j<len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [3,4,2,1,5,7]
mergeSort(arr)
print(arr)

