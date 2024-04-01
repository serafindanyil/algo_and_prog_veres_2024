"""
Напишіть функцію, яка виконає операцію інвертування (перевернення) бінарного дерева таким чином,
щоб лівий дочірній вузол став правим, а правий дочірній вузол став лівим.
"""


class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree) -> BinaryTree:
    if tree is None:
        return tree
    else:
        tree.left, tree.right = invert_binary_tree(tree.right), invert_binary_tree(tree.left)
    return tree

