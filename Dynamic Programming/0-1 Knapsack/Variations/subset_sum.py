# Subset Sum Problem reference https://youtu.be/_gPcYovP7wc
# Problem Statement: Given an integer array "nums" and an integer "sums", output where any subset of nums can sum upto to "sum"
# Output: Boolean (True/False)

# eg1: 
# nums = [2,3,7,8,10]
# sum = 11
# output: True

#First Step, Let's make the DP Matrix
# t[length+1][w+1] but here: t[length+1][sums+1] where length = len(nums)

# t = [[0 for _ in range(sums+1)] for _ in range(len(nums)+1)]
# here it will be:
t = [[0 for _ in range(12)] for _ in range(6)]

def subset_sum(nums, sums):
    
    # Initialization of the first row and column according to the base condition
    
    # Here t[0][0] will be True, because when len(nums)==0 and req. sum is 0, that case is possible with a empty subset
    # Remaining row 0 will be False, because  when we want any req sum>0 and the array has no elements, that case isn't possible
    # Remaining of column 0 will be initialised with True because, for a req. sum of 0, given any amount of integers in the nums array, an empty subset is always possible
    
    # Kar lete hai
    for i in range(len(nums)+1):
        for j in range(sums+1):
            if i==0:
                t[i][j] = False
            if j==0:
                t[i][j] = True
    
    # print(t)
    
    # Code Logic
    
    # Referenceing the last 0-1 knapsack code, wts arrays correponds to nums and W corresponds to sums
    # So nums-->i, sums-->j
    for i in range(1, len(nums)+1):
        for j in range(1, sums+1):
            
            # We check if the current number is less than the required sum or not for a particular subproblem
            if nums[i-1]<=j:
                # if yes, previously we took "max" but now that we are dealing with boolean values we'll use the "or" operator
                t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
                
            else:
                # If not, just move on
                t[i][j] = t[i-1][j]
    
    # Latly, you gotta return the value form the last row and last column            
    return t[len(nums)][sums]
    
    
nums = [2,3,7,8,11]
sums = 11
print(subset_sum(nums, sums))
