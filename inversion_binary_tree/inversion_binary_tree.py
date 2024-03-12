"""
Напишіть функцію, яка виконає операцію інвертування (перевернення) бінарного дерева таким чином,
щоб лівий дочірній вузол став правим, а правий дочірній вузол став лівим.
"""


class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class InvertTree(BinaryTree):
    @staticmethod
    def invert_binary_tree(tree) -> BinaryTree:
        if tree is None:
            return tree
        else:
            tree.left, tree.right = InvertTree.invert_binary_tree(tree.right), InvertTree.invert_binary_tree(tree.left)
        return tree
