# Linear Search
def linear_search(arr,x):
    # Worst case time complexity = O(n)
    for i in range(len(arr)):
        if arr[i] == x:
            return (i)
    return -1
    
def linear_search_1(arr,x):
    # Worst case time complexity = O(n/2)
    # Uses 2 pointers, one from start and the other from the end
    # Takes half as much of the time
    
    left = 0
    right = len(arr)-1
    pos = -1
    while left<right:
        if arr[left] == x:
            return left
        
        if arr[right] == x:
            return right
            
        left += 1
        right -= 1
        
    return -1

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 130
print(linear_search(arr,x))
print(linear_search_1(arr,x))
