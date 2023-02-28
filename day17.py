# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

# https://adventofcode.com/2022/day/17

from itertools import cycle


def init_rocks(y=0):
    rocks = []
    rocks.append({(2, y), (3, y), (4, y), (5, y)})
    rocks.append({(3, y), (2, y + 1), (3, y + 1), (4, y + 1), (3, y + 2)})
    rocks.append({(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)})
    rocks.append({(2, y), (2, y + 1), (2, y + 2), (2, y + 3)})
    rocks.append({(2, y), (3, y), (2, y + 1), (3, y + 1)})
    return rocks


def add_rock_to_tower(rock, tower):
    for r in rock:
        tower.current_path(r)
    return tower


def shift_rock(rock, x=0, y=0):
    shifted_rock = set()
    for r in rock:
        x_new = r[0] + x
        y_new = r[1] + y
        shifted_rock.add((x_new, y_new))
    return shifted_rock


def check_collision_with_walls(rock):
    collision = False
    for r in rock:
        if r[0] < 0 or r[0] > 6:
            collision = True
            return collision
    return collision


def check_collision_with_rocks(tower, rock):
    collision = False
    for r in rock:
        if r in tower:
            collision = True
            return collision
    return collision


def check_collision_with_bottom(rock):
    collision = False
    for r in rock:
        if r[1] <= 0:
            collision = True
            return collision
    return collision


def calculate_top_of_tower(tower, top):
    for r in tower:
        top = max(top, r[1])
    return top


def print_tower(tower, top):
    for y in range(top + 4, 0, -1):
        for x in range(7):
            if (x, y) in tower:
                print("#", end='')
            else:
                print(".", end='')
        print()
    print(f'top_of_tower= {top}')
    return


def detect_new_bottom(tower, top):
    detected = True
    for x in range(7):
        if (x, top) not in tower:
            detected = False
            return detected
    return detected


def init_tower():
    tower = set()
    return tower


def find_pattern(data: list[int]) -> tuple[list[int], list[int]]:
    """"
    this look for pattern in a list
    [r1, r2, r3, r4, a, b, c, a, b, c, a, b, c]
    it will return:
    [r1, r2, r3] and [a, b, c]
    """
    for p in range(len(data)):
        sd = data[p:]
        for r in range(2, len(sd) // 2):
            if sd[0:r] == sd[r:2 * r]:
                if all([(sd[0:r] == sd[y:y + r]) for y in range(r, len(sd) - r, r)]):
                    return data[:p], data[p:p + r]
    return [], []


def read_input_file(filename):
    with open(filename) as f:
        content = f.read().splitlines()
    return content


if __name__ == '__main__':
    filename = "input/input17.txt"
    jet_pattern = read_input_file(filename)

    """"
    get new rock
        step 1
        move rock <>
        check for collision with existing rocks in tower
        if collision do not make the move
        
        step 2
        move rock <>
        if collision with wall, do not make the move
        
        step 3
        move rock V
        check for collision with existing rocks in tower
        if collision; freeze rock and move to next rock
        
        step 4
        move rock V
        check for collision with bottom of tower
        if collision; freeze rock and move to next rock
        
        step 5
        move rock V to new position and go back to start.
    add rock to tower
    """

    top_of_tower = 0
    tower = init_tower()
    rock_cycle = cycle(init_rocks())
    direction_cycle = cycle(jet_pattern[0])
    top_of_tower_list = []
    number_of_samples = 10000

    for _ in range(number_of_samples):  # cycle falling rocks, sample size must be large enough to detect a cycle-pattern
        rock = next(rock_cycle)
        top_of_tower = calculate_top_of_tower(tower, top_of_tower)
        top_of_tower_list.append(top_of_tower)
        rock = shift_rock(rock, x=0, y=top_of_tower + 4)  # the next rock starts 4 units above the top
        collision = False
        drop_level = 0
        shift_direction = 0
        while not collision:  # cycle wind-direction
            direction = next(direction_cycle)
            x = -1 if direction == "<" else 1
            # step 1 move left or right
            shifted_rock = shift_rock(rock, x=x, y=0)
            collision1 = check_collision_with_rocks(tower, shifted_rock)
            collision2 = check_collision_with_walls(shifted_rock)
            # step 2 move left or right
            if not collision1 and not collision2:
                rock = shift_rock(rock, x=x, y=0)
                shift_direction += x

            # step 3 move down
            shifted_rock = shift_rock(rock, x=0, y=-1)
            collision1 = check_collision_with_rocks(tower, shifted_rock)
            collision2 = check_collision_with_bottom(shifted_rock)
            if collision1 or collision2:
                add_rock_to_tower(rock, tower)
                # tower_helper_list.append((rock_number, shift_direction, drop_level ))
                collision = True
                continue
            # step 4 move down
            # shifted_rock = shift_rock(rock, x=0, y=-1)
            # if collision:
            #     add_rock_to_tower(rock, tower)
            #     tower_helper_list.append((rock_number, shift_direction, drop_level ))
            #     continue
            # step 5 move down
            rock = shift_rock(rock, x=0, y=-1)
            drop_level += -1

    top_of_tower = calculate_top_of_tower(tower, top_of_tower)
    top_of_tower_list.append(top_of_tower)
    top_of_tower_differences = [top_of_tower_list[i + 1] - top_of_tower_list[i] for i in
                                range(len(top_of_tower_list) - 1)]

    print(f'partI: {top_of_tower= } ')
    print(f'{top_of_tower_list= }')
    print(f'{top_of_tower_differences= }')

    preamble, repetition = find_pattern(top_of_tower_differences)
    print(preamble)
    print(repetition)
    p_len = len(preamble)
    r_len = len(repetition)

    num_rocks = 2022
    height = sum(preamble) \
             + sum(repetition) * ((num_rocks - p_len) // r_len) \
             + sum(repetition[:((num_rocks - p_len) % r_len)])

    print(f'partI: {height= }')

    num_rocks = 1000000000000
    height = sum(preamble) \
             + sum(repetition) * ((num_rocks - p_len) // r_len) \
             + sum(repetition[:((num_rocks - p_len) % r_len)])

    print(f'partII: {height= }')
