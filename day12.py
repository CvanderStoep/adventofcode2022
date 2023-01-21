# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)
import networkx as nx


def read_input_file(filename):
    with open(filename) as f:
        content = f.read().splitlines()
    return content


# heightmap.append(list(map(int, list(line))))
def process_input_lines(input_lines):
    heightmap = []
    for line in input_lines:
        line_list = list(line)
        heightmap.append(line_list)
    return heightmap


def surrounding(input, x, y):
    vals = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(x_i, y_i) for (x_i, y_i) in vals if 0 <= x_i < len(input) and 0 <= y_i < len(input[x])]


def define_graph(input_data):
    rows = len(input_data)
    cols = len(input_data[0])
    DG = nx.DiGraph()

    for i in range(rows):
        for j in range(cols):
            if input_data[i][j] == 'S':
                start_position = (i, j)
                input_data[i][j] = 'a'
            if input_data[i][j] == 'E':
                end_position = (i, j)
                input_data[i][j] = 'z'

    for i in range(rows):
        for j in range(cols):

            for x, y in surrounding(input_data, i, j):
                source = input_data[i][j]
                destination = input_data[x][y]
                if ord(destination) <= ord(source) + 1:
                    DG.add_edge((i, j), (x, y))
                    # print(f'{i}, {j}, {x}, {y}', {heightmap[i][j]}, {heightmap[x][y]})
    return DG, start_position, end_position


def path_pretty_print(path, input_data):
    rows = len(input_data)
    cols = len(input_data[0])
    for i in range(rows):
        for j in range(cols):
            if (i, j) in path:
                print('*', end="")
            else:
                print(' ', end="")
        print()


if __name__ == '__main__':
    filename = "input/input12.txt"
    content = read_input_file(filename)
    heightmap = process_input_lines(content)

    DG, start_position, end_position = define_graph(heightmap)
    shortest_path = nx.shortest_path(DG, source=start_position, target=end_position)
    path_pretty_print(shortest_path, heightmap)

    print(f'partI:  {len(shortest_path) -1 = }')

    rows = len(heightmap)
    cols = len(heightmap[0])
    fewest_steps = rows * cols

    for i in range(rows):
        for j in range(cols):
            if heightmap[i][j] == 'a':
                start_position = (i, j)
                try:
                    shortest_path = nx.shortest_path(DG, source=start_position, target=end_position)
                    if len(shortest_path) - 1 < fewest_steps:
                        fewest_steps = len(shortest_path) - 1
                except Exception as error:
                    # print(error)
                    pass
    print(f'partII: {fewest_steps= } ')
