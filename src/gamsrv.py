from typing import Tuple, List


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def up(self, i):
        while i != 0 and self.heap[i].priority > self.heap[(i - 1) // 2].priority:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def down(self, i):
        n = len(self.heap)
        while 2 * i + 1 < n:
            max_child = 2 * i + 1
            if max_child + 1 < n and self.heap[max_child].priority < self.heap[max_child + 1].priority:
                max_child += 1
            if self.heap[i].priority >= self.heap[max_child].priority:
                break
            self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
            i = max_child

    def insert_element(self, obj):
        self.heap.append(obj)
        self.up(len(self.heap) - 1)

    def delete_element(self, obj):
        obj_index = None
        n = len(self.heap)
        for index in range(0, n):
            if obj == self.heap[index]:
                obj_index = index
        self.heap[obj_index], self.heap[n - 1] = self.heap[n - 1], self.heap[obj_index]
        self.heap.pop(n - 1)
        self.down(obj_index)
        return obj_index, obj #added!!!!!


class GameServer:

    @staticmethod
    def read_input_data_from_file(input_file):
        if input_file is None:
            raise FileNotFoundError("File not found")
        try:
            with open(f'../src/gamsrv_resources/{input_file}', 'r') as file:
                count_nodes, count_edges = tuple(map(int, file.readline().split(' ')))
                clients_nodes = tuple(map(int, file.readline().split(' ')))
                nodes = tuple(tuple(map(int, file.readline().split(' '))) for cycle in range(count_nodes))
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{input_file}' not found")
        except ValueError:
            raise ValueError('Value is not corrected')
        file.close()
        return count_nodes, count_edges, clients_nodes, nodes

    # def write_output_data_to_file(output_file, matrix):
    #     file = open(f'../src/field_filling_resources/{output_file}', 'w')
    #     for rows in matrix:
    #         file.write(f'{rows}\n')
    #     file.close()

    def game_server_max_delay_time(self, input_file):
        count_nodes, count_edges, clients, nodes = self.read_input_data_from_file(input_file)
        graph = {start_node: (end_node, latency) for (start_node, end_node, latency) in nodes}

        # def network_delay_time(graph, client):
        #     pq = PriorityQueue()
        #     start_element = Node(client, 0)
        #     pq.insert_element(start_element)  # Використовуємо ваш метод insert_element для вставки елемента
        #     shortest_path = {}
        #     while pq.heap:
        #         w, v = pq.delete_element(client)  # Використовуємо ваш метод delete_element для вилучення елемента
        #         if v not in shortest_path:
        #             shortest_path[v] = w
        #             for v_i, w_i in graph[v]:
        #                 add_element = Node(w + w_i, v_i)
        #                 pq.insert_element(
        #                     add_element)  # Використовуємо ваш метод insert_element для вставки нового елемента
        #     if len(shortest_path) == client:
        #         return max(shortest_path.values())
        #     else:
        #         return -1
        #
        # shortness = []
        # for client in clients:
        #     shortness.append(network_delay_time(graph, client))

        # def dijkstra(graph, source):
        #     # Initialize the distance and predecessor dictionaries
        #     distance = {node: float('inf') for node in graph}
        #     distance[source] = 0
        #     predecessor = {node: None for node in graph}
        #     # Create a priority queue of nodes, ordered by their distance
        #     pq = PriorityQueue()
        #     pq.insert_element(Node(source, 0))
        #     # Repeat until the queue is empty
        #     while pq.heap:
        #         # Extract the node with the smallest distance
        #         dist, node = pq.delete_element(source)
        #         # For each neighbor of the node
        #         for neighbor, weight in graph[node]:
        #             # Calculate the new distance
        #             new_dist = dist + weight
        #             # If the new distance is smaller than the old distance
        #             if new_dist < distance[neighbor]:
        #                 # Update the distance and predecessor
        #                 distance[neighbor] = new_dist
        #                 predecessor[neighbor] = node
        #                 # Insert or update the neighbor in the queue
        #                 heapq.heappush(queue, (new_dist, neighbor))
        #     # Return the distance and predecessor dictionaries
        #     return distance, predecessor

            # def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        #     graph = collections.defaultdict(list)
        #     for (u, v, w) in times:
        #         graph[u].append((v, w))
        #
        #     priority_queue = [(0, K)]
        #     shortest_path = {}
        #     while priority_queue:
        #         w, v = heapq.heappop(priority_queue)
        #         if v not in shortest_path:
        #             shortest_path[v] = w
        #             for v_i, w_i in graph[v]:
        #                 heapq.heappush(priority_queue, (w + w_i, v_i))
        #
        #     if len(shortest_path) == N:
        #         return max(shortest_path.values())
        #     else:
        #         return -1

Server1 = GameServer.game_server_max_delay_time(GameServer, input_file='input.txt')
print(Server1)
