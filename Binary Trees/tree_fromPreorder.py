# Method-1
# Creating a tree from the given preorder traversal in array fromat
# time - O(n^2)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
# constructTreeUtil.preIndex is a static variable of function constructTreeUtil
# static variables are the ones who don't lose their value post a function is over. The value lasts till the entire program runs

# Function to get the value of static variable constructTreeUtil.preIndex
def getPreIndex():
    return constructTreeUtil.preIndex
    
# Function to increment the value of static variable constructTreeUtil.preIndex
def incrementPreIndex():
    constructTreeUtil.preIndex += 1

# Construction of Tree
def constructTreeUtil(preOrder, low, high):
    
    # Corner Case
    if low>high:
        return None
    
    # first node is the root, create it. 
    # Increment preIndex
    root = Node(preOrder[getPreIndex()])
    incrementPreIndex()
    
    # if current subarray has only one element, do not recur
    if low == high:
        return root
        
    # to find the index when index.val > root.val
    r_root = -1
    for i in range(low, high+1):
        if preOrder[i] > root.val:
            r_root = i
            break
    # If no elements are greater than the current root, all elements are left children so assign root appropriately
    if r_root == -1:
        r_root = getPreIndex() + high - low
        
    # Use the index of element found in preorder to divide preorder array in two parts. Left subtree and right subtree
    root.left = constructTreeUtil(preOrder, getPreIndex(), r_root-1)
    root.right = constructTreeUtil(preOrder, r_root, high)
    
    return root
    
    
# Construct Tree initial fucntion
def constructTree(preOrder):
    n = len(preOrder)
    constructTreeUtil.preIndex = 0
    return constructTreeUtil(preOrder, 0, n-1)
    
def post_order(root):
    
    temp = root
    
    if not temp:
        return

    post_order(temp.left)
    post_order(temp.right)
    print(temp.val, end= " ")

# main
preOrder = [10,5,1,7,40,50]
root = constructTree(preOrder)
post_order(root)

    
