# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def read_input_file():
    filename = "input/input9test.txt"
    with open(filename) as f:
        content = f.read().splitlines()
    return content


def process_input_lines(input_lines):
    commands = []
    for line in input_lines:
        direction, amount = line.split(" ")
        commands.append([direction, amount])
    return commands


def update_head_position(head, direction):
    match direction:
        case "R":
            head.x += 1
        case "L":
            head.x -= 1
        case "U":
            head.y += 1
        case "D":
            head.y -= 1


def update_tail_position(head, tail, tail_positions):
    if abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1:
        pass
    elif head.y == tail.y:  # head and tail on a horizontal line
        if head.x > tail.x:
            tail.x += 1
        else:
            tail.x -= 1
    elif head.x == tail.x:  # head and tail on a vertical line
        if head.y > tail.y:
            tail.y += 1
        else:
            tail.y -= 1
    elif head.x > tail.x and head.y > tail.y:
        tail.x += 1
        tail.y += 1
    elif head.x > tail.x and head.y < tail.y:
        tail.x += 1
        tail.y -= 1
    elif head.x < tail.x and head.y > tail.y:
        tail.x -= 1
        tail.y += 1
    elif head.x < tail.x and head.y < tail.y:
        tail.x -= 1
        tail.y -= 1
    tail_positions.append([tail.x, tail.y])


def update_positions(commands, head, tail, tail_positions):
    for command in commands:
        direction = command[0]
        amount = int(command[1])
        for _ in range(amount):
            update_head_position(head, direction)
            update_tail_position(head, tail, tail_positions)


if __name__ == '__main__':
    content = read_input_file()
    commands = process_input_lines(content)
    # x, y starting coordinates
    head = Point(0, 0)
    tail = Point(0, 0)
    tail_positions = []
    update_positions(commands, head, tail, tail_positions)

    # convert the list of position to a set of unique positions
    set_of_tail_positions = set()
    for p in tail_positions:
        set_of_tail_positions.add((p[0], p[1]))

    print(tail_positions)
    print(set_of_tail_positions)

    print(f'partI: number of tail positions {len(set_of_tail_positions)} ')

    print(f'partII:  ')
