# *** Important ***
# To caclulate mid, always use mid = low + (high-low)//2 to avoid any overflow
# Now what exactly is the overflow?
# --> The overflow occurs when the size of the variable(int) is taken into consideration.
# low+high can overflow to a value outside the permissible int range and can lead to a roolever of iteger values starting from 0 taken unsigned
# to avoid that, (high-low) will never cause the overflow as no value is added to high.
# Refer : https://stackoverflow.com/questions/6735259/calculating-mid-in-binary-search


# Recursive Binary search, O(logn) time
# Auxilary space = O(n) i.e recursive call stack space
def binary_search(arr,x, start, end):
    
    if start<=end:
        mid = (start+end)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr, x, start, mid)
        else:
            return binary_search(arr, x, mid+1, end)
    else:
        return -1
    
# Iterative Binary search, O(logn)
# Auxilary space = O(1)
def binary_search_1(arr, x, start, end):
    
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            end = mid
        else:
            start = mid+1
    
    return -1        
    

arr = [10, 20, 30, 50, 60, 80, 100, 110, 130, 170]
x = 110

print(binary_search(arr, x, 0, len(arr)-1))
print(binary_search_1(arr, x, 0, len(arr)-1))


