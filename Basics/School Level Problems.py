# Armstrong Number
def armstrongNumber (n):
    # code here 
    ans = 0
    for num in str(n):
        ans += int(num)**3
    if ans==n:
        return "Yes"
    return "No"
     
# Floyd Triangle - https://practice.geeksforgeeks.org/problems/floyds-triangle1222/1/?category[]=Mathematical&category[]=Mathematical&difficulty[]=-2&page=1&sortBy=accuracy&query=category[]Mathematicaldifficulty[]-2page1sortByaccuracycategory[]Mathematical
# Not Working
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
def reverse_digit(n):
	# Code here
	ans = ""
	while n:
	    ans += str(n%10)
	    n = n//10
  return int(ans)


# 

