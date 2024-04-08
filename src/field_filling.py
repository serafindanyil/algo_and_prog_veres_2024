
def __read_input_data_from_file(input_file):
    file = open(f'../src/field_filling_resources/{input_file}', 'r')
    try:
        rows, colunms = tuple(map(int, file.readline().split(',')))
        start_pos = tuple(map(int, file.readline().split(',')))
        change_color = str(file.readline().strip())
        matrix = [eval(file.readline().strip(',\n')) for _ in range(rows)]
    except FileNotFoundError:
        FileNotFoundError('File not found')
    file.close()
    return rows, colunms, start_pos, change_color, matrix
def __write_output_data_to_file():
    pass
def field_filling(input_file, output_file):
    rows, colunms, start_pos, change_color, matrix = __read_input_data_from_file(input_file)

    visited = set()
    queue = []
    start_color

    def bfs(visited, graph, node):  # function for BFS
        visited.append(node)
        queue.append(node)

        while queue:  # Creating loop to visit each node
            m = queue.pop(0)
            print(m, end=" ")

            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

