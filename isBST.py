'''
Problem:
Check if a Binary Tree is BST or not
Given the root of a binary tree. Check whether it is a Binary Search Tree or not. 

A Binary Search Tree (BST) is a node-based binary tree data structure with the following properties. 
All keys in the left subtree are smaller than the root and all keys in the right subtree are greater.
Both the left and right subtrees must also be binary search trees.
Each key must be distinct.
'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isValid(node,min,max,dict1):
    if node is None:
        return dict1
    else:
        print(f'Checking for Node={node.data} with min = {min} and max={max} values')
        
    if not min < node.data < max:
        print(f'Node={node.data} checked and found invalid as not falling between min = {min} and max={max}')
        dict1[node.data] = False
        #return False
    else:
        dict1[node.data] = True
        print(f'Node={node.data} checked and valid BST node')
    return isValid(node.left,min,node.data,dict1) and isValid(node.right,node.data,max,dict1)
def validateBST(root):
    min = float('-inf')
    max = float('inf')
    node = root
    dict1 = isValid(node,min,max,{})
    print(f'BST Element status: {dict1}')
    for val in dict1.values():
        if val == False:
            return False
    return True    


       
if __name__=="__main__":
    print("Hello World")
    root = node(15)
    root.left = node(4)
    root.right = node(11)
    root.left.left = node(3)
    root.left.right = node(7)
    root.left.right.left = node(6)
    root.left.right.right = node(8)
    root.right.left = node(17)
    root.right.right = node(29)
    print(root.data)
    print(f'Given BST Tree is {validateBST(root)}')