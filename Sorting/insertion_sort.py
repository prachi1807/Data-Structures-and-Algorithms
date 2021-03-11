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
