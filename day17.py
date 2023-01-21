# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

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
        tower.add(r)
    return tower


def shift_rock(rock, x=0, y=0):
    #  TODO separate shift and check collision with wall
    shifted_rock = set()
    for r in rock:
        x_new = r[0] + x
        y_new = r[1] + y
        if x_new < 0 or x_new > 6:
            return rock
        shifted_rock.add((x_new, y_new))

    return shifted_rock

def check_collision_with_walls(rock):
    #  TODO separate shift and check collision with wall
    collision = False
    return collision


def check_collision_with_rocks(tower, rock):
    collision = False
    for r in rock:
        if r in tower:
            collision = True
            # print('collision in tower')
            return collision
    return collision


def check_collision_with_bottom(rock):
    collision = False
    for r in rock:
        if r[1] <= 0:
            collision = True
            # print('collision with bottom')
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


def init_tower():
    tower = set()
    return tower


def read_input_file(filename):
    with open(filename) as f:
        content = f.read().splitlines()
    return content


if __name__ == '__main__':
    filename = "input/input17.txt"
    jet_pattern = read_input_file(filename)
    print(jet_pattern)

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

    for _ in range(2022):  # cycle falling rocks
        rock = next(rock_cycle)
        top_of_tower = calculate_top_of_tower(tower, top_of_tower)
        rock = shift_rock(rock, x=0, y=top_of_tower + 4)  # the next rock starts 4 units above the top
        collision = False
        while not collision:  # cycle wind-direction
            direction = next(direction_cycle)
            x = -1 if direction == "<" else 1
            # step 1 move left or right
            shifted_rock = shift_rock(rock, x=x, y=0)
            collision = check_collision_with_rocks(tower, shifted_rock)
            # TODO
            # collision = check collision with walls

            # step 2 move left or right
            if not collision:
                rock = shift_rock(rock, x=x, y=0)
            # step 3 move down
            shifted_rock = shift_rock(rock, x=0, y=-1)
            collision = check_collision_with_rocks(tower, shifted_rock)
            if collision:
                add_rock_to_tower(rock, tower)
                continue
            # step 4 move down
            shifted_rock = shift_rock(rock, x=0, y=-1)
            collision = check_collision_with_bottom(shifted_rock)
            if collision:
                add_rock_to_tower(rock, tower)
                continue
            # step 5 move down
            rock = shift_rock(rock, x=0, y=-1)

    top_of_tower = calculate_top_of_tower(tower, top_of_tower)
    # print_tower(tower, top_of_tower)

    print(f'partI: {top_of_tower= } ')
    print(f'partII:  ')
