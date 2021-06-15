# Maximum Cuts 
# Complete the function maximum_Cuts() which takes n as input parameter and returns the maximum number of pieces that can be formed by making n cuts.

# Method-1 - Recursive calling
# Time - exponential
# Space - Stack space
def maximum_Cuts(n):
    if n==0:
        return 1
    return n + maximum_Cuts(n-1)

print(maximum_Cuts(5))

# Method-2 - Deriving Formula out of the above equation
# Since, f(n) = n + f(n-1) (from Above)
# therefore f(n) = n + n-1 + n-2 + ....... + 2 + 1 + f(0)

# Time - O(1)
# Space - O(1)
def maximum_Cuts(n):
   return (n*(n+1)//2)+1
  
print(maximum_Cuts(5))

# Number of Paths: https://practice.geeksforgeeks.org/problems/number-of-paths0926/1/?category[]=Mathematical&category[]=Mathematical&difficulty[]=-1&difficulty[]=0&page=1&sortBy=accuracy&query=category[]Mathematicaldifficulty[]-1difficulty[]0page1sortByaccuracycategory[]Mathematical 
# Best way to go about would be recursion
# Base Case - If either number of rows or columns is 1, paths available are 1

# Time - exponential
# Stack space required.

def numberOfPaths(n,m):
    if n==1 or m==1:
        return 1
    return numberOfPaths(n-1, m) + numberOfPaths(n, m-1)

print(numberOfPaths(2,6))



# Check if number is fibonacci

# Method 1

# Time - O(N) for a bigger number, O(1) if number is small
# Space - O(1)

def checkFibonacci(N):
    a = 0
    b = 1
    while True:
        c = a+b
        a = b
        b = c
        if b==N:
            return True
        elif b>N:
            return False
        
print(checkFibonacci(56))

# Method -2 (Using formula)
# A number "n" is said to be a fibonacci number if and only if either of (5*n2 + 4) or (5*n2 – 4) is a perfect square (weird)




