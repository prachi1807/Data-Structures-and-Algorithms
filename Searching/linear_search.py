# Linear Search
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return (i)
    return -1

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 180
print(linear_search(arr,x))
