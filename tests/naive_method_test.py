from unittest import TestCase, main
from src.naive_method import naive_method


class FindBiggestElementTest(TestCase):
    def test_empty_input(self):
        with self.assertRaises(ValueError):
            naive_method(None, None)

    def test_needle_greater_than_haystack(self):
        with self.assertRaises(ValueError):
            haystack_test = "acaaca"
            needle_test = "acaacaab"
            naive_method(haystack_test, needle_test)

    def test_invalid_data_type(self):
        with self.assertRaises(TypeError):
            haystack_test = 12
            needle_test = "acaacaab"
            naive_method(haystack_test, needle_test)

    def test_naive_method(self):
        haystack_test = 'acaacaab'
        needle_test = 'aac'

        needle_test_test = 2
        count_compare_test = 5
        needle_index, count_compare = naive_method(haystack_test, needle_test)
        self.assertEqual(needle_index, needle_test_test)
        self.assertEqual(count_compare, count_compare_test)


if __name__ == '__main__':
    main()
