# Simpler solution to this problem in Java with Time complexity O(n). Here are the steps to follow;

# 1) Create HashMap of all array values as keys and indexes as values. If for any key there are multiple values, then it's stored comma separated.

# 2) Create an empty Stack and insert the first node with index value of -1 as root.

# 3) Iterate over the stack till its not empty, keep popping the elements from it.

# 4) Set currentNode = stack.pop();

# 5) For each popped element get its corresponding values from Hashmap.

# 6) For each value retireved in step 4 do following:

# a) if value if not null and there are multiple values comma separated, then add it as left and right node to the stack, and simultaneously set the reference from the currentNode to the child nodes which you just added to stack.

# b) if value is not null, and there is just a single value then add it to stack as left child and simultaneously update the reference from the currentNode to the leftChild.

# c) if value is null, then continue to the next iteration.

# 7) Go to step 3, until stack is empty.

def createTree(parent):
    
    hash_map = dict()
    for i in range(len(parent)):
        if parent[i] in hash_map:
            hash_map[parent[i]].append(i)
            
        else:
            hash_map[parent[i]] = [i]
            
    print(hash_map)
            
            
    
    # create a stack and add the node with parent value -1 to it, its the root
    curr = hash_map[-1][0]
    print(curr)
    stack = [Node(curr)]
    
    #iterate while stack is not empty
    while stack:
        curr_vals = hash_map[stack[-1].val]
        print(curr_vals)
        current_node = stack.pop()
        
        
        if curr_vals is not None:
            if len(curr_vals) > 1:
                
                right = Node(curr_vals[1])
                stack.append(right)
                current_node.right = right
                
                
                left = Node(curr_vals[0])
                stack.append(left)
                current_node.left = left
                
                
            else:
                left = Node(curr_vals[0])
                stack.append(left)
                current_node.left = left

#-------------------------------------------------------------------------------------

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
