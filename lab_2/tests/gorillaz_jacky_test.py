
"""
Unittest function 'find_biggest_element'
"""

from unittest import TestCase, main
from lab_2.gorillaz_jacky import jacky_min_eating_speed


class FindBiggestElementTest(TestCase):
    def test_jacky_min_eating_speed(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(jacky_min_eating_speed(piles, h), 4)


if __name__ == '__main__':
    main()
