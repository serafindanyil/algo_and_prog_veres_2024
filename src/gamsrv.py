from collections import defaultdict
import src.heap_based_priority_queue as pqueue


class GameServer:
    @staticmethod
    def read_input_data_from_file(input_file):
        if input_file is None:
            raise FileNotFoundError("File not found")
        try:
            with open(f'../src/gamsrv_resources/{input_file}', 'r') as file:
                count_nodes, count_edges = tuple(map(int, file.readline().split(' ')))
                clients_nodes = tuple(map(int, file.readline().split(' ')))
                graph_in_list = list(list(map(int, file.readline().split(' '))) for cycle in range(count_nodes))
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{input_file}' not found")
        except ValueError:
            raise ValueError('Value is not corrected')
        file.close()
        return count_edges, clients_nodes, graph_in_list

    @staticmethod
    def write_output_data_to_file(output_file, min_latency_from_server):
        file = open(f'../src/gamsrv_resources/{output_file}', 'w')
        file.write(str(min_latency_from_server))
        file.close()

    def game_servers(self, count_edges, clients, graph_in_list):
        graph = defaultdict(list)
        reversed_graph = defaultdict(list)
        combined_paths = {}
        combined_shortest_path = defaultdict(list)
        routers = set(range(1, count_edges)) - set(clients)
        max_latency = []

        for (start_node, end_node, latency) in graph_in_list:
            graph[start_node].append((end_node, latency))
            reversed_graph[end_node].append((start_node, latency))

        def dijkstra(start_pos, input_graph):
            pq = pqueue.PriorityQueue()
            priority_queue_start_node = pqueue.Node(start_pos, 0)
            pq.insert_element(priority_queue_start_node)
            shortest_path = {}

            while pq.heap:
                end_pos, latency = pq.pop_element()
                if end_pos not in shortest_path:
                    shortest_path[end_pos] = latency
                    for end_pos_i, latency_i in input_graph[end_pos]:
                        priority_queue_add_node = pqueue.Node(end_pos_i, latency + latency_i)
                        pq.insert_element(priority_queue_add_node)
            return shortest_path

        for client in clients:
            path = dijkstra(client, graph)
            reverse_path = dijkstra(client, reversed_graph)
            for k, end_node in path.items():
                if k not in clients:
                    if k in combined_paths:
                        combined_paths[k] = max(combined_paths[k], end_node)
                    else:
                        combined_paths[k] = end_node

            for k, end_node in reverse_path.items():
                if k not in clients:
                    if k in combined_paths:
                        combined_paths[k] = max(combined_paths[k], end_node)
                    else:
                        combined_paths[k] = end_node

        for k, end_node in combined_paths.items():
            combined_shortest_path[k].append(end_node)

        for router in routers:
            max_latency.extend(combined_shortest_path[router])

        return min(max_latency)
