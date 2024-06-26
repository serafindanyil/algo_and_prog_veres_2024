from unittest import TestCase, main
from src.kvitka_company import read_input_data_from_file, write_output_data_to_file, max_flow


class KvitkaCompanyTest(TestCase):
    def test_read_input_data_from_file(self):
        path_to_file = '../src/kvitka_company_resources/test_read_input.csv'
        data = read_input_data_from_file(path_to_file=path_to_file)

        test_data = {
            'farms': ['VS', 'F1', 'F2', 'F3'],
            'shops': ['S1', 'S2', 'S3', 'S4', 'S5'],
            'graph': {
                'VS': {'F1': float('inf')}
            }
        }

        self.assertTrue(data['farms'], test_data['farms'])
        self.assertTrue(data['shops'], test_data['shops'])
        self.assertTrue(data['graph'], test_data['graph'])

    def test_write_output_data_to_file(self):
        test_data = 123

        output_file_path = '../src/kvitka_company_resources/test_write_output.csv'
        write_output_data_to_file(test_data, output_file_path)
        write_output = open(f'../src/kvitka_company_resources/test_write_output.csv', 'r')
        self.assertTrue(write_output, test_data)

    def test_max_flow(self):
        test_result = 15

        path_to_file = '../src/kvitka_company_resources/test_input_data.csv'
        data = read_input_data_from_file(path_to_file)
        result = max_flow(data['graph'], 'VS', 'VD')
        self.assertTrue(result, test_result)


if __name__ == '__main__':
    main()
