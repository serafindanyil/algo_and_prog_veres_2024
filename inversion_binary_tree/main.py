"""
This is main script
"""
from inversion_binary_tree import BinaryTree

if __name__ == 'main':
    root = BinaryTree(1)

    root.left = BinaryTree(2)
    root.right = BinaryTree(3)

    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)

    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    invert_tree = root.invert_binary_tree(root)
    print(invert_tree)