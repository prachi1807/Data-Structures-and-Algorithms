# Here the same Recursive approach is used, except for every value that we get, we store it in the matrix "t"
# So that if we have to calculate the value of the same entity again, we already have it stored


# Memoization
# Using a DP matrix to store the values
t = [[-1 for _ in range(1000)] for _ in range(100)]


def knapsack(wts, val, W, length):
  
    # Base Condition:
    # Smallest valid weight = 0 kg
    # Smallest possible capacity value = 0 
    if length==0 or W==0:    # When either knapsack is full when no elements remain in the wts array
        return 0
        
    if t[length][W]!=-1:
        return t[length][W]
        
    # Logic here is to traverse the array backward
    # See if the weight of a  certain element is less than or equal to the capacity of the knapsack
    
    # Case-1: yes, it is.
    # There are further 2 choices, either take the element or don't
    # So we check profit wise, if the element will yiled greater profit, we'll take it else call the function for the rest of the array
    if wts[length-1]<=W:
        return max((val[length-1] + knapsack(wts, val, W - wts[length-1], length-1)), (knapsack(wts, val, W, length-1)))
    
    # Casse-2: no
    # Then we simple do not need that element and we can move to the remaining array
    else:
        return knapsack(wts, val, W, length-1)
    
    # Choice Diagram



wts = [1,3,5,4]
val = [1,4,7,5]
W = 7   # This is capacity of the knapsack

# function should return maximum profit
print(knapsack(wts, val, W, len(wts)))
