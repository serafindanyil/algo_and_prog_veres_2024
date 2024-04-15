def read_input_data_from_file(input_file):
    if input_file is None:
        raise FileNotFoundError("File not found")
    try:
        with open(f'../src/field_filling_resources/{input_file}', 'r') as file:
            rows, colunms = tuple(map(int, file.readline().split(',')))
            start_pos = tuple(map(int, file.readline().split(',')))
            change_color = str(eval(file.readline()))
            matrix = [eval(file.readline().strip(',\n')) for cycle in range(rows)]
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{input_file}' not found")
    except ValueError:
        raise ValueError('Value is not corrected')
    file.close()
    return rows, colunms, start_pos, change_color, matrix


def write_output_data_to_file(output_file, matrix):
    file = open(f'../src/field_filling_resources/{output_file}', 'w')
    for rows in matrix:
        file.write(f'{rows}\n')
    file.close()


def field_filling(input_file, output_file):
    rows, colunms, start_pos, change_color, matrix = read_input_data_from_file(input_file)
    start_color = matrix[start_pos[0]][start_pos[1]]

    try:
        if start_color is change_color:
            raise ValueError('The color it replaces is the same')
    except ValueError:
        raise

    visited = []
    queue = [(start_pos[0], start_pos[1])]

    while queue:
        row, col = queue.pop(0)
        if row < 0 or row >= rows or col < 0 or col >= colunms or (row, col) in visited or matrix[row][
            col] != start_color:
            continue
        matrix[row][col] = change_color
        visited.append((row, col))
        queue.append((row + 1, col))
        queue.append((row - 1, col))
        queue.append((row, col + 1))
        queue.append((row, col - 1))
        return matrix
    write_output_data_to_file(output_file, matrix)
