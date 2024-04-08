def __read_input_data_from_file(input_file):
    file = open(f'../src/field_filling_resources/{input_file}', 'r')
    try:
        rows, colunms = tuple(map(int, file.readline().split(',')))
        start_pos = tuple(map(int, file.readline().split(',')))
        change_color = str(eval(file.readline()))
        matrix = [eval(file.readline().strip(',\n')) for _ in range(rows)]
    except FileNotFoundError:
        FileNotFoundError('File not found')
    file.close()
    return rows, colunms, start_pos, change_color, matrix


def __write_output_data_to_file(output_file, matrix):
    file = open(f'../src/field_filling_resources/{output_file}', 'w')
    for rows in matrix:
        file.write(f'{rows}\n')


def field_filling(input_file, output_file):
    rows, colunms, start_pos, change_color, matrix = __read_input_data_from_file(input_file)
    start_color = matrix[start_pos[0]][start_pos[1]]

    visited = [[False] * colunms for _ in range(rows)]
    queue = [(start_pos[0], start_pos[1])]

    while queue:
        row, col = queue.pop(0)
        if row < 0 or row >= rows or col < 0 or col >= colunms or visited[row][col] or matrix[row][col] != start_color:
            continue
        matrix[row][col] = change_color
        visited[row][col] = True
        queue.append((row + 1, col))
        queue.append((row - 1, col))
        queue.append((row, col + 1))
        queue.append((row, col - 1))
    __write_output_data_to_file(output_file, matrix)
    # while queue:
    #     row, col = queue.pop(0)
    #     if (row < 0 or row >= rows or col < 0 or col >= col or visited[row][col] or matrix[row][col] != start_color):
    #         continue
    #     matrix[row][col] = replacement_color
    #     visited[row][col] = True
    #     queue.append((row + 1, col))
    #     queue.append((row - 1, col))
    #     queue.append((row, col + 1))
    #     queue.append((row, col - 1))
    # # def bfs(visited, graph, node):  # function for BFS
    #     visited.append(mtrx(node))
    #     queue.append(mtrx(node))
    #
    #
    #     while queue:  # Creating loop to visit each node
    #         row, col = queue.pop(0)
    #         for neighbour in graph[m]:
    #             if neighbour not in visited:
    #                 visited.append(neighbour)
    #                 queue.append(neighbour)
    #
    # bfs(visited, matrix, start_pos)
    print(start_color)
    print(change_color)
    print(type(start_color))
    print(type(change_color))


field_filling(input_file='input_data.txt', output_file='output_data.txt')
