'''
K’th Largest Element in BST when modification to BST is not allowed
Given a Binary Search Tree (BST) and a positive integer k, the task is to find the kth largest element in the Binary Search Tree.
'''

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def getAssend(root,alist):
    if root is None:
        return
    getAssend(root.right,alist)
    alist.append(root.data)
    getAssend(root.left,alist)
'''
Q)Find the node with minimum value in a Binary Search Tree 
Sol: Similar logice, got only left till end and get the element

Q) Inorder Successor in Binary Search Tree
Sol: Similar logic of inorder search with output the next bigger number for given number

Q) Find median of BST
Given a Binary Search Tree, find the median of it. 

If number of nodes are even: then median = ((n/2th node + ((n)/2th+1) node) /2 
If number of nodes are odd: then median = (n+1)/2th node.

Sol: Get Inorder list from BST then get median as Inorder is sorted list and can be used for median.

Q) Binary Tree to Binary Search Tree Conversion
Sol: 1. Get inorder list from BT
2. Sort the list
3. Start inorder search on BT and replace the each element as per sorted list.

Q) Count pairs from two BSTs whose sum is equal to a given value x
Sol: 1.  Create Inorder list for both BST
2. Run for loop with both list and put sum criteria to get all pair



'''
if __name__=="__main__":
    k=3
    print("hello")
    root = node(20)
    root.left = node(8)
    root.left.left = node(4)
    root.left.right = node(12)
    root.left.right.left = node(10)
    root.left.right.right = node(14)
    root.right = node(22)
    alist = []
    getAssend(root,alist)
    print(alist[k-1])
