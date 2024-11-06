import isBST
root = isBST.node(2)
root.left = isBST.node(1)
root.right = isBST.node(7)
root.right.right = isBST.node(6)
root.right.right.right = isBST.node(9)
print(f'Given BST Tree is {isBST.validateBST(root)}')

