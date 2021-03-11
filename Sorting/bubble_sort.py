# The idea here is to compare each element with it's corresponding next element to find the greater one
# Bubble sort puts the largest element at the end of the array after every iteration
# Time Complexity = O(n^2) and Auxilary Space = O(1)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr


arr = [64, 34, 25, 12, 22, 11, 90] 
print(bubble_sort(arr))

# *********************************************************************************************
# Here is an optimised approach to the above bubble sort
# In a regular bubble sort, the loop conditions keep on checking for heavier element even if the array is sorted (i.e time = O(n^2))
# But by using an extra flag, we keep see, if in a particular iteration the values are swapped or not.
# If the values are not swapped, that means that the array is alreay sorted and we can break out of the main loop
# Worst case time complexity = O(n^2)
# Besat case time = O(n) -- completely sorted array

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if swapped == False:
            break
            
                
    return arr


arr = [64, 34, 25, 12, 22, 11, 90] 
print(bubble_sort(arr))
