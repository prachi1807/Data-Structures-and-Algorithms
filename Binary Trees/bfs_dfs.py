class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
# BFS traversal on a tree (also called, level order traversal)
# time - O(n), each node is traversed exactly once
# uses extra space O(w), where w is width of tree (for queue)

def bfs_traversal(root):
    
    if not root:
        return 
    
    queue = [root]
    
    while len(queue) > 0:
        print(queue[0].val, end=" ")
        node = queue.pop(0)
        
        if node.left is not None:
            queue.append(node.left)
            
        if node.right is not None:
            queue.append(node.right)
            
            
 # DFS traversal on a tree 
# time - O(n), each node is traversed exactly once
# uses extra space O(h), where h is height of tree (recursive space or stack)

# 3 types - inorder, preorder and postorder

# recursive
def in_order(root):
    
    temp = root
    
    if not temp:
        return
    
    in_order(temp.left)
    print(temp.val, end= " ")
    in_order(temp.right)

# iterative
def inorder(root):
    
    # we will be using a stack
    current = root
    stack = []
    
    while True:
        
        if current is not None:
            stack.append(current)
            current = current.left  #takes to left extreme of present root
            
        elif stack:
            current = stack.pop()
            print(current.val, end=" ")
            
            # now point to left half
            current = current.right
            
        else:
            break
            
            
# inorder without extra space
# Morris traversals 
# time - O(n)

def morris_traversal(root):
    
    current = root
    
    while current is not None:
        
        if current.left is None:
            yield current.val
            current = current.right
            
        else:
            
            # let's find inorder predecessor of current
            pre = current.left
            
            while pre.right is not None and pre.right is not current:
                pre = pre.right
                
            if pre.right is None:
                
                # make current as right child of its inorder predecessor
                pre.right = current
                current = current.left
            
            else:
                
                # Revert the changes made in the 'if' part to restore the original tree. i.e., fix the right child of predecessor
                pre.right = None
                yield current.val
                current = current.right
            

    
def pre_order(root):
    
    temp = root
    
    if not temp:
        return
    
    
    print(temp.val, end= " ")
    pre_order(temp.left)
    pre_order(temp.right)
    

def post_order(root):
    
    temp = root
    
    if not temp:
        return
    
    
    post_order(temp.left)
    post_order(temp.right)
    print(temp.val, end= " ")


    
# Creating a tree manually
root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.left.right = Node(20)

root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

# Level order traverse
bfs_traversal(root)
print()

# depth traversals
in_order(root)
print()
pre_order(root)
print()
post_order(root)


for i in morris_traversal(root):
    print(i, end = " ")
