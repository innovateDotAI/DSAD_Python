
'''
Iterative searching in Binary Search Tree

Given a Binary Search Tree and a key, the task is to find if the node with a value 
key is present in the BST or not.
'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def search(root, key):
    curr = root
    while curr is not None:
        if curr.data == key:
            return True
        elif curr.data < key:
            curr = curr.right
        else:
            curr = curr.left
    return False 
    


if __name__ == "__main__":
    root = node(6)
    root.left = node(2)
    root.right = node(8)
    root.right.left = node(7)
    root.right.right = node(9)
    key = 71
    print(search(root,key))