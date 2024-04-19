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

    def test_read_input_data_from_file(self):
        count_edges, clients_nodes, graph_in_list = GameServer.read_input_data_from_file(
            input_file='test_read_input.txt')
        test_count_edges, test_clients_nodes, test_graph_in_list = 6, (1, 2, 6), [[1, 3, 10], [3, 4, 80], [4, 5, 50],
                                                                                  [5, 6, 20], [2, 3, 40], [2, 4, 100]]
        self.assertTrue(count_edges, test_count_edges)
        self.assertTrue(clients_nodes, test_clients_nodes)
        self.assertTrue(graph_in_list, test_graph_in_list)

    def test_write_output_data_to_file(self):
        test_data = 'VirusLviv'
        GameServer.write_output_data_to_file(output_file='test_write_output', min_latency_from_server=test_data)
        test_write_output = open(f'../src/gamsrv_resources/test_write_output.txt', 'r')
        self.assertTrue(test_write_output, test_data)
        test_write_output.close()

    def test_game_server(self):
        count_edges, clients_nodes, graph_in_list = GameServer.read_input_data_from_file(input_file='input.txt')
        server_test = GameServer.game_servers(GameServer, count_edges, clients_nodes, graph_in_list)
        GameServer.write_output_data_to_file(output_file='output.txt', min_latency_from_server=server_test)
        test_game_server = open(f'../src/gamsrv_resources/output.txt', 'r')
        test_output = open(f'../src/gamsrv_resources/test_game_server_output.txt', 'r')
        self.assertTrue(test_game_server, test_output)
        test_game_server.close()
        test_output.close()


if __name__ == '__main__':
    main()
