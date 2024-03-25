
"""
Unittest function 'jacky_min_eating_speed'
"""

from unittest import TestCase, main
from src.gorillaz_jacky import jacky_min_eating_speed


class FindBiggestElementTest(TestCase):
    def test_empty_array(self):
        with self.assertRaises(ValueError):
            jacky_min_eating_speed([], 3)

    def test_count_piles_greater_from_hours(self):
        with self.assertRaises(ValueError):
            jacky_min_eating_speed([3, 6, 7, 11], 3)

    def test_jacky_min_eating_speed(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(jacky_min_eating_speed(piles, h), 4)


if __name__ == '__main__':
    main()
