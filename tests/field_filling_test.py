from unittest import TestCase, main
from src.field_filling import field_filling, read_input_data_from_file, write_output_data_to_file


class FieldFillingTest(TestCase):
    def test_field_filling(self):
        field_filling(input_file='test_input.txt', output_file='test_output')
        test_input = open(f'../src/field_filling_resources/test_input.txt', 'r')
        test_field_filling = open(f'../src/field_filling_resources/test_field_filling.txt', 'r')
        self.assertTrue(test_input, test_field_filling)
        test_input.close()
        test_field_filling.close()

    def test_none_input_data(self):
        with self.assertRaises(FileNotFoundError):
            read_input_data_from_file(input_file=None)

    def test_write_output_data_to_file(self):
        test_matrix = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
        write_output_data_to_file(output_file='test_output', matrix=test_matrix)
        test_write_output = open(f'../src/field_filling_resources/test_output.txt', 'r')
        test_correct_output = open(f'../src/field_filling_resources/test_wrrite_output_data_to_file_correct.txt', 'r')
        self.assertTrue(test_write_output, test_correct_output)
        test_write_output.close()
        test_correct_output.close()

    def test_same_color(self):
        with self.assertRaises(ValueError):
            field_filling(input_file='test_same_color_input.txt', output_file='test_same_color_output')


if __name__ == '__main__':
    main()
