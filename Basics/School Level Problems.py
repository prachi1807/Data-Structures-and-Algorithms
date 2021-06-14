# Armstrong Number
# Time - O(1)
# Space = O(1)
def armstrongNumber (n):
    # code here 
    ans = 0
    for num in str(n):
        ans += int(num)**3
    if ans==n:
        return "Yes"
    return "No"
     
# Floyd Triangle - https://practice.geeksforgeeks.org/problems/floyds-triangle1222/1/?category[]=Mathematical&category[]=Mathematical&difficulty[]=-2&page=1&sortBy=accuracy&query=category[]Mathematicaldifficulty[]-2page1sortByaccuracycategory[]Mathematical
# Not Working on GFG
# Time - O(n^2)
# Space = O(1)
def printFloydTriangle(N):
    #code here 
    num = 1
    for i in range(N):
        for j in range(i+1):
            print(num, end = " ")
            num += 1    
        print("\n")
        
        
# Reverse Digits
# Method 1 (lame)
def reverse_digit(n):
	# Code here
	return int(str(n)[::-1])

# Method 2 - Seperating digits
# Time - O(log(n))
# Space = O(1)
def reverse_digit(n):
	# Code here
	ans = ""
	while n:
	    ans += str(n%10)
	    n = n//10
  	return int(ans)


# Average in a stream (Running Average)
# Time - O(n)
# Space = O(1)
def streamAvg(arr, n):
	# code here
	ans = list()
	sum_nums = 0
	for i in range(len(arr)):
	    sum_nums += arr[i]
	    ans.append(sum_nums/(i+1))
	return ans
    
arr = [10, 20, 30, 40, 50]
print(streamAvg(arr, 5))


# Sum Palindrome
# Time - ?
# Space = O(1)
def isPalindrome(num):
    return num == int(str(num)[::-1])
    
def reverse(num):
    return int(str(num)[::-1])
    
    
def isSumPalindrome (n):
    
    if isPalindrome(n):
        return n
            
    count = 0
    while count!=5:
        count += 1
        new = reverse(n)
        n += new
        if isPalindrome(n):
            return n
        
    return -1
    
print(isSumPalindrome(121))
