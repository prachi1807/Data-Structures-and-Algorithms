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

def in_order(root):
    
    temp = root
    
    if not temp:
        return
    
    in_order(temp.left)
    print(temp.val, end= " ")
    in_order(temp.right)
    
    
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

