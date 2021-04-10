# Equal Sum Partition

# PS: Given an arrays "nums", return whether or not the array can be broken into 2 subsets such that the sum of both the partitions is equal

# eg:
# nums = [1,5,11,5]
# o/p = True
# because [1,5,5] = 11 and [11] = 11

# *********************NOTE**********************
# If the sum of the elements in "nums" is even, then and only then is an equal sum partition possible

t = [[0 for _ in range(12)] for _ in range(5)]
def subset_sum(nums, sums):
    
    # Initialise
    for i in range(len(nums)+1):
        for j in range(sums+1):
            if i==0:
                t[i][j] = False
            if j==0:
                t[i][j] = True
    
    for i in range(1, len(nums)+1):
        for j in range(1, sums+1):
            if nums[i-1]<=j:
                t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
                
            else:
                t[i][j] = t[i-1][j]
                
    return t[len(nums)][sums]
    


def equal_sum_parti(nums):
    
    # *********************NOTE**********************
    # If the sum of the elements in "nums" is even, then and only then is an equal sum partition possible
    sum_arr = sum(nums)
    if sum_arr%2!=0:
        return False
        
    # Now to  problem reduces to something very very simple
    # We just have to find one subset whose sum==sum_arr//2, automatically the remaining partitions value is sum_arr//2
    # Reduced to subset sum problem now
    
    return subset_sum(nums, sum_arr//2)
    


nums = [1,5,11,5]
print(equal_sum_parti(nums))
