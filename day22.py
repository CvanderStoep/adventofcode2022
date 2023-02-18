import logging
import re

import numpy as np

def read_input_file(filename):
    """"
    returns a 3D map array[i][j]
    with rows [i] and columns [j]
    returns the path
    map[i][j]
    --> j
    |
    |i
    \/
    """
    with open(filename) as f:
        content = f.read().splitlines()
    map = []
    for line in (content):
        map.append(list(line))

    return map[:-2], line  # returns map + path

def fill_map(map):
    """right fill map with spaces"""
    rows = len(map)
    cols = len(map[0])
    for c in map:
        cols = max(cols, len(c))

    for c in map:
        for _ in range(cols-len(c)):
            c.append(' ')
    return map

def convert_path_to_list(path):
    steps = [int(a) for a in re.findall("[0-9]+", path)]
    headings = re.findall("[L,R]", path)
    path_list = []
    for i in range(min(len(steps), len(headings))):
        path_list.append(steps[i])
        path_list.append(headings[i])
    path_list.append(steps[-1])
    return path_list


def evaluate_path(map, position, path, heading):

    for change in path:  # change in heading or number of steps forward in current heading
        if isinstance(change, int):
            position = move_position(map=map, heading=heading, position=position, steps=change)
        else:
            heading = change_heading(rotation=change, heading=heading)

    return position, heading


def move_position(map, heading, position, steps):
    """"
    move steps from current position into the heading
    if wall (#) is encountered, break
    if space ( ) is encountered, skip until wall or "." is encountered
    use module rows/cols to rotate from left/right or top/bottom
    """
    rows = len(map)
    cols = len(map[0])

    moves = 0
    while moves < steps:
        old_position = position.copy()
        match heading:
            case 0:
                position[0] -= 1
                position[0] = position[0] % rows
                while map[position[0]][position[1]] == " ":
                    position[0] -= 1
                    position[0] = position[0] % rows
            case 90:
                position[1] += 1
                position[1] = position[1] % cols
                while map[position[0]][position[1]] == " ":
                    position[1] += 1
                    position[1] = position[1] % cols
            case 180:
                position[0] += 1
                position[0] = position[0] % rows
                while map[position[0]][position[1]] == " ":
                    position[0] += 1
                    position[0] = position[0] % rows
            case 270:
                position[1] -= 1
                position[1] = position[1] % cols
                while map[position[0]][position[1]] == " ":
                    position[1] -= 1
                    position[1] = position[1] % cols
        moves += 1
        if map[position[0]][position[1]] == "#":
                position = old_position
                break
    return position

def change_heading(rotation, heading):
    if rotation == "R":
        heading += 90
    else:
        heading -= 90
    return heading%360

def starting_position(map):
    for j in range(len(map[0])):
        if map[0][j] == "." :
            return [0,j]


def calculate_password(position, heading):
    final_row = position[0] + 1  # base 1
    final_column = position[1] + 1  # base 1
    match heading:
        case 90:
            final_facing = 0
        case 180:
            final_facing = 1
        case 270:
            final_facing = 2
        case 0:
            final_facing = 3

    print(f'{final_row= }, {final_column= }, {final_facing= }')
    password = 1000 * final_row + 4 * final_column + final_facing

    return password


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    filename = "input/input22.txt"
    map, path = read_input_file(filename)
    map = fill_map(map)
    path = convert_path_to_list(path)
    logging.info(path)
    start = starting_position(map)
    logging.debug(start)

    final_position, final_heading = evaluate_path(map= map, position=start, path=path, heading=90)
    logging.info("final position: " + str(final_position))
    logging.info("final heading: " + str(final_heading))

    password = calculate_password(position=final_position, heading=final_heading)


    print(f'partI: {password= }')

