'''
Check if a given Binary Tree is a Heap

Given a binary tree, check if it has heap property or not, Binary tree needs to fulfil the 
following two conditions for being a heap:

1. It should be a complete tree (i.e. all levels except the last should be full).
2. Every node’s value should be greater than or equal to its child node (considering max-heap).
Sol: Start BFS search. For each node check following:
    A) both child should be small the parent
    B) Complete Tree consitency status track

'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        


main = node(97)
main.left = node(46)
main.right = node(37)
main.left.left = node(12)
main.left.right = node(3)
#main.left.left.left = node(6)
main.left.left.right = node(9)
main.right.left = node(7)
main.right.right = node(31)    
queue = [main]
status = False # Heap status
cn = 3 # No. of child in previous run
ss = [] # Search sequence
while queue:
    root = queue.pop(0)        
    if root.left is not None and root.right is not None:
        if root.left.data < root.data and root.right.data < root.data:
            status = True
            queue.extend([root.left,root.right])
        else:
            status = False
            break
        cc = 2
        
    elif root.left is not None and root.right is None:
        if root.left.data < root.data:
            status = True
            queue.append(root.left)
        else:
            status = False
            break
        cc = 1
    elif root.left is None and root.right is not None:
        status = False
        break
    elif root.left is None and root.right is None:
        status = True
        cc = 0
    if cc <= cn:
        status = True
    else:
        status = False
        break
    cn = cc
print(f"Heap status for given BT is {status}")
      
    
    