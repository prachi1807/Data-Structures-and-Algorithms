# The idea here is to have two sections of the array, one that is sorted and the other that isn't (Intially the whole array is unsorted)
# We pick the smallest element from the unsorted array and add it in the sorted array
# Time Complexity = O(n^2)
# Auxilary space = O(1)
# Visulaization :https://www.geeksforgeeks.org/selection-sort/

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

arr = [64, 25, 12, 22, 11, 5, 33, 56] 
print(selection_sort(arr))
