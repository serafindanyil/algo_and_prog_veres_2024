from unittest import TestCase, main
from src.gamsrv import Node, PriorityQueue, GameServer


class NodeAndPriorityQueueTest(TestCase):
    def test_insert_element(self):
        pq = PriorityQueue()

        test = Node("test", 100)
        pq.insert_element(test)
        self.assertEqual(len(pq.heap), 1)

    def test_delete_element(self):
        pq = PriorityQueue()

        should_delete = Node("test", 100)
        pq.insert_element(should_delete)
        test1 = Node("test1", 10)
        pq.insert_element(test1)
        test2 = Node("test2", 20)
        pq.insert_element(test2)
        test3 = Node("test2", 30)
        pq.insert_element(test3)
        pq.delete_element(should_delete)
        self.assertEqual(len(pq.heap), 3)

    def test_pop_element(self):
        pq = PriorityQueue()

        test = Node("test1", 10)
        pq.insert_element(test)

        pq.pop_element()
        self.assertEqual(len(pq.heap), 0)

    def test_correct_priority_queue(self):
        pq = PriorityQueue()

        danik = Node("Danik", 300)
        pq.insert_element(danik)

        andrew = Node("Andrew", 20)
        pq.insert_element(andrew)

        vasya = Node("Vasya", 400)
        pq.insert_element(vasya)

        result = [node.priority for node in pq.heap]
        self.assertEqual(result, [400, 20, 300])


class GameServeTest(TestCase):
    def test_none_input_data(self):
        with self.assertRaises(FileNotFoundError):
            GameServer.read_input_data_from_file(input_file=None)

    def test_write_output_data_to_file(self):
        test_data = 'VirusLviv'
        GameServer.write_output_data_to_file(output_file='test_write_output', min_latency_from_server=test_data)
        test_write_output = open(f'../src/gamsrv_resources/test_write_output.txt', 'r')
        self.assertTrue(test_write_output, test_data)
        test_write_output.close()

    def test_read_inputput_data_from_file(self):
        test_count_edges, test_clients_nodes, test_graph_in_list = 1, (1, 2, 6), [[1, 3, 10]]
        test_read_input_data_from_file = GameServer.read_input_data_from_file(input_file='test_read_input')
        count_edges, clients_nodes, graph_in_list = test_read_input_data_from_file
        self.assertTrue(count_edges, test_count_edges)
        test_read_input_data_from_file.close()
    #         read_input_data_from_file(input_file=None)
    # def test_field_filling(self):
    #     field_filling(input_file='test_input.txt', output_file='test_output')
    #     test_input = open(f'../src/field_filling_resources/test_input.txt', 'r')
    #     test_field_filling = open(f'../src/field_filling_resources/test_field_filling.txt', 'r')
    #     self.assertTrue(test_input, test_field_filling)
    #     test_input.close()
    #     test_field_filling.close()
    #
    # def test_none_input_data(self):
    #     with self.assertRaises(FileNotFoundError):
    #         read_input_data_from_file(input_file=None)
    #
    # def test_write_output_data_to_file(self):
    #     test_matrix = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
    #     write_output_data_to_file(output_file='test_output', matrix=test_matrix)
    #     test_write_output = open(f'../src/field_filling_resources/test_output.txt', 'r')
    #     test_correct_output = open(f'../src/field_filling_resources/test_wrrite_output_data_to_file_correct.txt', 'r')
    #     self.assertTrue(test_write_output, test_correct_output)
    #     test_write_output.close()
    #     test_correct_output.close()
    #
    # def test_same_color(self):
    #     with self.assertRaises(ValueError):
    #         field_filling(input_file='test_same_color_input.txt', output_file='test_same_color_output')


if __name__ == '__main__':
    main()
