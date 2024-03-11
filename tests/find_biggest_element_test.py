"""
Unittest function 'find_biggest_element'
"""

from unittest import TestCase, main
from lab_1.find_biggest_element import find_biggest_element


class FindBiggestElementTest(TestCase):

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            find_biggest_element([], 1)

    def test_k_greater_than_array(self):
        with self.assertRaises(ValueError):
            find_biggest_element([1, 2, 3], 4)

    def test_invalid_data_type(self):
        with self.assertRaises(TypeError):
            find_biggest_element([1.5, "20", "str"], 1)

    def test_find_first_biggest_element(self):
        array = [1, 2, 3, 4, 5]
        index, value, k = find_biggest_element(array, 1)
        self.assertEqual(index, 0)
        self.assertEqual(value, 1)
        self.assertEqual(k, 1)

    def test_find_last_biggest_element(self):
        array = [1, 2, 3, 4, 5]
        index, value, k = find_biggest_element(array, 5)
        self.assertEqual(index, 4)
        self.assertEqual(value, 5)
        self.assertEqual(k, 5)


if __name__ == '__main__':
    main()
