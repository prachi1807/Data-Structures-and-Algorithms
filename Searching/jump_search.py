import math

# The idea here is to use lesser time than linear search by jumping certain amount steps
# Applicable only when data is sorted
# The step/block is to be chosen in such a way that it is the most optimum step size, the best choice here would be the square root of the length of the array
# We find a range between which the needed value lies and then run a linear search on that part of the array
# Time Complexity = O(root(n))
# Auxilary space = O(1)

def jump_search(arr, x):
    i = 0
    block = int(math.sqrt(len(arr)))
    j = block
    while j!=len(arr):
        if arr[j] > x:
            break
        else:
            i = j
            j += block
    
    while i<=j:
        if arr[i]==x:
            return i
        i += 1
        
    return -1

arr = [0, 1, 2, 3, 5, 8, 10, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 610
print(jump_search(arr, x))


