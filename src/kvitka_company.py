from typing import Tuple, List, Dict
from collections import defaultdict
import csv, math

"""
Максимальна кількість автомобілів, які зможуть проїхати протягом дня з квіткових ферм до квіткових магазинів.
"""


def read_input_data_from_file(input_file: str):
    if input_file is None:
        raise FileNotFoundError("File not found")

    data = {
        'farms': [],
        'shops': [],
        'directions': [],
        'graph': defaultdict(dict)
    }

    try:
        with open(f'../src/kvitka_company_resources/{input_file}', 'r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data['farms'].extend(row)
                elif index == 1:
                    data['shops'].extend(row)
                else:
                    # data['directions'].append(tuple(row))
                    start_node, end_node, weight = row
                    data['graph'][start_node][end_node] = weight

            # for (start_node, end_node, weight) in data['directions']:
            #     data['graph'][start_node][end_node] = weight
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{input_file}' not found")
    except ValueError:
        raise ValueError('Value is not corrected')

    print(data.values())
    print()

    return data


def write_output_data_from_file(output_data, output_file_name):
    with open(f'../src/kvitka_company_resources/{output_file_name}', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(output_data)


def dfs(graph: Dict[str, Dict[str, int]], start: str, destination: str):
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
            # delete edge
            del graph[edge[0]][edge[1]]


def max_flow(graph, start, destination):
    total_flow = 0
    while True:
        path, found_flow = dfs(graph, start, destination)

        if found_flow == 0:
            break

        total_flow += found_flow
        decrease_weight_on_path(graph, path, found_flow)

    return total_flow


input_graph_dict = {
    "A": {"B": 10, "D": 8, "C": 13},
    "B": {"K": 5},
    "C": {"F": 21},
    "D": {"K": 4},
    "K": {"L": 5, "N": 5},
    "L": {"P": 9, "P1": 3},
    "N": {"P": 10},
    "P": {"VD": float("inf")},
    "F": {"N": 4, "S": 7},
    "S": {"P": 9, "P2": 2},
    "P1": {"VD": float("inf")},
    "P2": {"VD": float("inf")},
}
#
# print(max_flow(input_graph_dict, "A", "VD"))
data = read_input_data_from_file('input_data.csv')

