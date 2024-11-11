'''
LCA in BST – Lowest Common Ancestor in Binary Search Tree

Given two values n1 and n2 in a Binary Search Tree, find the Lowest Common Ancestor (LCA). 
You may assume that both values exist in the tree. The lowest common ancestor between two 
nodes n1 and n2 is defined as the lowest node that has both n1 and n2 as descendants 
(where we allow a node to be a descendant of itself). In other words, the LCA of n1 and n2 is 
the shared ancestor of n1 and n2 that is located farthest from the root [i.e., closest to n1 and n2].
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def lcaBST(root,n1,n2,lcaList):
    if root is None:
        return
    if n1 <= root.data <= n2:
        lcaList.append(root.data)
    if n1< root.data and  n2 < root.data:
        lcaBST(root.left,n1,n2,lcaList)
        lcaBST(root.right,n1,n2,lcaList)
    if n1> root.data and n2 > root.data:
        lcaBST(root.right,n1,n2,lcaList)
        lcaBST(root.left,n1,n2,lcaList)
if __name__=="__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    lcaList = []
    n1 = 8
    n2 = 14
    lcaBST(root,n1,n2,lcaList)
    print(lcaList[0])
        
        
    