from typing import Tuple, List, Dict, Any
from collections import defaultdict
import csv


def read_input_data_from_file(input_file: str):  # додати коментарі шо робиться з вхідними даними
    """
    The function parses the data by variables, and if there are no virtual points, the function adds them

    Args:
        input_file: The path to the input data using format csv

    Returns:
        data_type_dictionary: The dictionary has a parse data from arg: input_file.

    Raises:
        FileNotFoundError: If the arg: input_file is none.
        ValueError: If the value is not corrected.
    """
    if input_file is None:
        raise FileNotFoundError("File not found")

    data_type_dictionary: dict[str, list[Any] | defaultdict[Any, dict]] = {
        'farms': [],
        'shops': [],
        'graph': defaultdict(dict)
    }

    try:
        with open(f'../src/kvitka_company_resources/{input_file}', 'r') as file:
            reader = csv.reader(file)

            virtual_start_point = 'VS'
            virtual_end_point = 'VD'

            for index, row in enumerate(reader):
                if index == 0:
                    data_type_dictionary['farms'].extend(row)
                elif index == 1:
                    data_type_dictionary['shops'].extend(row)
                else:
                    start_node, end_node, weight = row

                    if data_type_dictionary['graph'].keys() != (virtual_start_point, virtual_end_point):
                        for start_farm_node in data_type_dictionary['farms']:
                            data_type_dictionary['graph'][virtual_start_point][start_farm_node] = float('inf')

                        for start_shop_node in data_type_dictionary['shops']:
                            data_type_dictionary['graph'][start_shop_node][virtual_end_point] = float('inf')

                    if weight == 'inf':
                        data_type_dictionary['graph'][start_node][end_node] = float('inf')
                    else:
                        data_type_dictionary['graph'][start_node][end_node] = int(weight)

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{input_file}' not found")
    except ValueError:
        raise ValueError('Value is not corrected')

    return data_type_dictionary


def write_output_data_to_file(output_data, output_file_name):
    """
        The function write the data.
        Args:
            output_data: The data from total flow.
            output_file_name: The output file name.
        """
    with open(f'../src/kvitka_company_resources/{output_file_name}', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str(output_data)])


def dfs(graph: Dict[str, Dict[str, int]], start: str, destination: str):
    """
        The default Depth For Search.

        Args:
            graph: The dictionary adjacency nodes.
            start: The start node.
            destination: The end node.
        """
    stack = [(start, float("inf"), [])]
    visited = set()

    while stack:
        current_element, current_weight, path = stack.pop()

        if current_element == destination:
            return path, current_weight

        visited.add(current_element)

        for next_element, weight in graph[current_element].items():
            if (
                    next_element not in visited and weight > 0
            ):
                new_flow = min(current_weight, weight)
                stack.append((next_element, new_flow, path + [(current_element, next_element)]))

    return [], 0


def decrease_weight_on_path(graph, path: List[Tuple[str, str]], found_flow: int):
    """_summary_

    Args:
        graph (_type_): _description_
        path (_type_): [(A, B), (B, C), (C, L)]
        found_flow (_type_): _description_
    """
    for edge in path:
        graph[edge[0]][edge[1]] -= found_flow
        if graph[edge[0]][edge[1]] == 0:
            del graph[edge[0]][edge[1]]


def max_flow(graph, start, destination):
    """
        The function for search max flow.

        Args:
            graph: The dictionary adjacency nodes.
            start: The start node.
            destination: The end node.

        Returns:
            total_flow: The total flow our graph.
        """
    total_flow = 0
    while True:
        path, found_flow = dfs(graph, start, destination)

        if found_flow == 0:
            break

        total_flow += found_flow
        decrease_weight_on_path(graph, path, found_flow)

    return total_flow
