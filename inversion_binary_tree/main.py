"""
This is main script
"""

from inversion_binary_tree import BinaryTree, InvertTree

if __name__ == '__main__':
    root = BinaryTree(1)

    root.left = BinaryTree(2)
    root.right = BinaryTree(3)

    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)

    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    invert_tree = InvertTree.invert_binary_tree(root)

    print(
        f"""
                         {root.value}
                      {root.left.value}     {root.right.value}
                    {root.left.left.value}   {root.left.right.value} {root.right.left.value}   {root.right.right.value}
                    """
    )



