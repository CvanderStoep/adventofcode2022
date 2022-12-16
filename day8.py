# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)


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


def check_visible(map):
    number_of_rows = len(map)
    number_of_columns = len(map[0])

    visible_left = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    visible_right = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    visible_top = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    visible_bottom = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    visible = [[True for _ in range(number_of_columns)] for _ in range(number_of_rows)]

    # TODO alternative could be to put visible on True,
    # check all the views, but only if visible is False so far; otherwise skip

    for row in range(1, number_of_rows - 1):
        for col in range(1, number_of_columns - 1):
            # left view
            for c in range(0, col):
                if map[row][c] >= map[row][col]:
                    visible_left[row][col] = False
                    break
            # right view
            for c in range(col + 1, number_of_columns):
                if map[row][c] >= map[row][col]:
                    visible_right[row][col] = False
                    break
            # top view
            for r in range(0, row):
                if map[r][col] >= map[row][col]:
                    visible_top[row][col] = False
                    break
            # bottom view
            for r in range(row + 1, number_of_rows):
                if map[r][col] >= map[row][col]:
                    visible_bottom[row][col] = False
                    break

    total_visible_trees = 0
    for r in range(0, number_of_rows):
        for c in range(0, number_of_columns):
            visible[r][c] = visible_left[r][c] | visible_right[r][c] | visible_top[r][c] | visible_bottom[r][c]
            if visible[r][c]:
                total_visible_trees += 1

    return total_visible_trees


def viewing_distance(map):
    number_of_rows = len(map)
    number_of_columns = len(map[0])

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
                if map[row][c] >= map[row][col]:
                    break
            # looking right
            for c in range(col + 1, number_of_columns):
                distance_right[row][col] += 1
                if map[row][c] >= map[row][col]:
                    break
            # looking down
            for r in range(row + 1, number_of_rows):
                distance_down[row][col] += 1
                if map[r][col] >= map[row][col]:
                    break
            # looking up
            for r in range(row - 1, -1, -1):
                distance_up[row][col] += 1
                if map[r][col] >= map[row][col]:
                    break

    for r in range(0, number_of_rows):
        for c in range(0, number_of_columns):
            scenic_score[r][c] = distance_left[r][c] * distance_right[r][c] * distance_down[r][c] * distance_up[r][c]

    max_scenic_score = 0
    for r in range(0, number_of_rows):
        for c in range(0, number_of_columns):
            if scenic_score[r][c] > max_scenic_score:
                max_scenic_score = scenic_score[r][c]

    return max_scenic_score


if __name__ == '__main__':
    content = read_input_file()
    map = process_input_lines(content)
    visible_trees = check_visible(map)
    print(f'partI: {visible_trees= } ')

    max_score = viewing_distance(map)
    print(f'partII: {max_score= } ')
