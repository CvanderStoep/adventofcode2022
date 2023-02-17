# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

# https://adventofcode.com/2022/day/18
from itertools import combinations
import re


def distance(cube1, cube2):
    """"returns the manhattan distance of two objects"""
    distance = abs(cube1[0] - cube2[0]) + abs(cube1[1] - cube2[1]) + abs(cube1[2] - cube2[2])
    return distance


def read_input_file(filename):
    with open(filename) as f:
        content = f.read().splitlines()
        cube_list = []
        for c in content:
            cube = re.findall("[0-9]+", c)
            cube = [int(a) for a in cube]
            cube_list.append(cube)
    return cube_list


def surface_area(cube_list):
    area = 6 * len(cube_list)
    for cube1, cube2 in combinations(cube_list, 2):
        if distance(cube1, cube2) == 1:
            area -= 2
    return area


if __name__ == '__main__':
    filename = "input/input18-2.txt"
    cube_list = read_input_file(filename)
    total_surface_area = surface_area(cube_list)

    print(f'partI: {total_surface_area= }')
    print(f'partII:')
