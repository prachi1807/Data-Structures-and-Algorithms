# Postorder from given Inorder and Preorder

# Method-1
# No really constructing the tree, just output the array basis the given 2
# time - O(n^2), O(n) for traversing the array and O(n) for the search that's inside this traversal.
# space - recursion stack space

def search(arr, val, n):
    
    for i in range(n):
        if arr[i] == val:
            return i
            
    return -1

def to_postorder(inorder, preorder, n):
    
    # first element in preorder is root, search uska index in inorder
    root = search(inorder, preorder[0], n)
    
    # if left subtree is not empty
    if root != 0:
        to_postorder(inorder, preorder[1:n], root)
        
    if root != n-1:
        to_postorder(inorder[root+1 : n], preorder[root+1:n], n-root-1)
        
    print(preorder[0], end=" ")
    
    
inorder = [ 4, 2, 5, 1, 3, 6]
preorder = [ 1, 2, 4, 5, 3, 6]
to_postorder(inorder, preorder, len(inorder))



# Method-2
# using a hashmap to store indices of inorder and then recursively traverse to find preorder indices

# time - O(n^2), O(n) for traversing the array and O(n) for the search that's inside this traversal.
# space - recursion stack space

def to_postorder(inorder, preorder, inStr, inEnd):
    
    global hashmap, preIndex
    
    if inStr>inEnd:
        return
    
    # find index of first element in postorder in inorder
    inIndex = hashmap[preorder[preIndex]]
    preIndex += 1
    
    
    # recursively search in left subarray
    to_postorder(inorder, preorder, inStr, inIndex-1)
        
    # recursively search right subarray
    to_postorder(inorder, preorder, inIndex+1, inEnd)
        
    print(inorder[inIndex], end=" ")
    
    
inorder = [ 4, 2, 5, 1, 3, 6]
preorder = [ 1, 2, 4, 5, 3, 6]
hashmap = dict()
preIndex = 0
for i in range(len(inorder)):
    hashmap[inorder[i]] = i

to_postorder(inorder, preorder, 0, len(inorder)-1)


