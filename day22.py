import logging
import re

def read_input_file(filename):
    """"
    returns a 3D map array[i][j]
    with rows [i] and columns [j]
    returns the path
    """
    with open(filename) as f:
        content = f.read().splitlines()
    map = []
    for line in (content):
        map.append(list(line))

    return map[:-2], line  # returns map + path

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
    match heading:
        case 0:
            pass
        case 90:
            pass
        case 180:
            pass
        case 270:
            pass

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




if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    filename = "input/input22test.txt"
    map, path = read_input_file(filename)
    path = convert_path_to_list(path)
    logging.info(path)
    start = starting_position(map)
    logging.debug(start)

    final_position, final_heading = evaluate_path(map= map, position=start, path=path, heading=90)
    logging.info("final position: " + str(final_position))
    logging.info("final heading: " + str(final_heading))



    print(f'partI: ')

