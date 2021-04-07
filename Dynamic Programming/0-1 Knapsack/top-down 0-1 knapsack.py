# In the top down approach, we completely omit the recursive calls
# Every value is stored in the DP matrix and the answer is the last value of the DP Matrix

# We make a DP Matrix with one additional row and column for initialization
# Rows ---> len(val)
# Columns ---> W
t = [[-1 for _ in range(3)] for _ in range(4)]


def knapsack(wts, val, W, length):

    # Base Condition:
    # Smallest valid weight = 0 kg
    # Smallest possible capacity value = 0 
    
    # Corresponding to the base condition, we have to return 0 when either knapsack is full(W=0) or when all elements of val are over
    for i in range(length+1):
        for j in range(W+1):
            if i==0 or j==0:
                t[i][j] = 0
                
    
        
    if t[length][W]!=-1:
        return t[length][W]
        
    # Logic here is to traverse the array backward
    # See if the weight of a certain element is less than or equal to the capacity of the knapsack
    
    for i in range(1, length+1):
        for j in range(1, W+1):
    
    # Case-1: yes, it is.
    # There are further 2 choices, either take the element or don't
    # So we check profit wise, if the element will yiled greater profit, we'll take it else call the function for the rest of the array
    
    # if wts[length-1]<=W:
    #     t[length][W] = max((val[length-1] + knapsack(wts, val, W - wts[length-1], length-1)), (knapsack(wts, val, W, length-1)))
    #     return max((val[length-1] + knapsack(wts, val, W - wts[length-1], length-1)), (knapsack(wts, val, W, length-1)))
            
            if wts[i-1]<=j:
                t[i][j] = max((val[i-1] + t[i-1][j-wts[i-1]]), t[i-1][j])
            
    # Casse-2: no
    # Then we simple do not need that element and we can move to the remaining array
    
    # else:
    #     t[length][W] = knapsack(wts, val, W, length-1)
    #     return knapsack(wts, val, W, length-1)
    
            else:
                t[i][j] = t[i-1][j]
    
    for i in range(1, length+1):
        for j in range(1, W+1):
            if wts[i-1]<=j:
                t[i][j] = max((val[i-1] + t[i-1][j-wts[i-1]]), t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
        
    # Return the value from the intersection of last row and column
    return t[length][W]



wts = [1, 1, 1]
val = [10, 20, 30]
W = 2   # This is capacity of the knapsack

# function should return maximum profit
print(knapsack(wts, val, W, len(wts)))
