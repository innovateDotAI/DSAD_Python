'''
Count BST nodes that lie in a given range

Given a Binary Search Tree (BST) and a range [l, h], the task is to count the number of nodes in the BST that lie in the given range.
'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def getElement(root,nlist,min,max):
    if root is None:
        return
    getElement(root.left,nlist,min,max)
    if min < root.data < max:
        nlist.append(root.data)
    getElement(root.right,nlist,min,max)
        
if __name__=="__main__":
    l=5
    h=45
    root = node(10)
    root.left = node(5)
    root.left.left = node(1)
    root.right = node(50)
    root.right.left = node(40)
    root.right.right = node(100)
    nlist = []
    getElement(root,nlist,l,h)
    print(nlist)
