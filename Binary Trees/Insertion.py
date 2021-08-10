class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

# Level Order Insertion

# What is this?
# --> Level order insertion is when you are given a tree and when you come across the first elelemnt who doesn't have either a 
# left child or right child, you insert the new node there

# Given - a tree with one empty spot and a new val to be inserted. 

# NOTE: no AVL tree rules are followed here.


# print the values in the tree, Inorder traversal
def inorder(root):
    
    temp = root
    
    if not temp:
        return
    
    inorder(temp.left)
    print(temp.val, end= " ")
    inorder(temp.right)
    
    
def insert(root, val):
    
    temp = root
    if not temp:
        root = Node(val)
        return root
        
    queue = []
    queue.append(temp)
    
    # doing an level order traveral till we find an empty spot
    while queue:
        temp = queue[0]
        queue.pop(0)
        
        if not temp.left:
            temp.left = Node(val)
            return root
        else:
            queue.append(temp.left)
            
        
        if not temp.right:
            temp.right = Node(val)
            return root
        else:
            queue.append(temp.right)
            
            
    
    
    
# Creating a tree manually
root = Node(10)
root.left = Node(11)
root.left.left = Node(7)

root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

# so any new element has to ideally go to root.left.right

# we'll first print this
root = insert(root, 19)
inorder(root)

    
