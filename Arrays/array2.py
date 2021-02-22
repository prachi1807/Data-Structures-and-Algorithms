# import array as arr

# def rotate(a,d,n):  # Complexity= O(d*n)
#     for i in range(d):
#         temp=a[0]
#         for j in range(n-1):
#             a[j]=a[j+1]
#         a[n-1]= temp
#     return a

# def reverse(a, start, end):
#     while start<end:
#         temp=a[start]
#         a[start]=a[end]
#         a[end]=temp
#         start=start+1
#         end=end-1

# def rotate1(a,d,n): # Complexity= O(n)
#     if d==0:
#         return a
#     d=d%n
#     reverse(a,0,d-1)
#     reverse(a,d,n-1)
#     reverse(a,0,n-1)
#     return a


# a= arr.array('i', [1,2,3,4,5])
# print(rotate(a,2,5))

# a= arr.array('i', [1,2,3,4,5])
# print(rotate1(a,2,5))

nums= [3,2,3]
target=6
temp= nums[0]
for i in range(len(nums)):
    if len(nums)==2:
        if nums[0]+nums[1]==target:
            print([0,1])
            break
        else:
            print("Blank")
    if nums[i]>=target and nums[i+1] is not None:
        temp=nums[i+1]
    diff= target-temp
    print(diff)
    print(temp)
    print(nums[nums.index(temp)+1:])
    if diff in nums[nums.index(temp)+1:]:
        print(nums.index(diff))
        print([nums.index(temp), nums.index(diff, nums.index(temp)+1, len(nums))])
        break
    else:
        temp=nums[i+1]

