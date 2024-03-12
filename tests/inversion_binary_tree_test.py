"""
Unittest function 'InvertTree'
"""

from unittest import TestCase, main
from inversion_binary_tree.inversion_binary_tree import BinaryTree, InvertTree


class FindBiggestElementTest(TestCase):

    def test_empty_array(self):
        test_root = BinaryTree(None)
        self.assertEqual(test_root.value, None)

    def test_inversion_tree(self):
        test_root = BinaryTree(1)
        test_root.left = BinaryTree(2)
        test_root.right = BinaryTree(3)

        InvertTree.invert_binary_tree(test_root)

        self.assertEqual(test_root.value, 1)
        self.assertEqual(test_root.left.value, 3)
        self.assertEqual(test_root.right.value, 2)


if __name__ == '__main__':
    main()
