from unittest import TestCase, main
from src.linguist_game import string_of_words, read_input_data_from_file, write_output_data_to_file


class LinguistGameTest(TestCase):
    def test_string_of_words(self):
        input_words = ['crates', 'car', 'cats', 'crate', 'rate', 'at', 'ate', 'tea', 'rat', 'a']
        count_words = 10

        result = string_of_words(input_words, count_words)
        test_result = 6

        self.assertTrue(result, test_result)

    def test_none_input_data(self):
        path = '../src/linguist_game_resources/none.txt'

        with self.assertRaises(FileNotFoundError):
            read_input_data_from_file(path)

    def test_read_input_data_from_file(self):
        path = '../src/linguist_game_resources/test_input_data.txt'

        result = read_input_data_from_file(path)
        test_count_words, test_words_list = 5, ['b', 'bcad', 'bca', 'bad', 'bd']

        self.assertTrue(result, (test_count_words, test_words_list))

    def test_write_output_data_to_file(self):
        path = '../src/linguist_game_resources/test_output_data.txt'

        test_max_legnth = 6
        write_output_data_to_file(path, test_max_legnth)

        file = open(path, 'r')
        result = file.readline().strip('\n')

        file.close()

        self.assertTrue(test_max_legnth, result)


if __name__ == '__main__':
    main()
