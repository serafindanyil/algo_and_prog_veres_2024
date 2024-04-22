from unittest import TestCase, main
from src.gamsrv import GameServer


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
