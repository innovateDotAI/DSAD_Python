'''
Find the node with minimum value in a Binary Search Tree

Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.
'''
class node:
    def  __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def minValue(root,mList):
    if root is None:
        return
    minValue(root.left,mList)
    #print(f"Minimum Value in BST = {root.data}")
    mList.append(root.data)


if __name__=="__main__":
    root = node(5)
    root.left = node(4)
    root.left.left = node(3)
    root.left.left.left =node(1)
    root.right = node(6)
    root.right.right = node(7)
    minVal = []
    minValue(root,minVal)
    print(f'Minimum value={minVal[0]}')