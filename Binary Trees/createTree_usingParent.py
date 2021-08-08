class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
#-----------------------------------------------------------------------------------------    
# creating a tree from a given array

# Given:
# An array whose indexes indicate values of the nodes in the tree
# The values in the array indicate the parent of each of the indices.
# value of root node index is -1

def createNode(parent, i, created, root):
    
    # if node is already created
    if created[i] is not None:
        return
    
    # create a new node
    created[i] = Node(i)
    
    # if i is root, change the root pointer and return
    if parent[i] == -1:
        root[0] = created[i] #root[0] is root of tree
        return 
    
    # if parent is not created, create parent first
    if created[parent[i]] is None:
        createNode(parent, parent[i], created, root)
        
    # find parent pointer
    p = created[parent[i]]
    
    # if this is first child of parent, assign to left
    if p.left is None:
        p.left = created[i]
    else:
        p.right = parent[i]
        
        

def createTree(parent):
    
    # we will create another array say created to keep a track of nodes which have been created.
    # created[i] is NULL if the node isn't created. Else value is pointer to created node
    
    n = len(parent)
    created = [None for i in range(n+1)]
    root = [None]
    
    for i in range(n):
        createNode(parent, i, created, root)
        
    return root[0]
    
    
def in_order(root):
    
    temp = root
    
    if not temp:
        return
    
    in_order(temp.left)
    print(temp.val, end= " ")
    in_order(temp.right)


# Main function
parent = [1, 5, 5, 2, 2, -1, 3]
root = createTree(parent)
in_order(root)
