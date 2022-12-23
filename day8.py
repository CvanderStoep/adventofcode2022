# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

""""
Below description is generated from CHAT GTP when the code was uploaded ...

This is a program that reads a map from a file, processes it, and calculates the maximum scenic score and the number of
trees that are visible from at least one direction.
The read_input_file function reads the input file and returns its contents as a list of strings.
The process_input_lines function processes the input lines and returns a 2D list representation of the map.
The check_visible function calculates the number of trees that are visible from at least one direction by looping
through each cell in the map and checking its visibility in each direction. It returns the total number of visible trees.
The viewing_distance function calculates the maximum scenic score of the map. It has the same implementation as the
viewing_distance function described earlier.
Finally, the main function reads the input file, processes it, calculates the maximum scenic score and the number of
visible trees, and prints the results.
"""


def read_input_file():
    filename = "input/input8.txt"
    with open(filename) as f:
        content = f.read().splitlines()
    return content


def process_input_lines(input_lines):
    map_2D = []
    for line in input_lines:
        map = []
        for number in line:
            map.append(int(number))
        map_2D.append(map)
    return map_2D


def check_visible(tree_map):
    number_of_rows = len(tree_map)
    number_of_columns = len(tree_map[0])

    visible_left = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    visible_right = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    visible_top = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    visible_bottom = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    visible = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]

    # alternative could be to put visible on True,
    # check all the views, but only if visible is False so far; otherwise skip

    for row in range(1, number_of_rows - 1):
        for col in range(1, number_of_columns - 1):
            # left view
            for c in range(0, col):
                if tree_map[row][c] >= tree_map[row][col]:
                    visible_left[row][col] = False
                    break
            # right view
            for c in range(col + 1, number_of_columns):
                if tree_map[row][c] >= tree_map[row][col]:
                    visible_right[row][col] = False
                    break
            # top view
            for r in range(0, row):
                if tree_map[r][col] >= tree_map[row][col]:
                    visible_top[row][col] = False
                    break
            # bottom view
            for r in range(row + 1, number_of_rows):
                if tree_map[r][col] >= tree_map[row][col]:
                    visible_bottom[row][col] = False
                    break

    total_visible_trees = 0
    for r in range(0, number_of_rows):
        for c in range(0, number_of_columns):
            visible[r][c] = visible_left[r][c] | visible_right[r][c] | visible_top[r][c] | visible_bottom[r][c]
            if visible[r][c]:
                total_visible_trees += 1

    return total_visible_trees


def viewing_distance(tree_map):
    number_of_rows = len(tree_map)
    number_of_columns = len(tree_map[0])

    distance_left = [[0 for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    distance_right = [[0 for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    distance_down = [[0 for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    distance_up = [[0 for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    scenic_score = [[0 for _ in range(number_of_columns)] for _ in range(number_of_rows)]

    for row in range(0, number_of_rows):
        for col in range(0, number_of_columns):
            # looking left
            for c in range(col - 1, -1, -1):
                distance_left[row][col] += 1
                if tree_map[row][c] >= tree_map[row][col]:
                    break
            # looking right
            for c in range(col + 1, number_of_columns):
                distance_right[row][col] += 1
                if tree_map[row][c] >= tree_map[row][col]:
                    break
            # looking down
            for r in range(row + 1, number_of_rows):
                distance_down[row][col] += 1
                if tree_map[r][col] >= tree_map[row][col]:
                    break
            # looking up
            for r in range(row - 1, -1, -1):
                distance_up[row][col] += 1
                if tree_map[r][col] >= tree_map[row][col]:
                    break

    for r in range(0, number_of_rows):
        for c in range(0, number_of_columns):
            scenic_score[r][c] = distance_left[r][c] * distance_right[r][c] * distance_down[r][c] * distance_up[r][c]

    # max_scenic_score = 0
    # # for r in range(0, number_of_rows):
    # #     for c in range(0, number_of_columns):
    # #         if scenic_score[r][c] > max_scenic_score:
    # #             max_scenic_score = scenic_score[r][c]
    # for row in scenic_score:
    #     for value in row:
    #         if value > max_scenic_score:
    #             max_scenic_score = value

    max_scenic_score = max(max(row) for row in scenic_score)
    return max_scenic_score


if __name__ == '__main__':
    content = read_input_file()
    tree_map = process_input_lines(content)
    visible_trees = check_visible(tree_map)
    print(f'partI: {visible_trees= } ')

    max_score = viewing_distance(tree_map)
    print(f'partII: {max_score= } ')
