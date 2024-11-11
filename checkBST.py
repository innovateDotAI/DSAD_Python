import isBST
root = isBST.node(10)
root.left = isBST.node(2)
root.right = isBST.node(7)
root.left.left = isBST.node(8)
root.left.right = isBST.node(4)
print(f'Given BST Tree is {isBST.validateBST(root)}')

