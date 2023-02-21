# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

""""
-->j
|
i  elf[i,j]
\/

check for each elf if there are neighbours
process proposed move for each elf
check for double claims (2 or more elves to the same location)
process only the single claims
repeat until no elves move anymore

"""

from collections import Counter

directions = ["N", "S", "W", "E"]

def rotate_directions(directions):

    new_directions = directions[1:]
    new_directions.append(directions[0])

    return new_directions

def read_input_file(filename):
    with open(filename) as f:
        content = f.read().splitlines()

    positions = []
    for i, line in enumerate(content):
        for j, c in enumerate(line):
            if c == "#":
                positions.append((i,j))

    return positions

def nearby(elf):
    """"
    check for the 8 neighbouring positions
    """
    i, j = elf[0], elf[1]
    vals = [(i - 1, j), (i - 1, j - 1), (i - 1, j + 1),
            (i + 1, j), (i + 1, j - 1), (i + 1, j + 1),
            (i, j - 1), (i, j + 1)]
    return vals

def look_around(direction, elf):
    """"
    check for the 3 valid positions in the given direction
    """

    i, j = elf[0], elf[1]
    match direction:
        case "N":
            vals = [(i-1, j), (i-1, j-1), (i-1, j+1)]
        case "E":
            vals = [(i, j+1), (i+1, j+1), (i-1, j+1)]
        case "S":
            vals = [(i+1, j), (i+1, j-1), (i+1, j+1)]
        case "W":
            vals = [(i, j-1), (i+1, j-1), (i-1, j-1)]

    return vals

def next_step(direction, elf):
    i, j = elf[0], elf[1]
    match direction:
        case "N":
            vals = [i-1, j]
        case "E":
            vals = [i, j+1]
        case "S":
            vals = [i+1, j]
        case "W":
            vals = [i, j-1]

    return tuple(vals)

def print_scan(elves):
    elf_j = [elf[1] for elf in elves]
    elf_i = [elf[0] for elf in elves]

    for i in range(min(elf_i), max(elf_i) + 1):
        for j in range((min(elf_j)), max(elf_j) + 1):
            if (i,j) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    print('')


if __name__ == '__main__':
    filename = "input/input23.txt"
    part1 = False
    elves = read_input_file(filename)
    print_scan(elves)

    rounds = 0
    has_moved = True  # if no elf has moved, stop the process
    while has_moved:
        elves_set = set(elves)
        has_moved = False
        rounds += 1
        new_positions = [None] * len(elves)
        for i, elf in enumerate(elves):
            for nearby_elf in nearby(elf):
                if nearby_elf in elves_set:  # if there exist a neighbouring elf, continue to next step
                    has_moved = True
                    for direction in directions:
                        for ne in look_around(direction, elf):
                            if ne in elves_set:
                                break
                        else:
                            new_positions[i] = next_step(direction, elf)
                            break
                    break

        # check for double claims on the same position
        counts = Counter(new_positions)
        for i, elf in enumerate(new_positions):
            if counts[elf] == 1:
                elves[i] = elf

        # outcome for Part I, break after 10 rounds
        if part1 and rounds == 10:
            break

        if rounds % 10 == 0:
            print(rounds)
        directions = rotate_directions(directions)

    # calculate maximum grid size
    x_coordinates = [a[0] for a in elves]
    y_coordinates = [a[1] for a in elves]
    area = (max(x_coordinates) - min(x_coordinates) + 1) * \
           (max(y_coordinates) - min(y_coordinates) + 1)
    area = area - len(elves)
    print_scan(elves)

    if part1:
        print(f'partI: {area= }')
    else:
        print(f'partII: {rounds= }')
