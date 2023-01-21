# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)
import re
from typing import List


class Sand:
    def __init__(self, x=500, y=0, rest=False):
        self.x = x
        self.y = y
        self.rest = rest


def print_cave(cave, min_x):
    rows = len(cave)
    cols = len(cave[0])
    for y in range(rows):
        for x in range(min_x, cols):
            if x == 500 and y == 0:
                print('+', end="")
            elif cave[y][x] == 'air':
                print('.', end="")
            elif cave[y][x] == 'rock':
                print('#', end="")
            else:
                print('o', end="")
        print()


def cave_dimensions(cave, part=1):
    min_x = 0
    min_y = 0
    max_x = len(cave[0])  # number of columns
    max_y = len(cave)  # number of rows

    for x in range(max_x):
        for y in range(max_y):
            if cave[y][x] == 'rock':
                # print(f'rock layer found at {x= } {y= }')
                min_x = x
                return min_x, max_x - 1, min_y, max_y - 1  # zero based counting


def sand_move(cave, sand: Sand, part=1, floor_level=11):
    if cave[sand.y + 1][sand.x] == 'air':
        sand.y = sand.y + 1
        return
    if cave[sand.y + 1][sand.x - 1] == 'air':
        sand.x = sand.x - 1
        sand.y = sand.y + 1
        return
    if cave[sand.y + 1][sand.x + 1] == 'air':
        sand.x = sand.x + 1
        sand.y = sand.y + 1
        return
    sand.rest = True
    cave[sand.y][sand.x] = 'sand'
    return


def read_input_file(filename):
    with open(filename) as f:
        content = f.read().splitlines()
    return content


def create_cave(content):
    """"read the scanned lines and return a cave 2D list [y][x] which contains air/rock"""
    paths: List[List[List[int]]] = []
    #  read the scanned lines
    for line in content:
        # print(line)
        scanned_line = re.findall("(\d+\,\d+)", line)
        path = []
        for scan in scanned_line:
            node = [int(a) for a in scan.split(',')]
            path.append(node)
        paths.append(path)

    #  fill the cave with air/rock material
    cols = 0
    rows = 0
    for path in paths:
        for node in path:
            cols = max(cols, node[0] + 1)
            rows = max(rows, node[1] + 1)

    cave = [['air' for _ in range(cols)] for _ in range(rows)]

    for path in paths:
        current_node = 0
        while current_node < len(path) - 1:
            x_start = path[current_node][0]
            y_start = path[current_node][1]
            x_end = path[current_node + 1][0]
            y_end = path[current_node + 1][1]
            if x_start > x_end:
                x_start, x_end = x_end, x_start
            if y_start > y_end:
                y_start, y_end = y_end, y_start
            for x in range(x_start, x_end + 1):
                for y in range(y_start, y_end + 1):
                    cave[y][x] = 'rock'
            current_node += 1

    return cave


def create_cave_with_floor(content, part=1):
    """"read the scanned lines and return a cave 2D list [y][x] which contains air/rock"""
    paths: List[List[List[int]]] = []
    #  read the scanned lines
    for line in content:
        # print(line)
        scanned_line = re.findall("(\d+\,\d+)", line)
        path = []
        for scan in scanned_line:
            node = [int(a) for a in scan.split(',')]
            path.append(node)
        paths.append(path)

    #  fill the cave with air/rock material
    cols = 0
    rows = 0
    for path in paths:
        for node in path:
            cols = max(cols, node[0] + 1)
            rows = max(rows, node[1] + 1)

    if part == 1:
        cave = [['air' for _ in range(cols)] for _ in range(rows)]
    else:
        rows = rows + 2  # floor level at y_max + 2
        cols = cols + 2 * rows
        cave = [['air' for _ in range(cols)] for _ in range(rows)]

    for path in paths:
        current_node = 0
        while current_node < len(path) - 1:
            x_start = path[current_node][0]
            y_start = path[current_node][1]
            x_end = path[current_node + 1][0]
            y_end = path[current_node + 1][1]
            if x_start > x_end:
                x_start, x_end = x_end, x_start
            if y_start > y_end:
                y_start, y_end = y_end, y_start
            for x in range(x_start, x_end + 1):
                for y in range(y_start, y_end + 1):
                    cave[y][x] = 'rock'
            current_node += 1

    if part == 2:
        min_x, max_x, min_y, max_y = cave_dimensions(cave)
        for x in range(min_x, max_x + 1):
            y = max_y
            cave[y][x] = 'rock'

    return cave


if __name__ == '__main__':
    """
    for part II a rock layer at y == 159 was added manually.
    
    """
    filename = "input/input14.txt"
    content = read_input_file(filename)
    content.append('288,159 -> 752,159')  # manual rock layer
    cave = create_cave(content)
    min_x, max_x, min_y, max_y = cave_dimensions(cave)

    overflow = False
    round = 0
    while not overflow:
        sand = Sand()
        while not sand.rest:
            sand_move(cave, sand)
            # if sand.y == max_y:  # part I - check
            if sand.y == 0:        # part II - check
                # print(f'partI: overflow after {round= }')
                print(f'partII: overflow after {round+1= }')
                overflow = True
                break
        round += 1
    print_cave(cave, min_x)
    print()

