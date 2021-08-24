# Postorder from given Inorder and Preorder

# Method-1
# No really construction the tree, just output the array basis the given 2
# time - O(n)
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
        to_postorder(inorder, preorder[1:n], n)
        
    if root != n-1:
        to_postorder(inorder[root+1 : n], preorder[root+1:n], n)
        
    print(preorder[0], end=" ")
    
    
inorder = [ 4, 2, 5, 1, 3, 6]
preorder = [ 1, 2, 4, 5, 3, 6]
to_postorder(inorder, preorder, len(inorder))
