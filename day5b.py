# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)
stack_of_crates = [[], ['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'],
                   ['N', 'B', 'L'],
                   ['J', 'C', 'H', 'T', 'L', 'V'],
                   ['S', 'P', 'J', 'W'],
                   ['Z', 'S', 'C', 'F', 'T', 'L', 'R'],
                   ['W', 'D', 'G', 'B', 'H', 'N', 'Z'],
                   ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'],
                   ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'],
                   ['R', 'P', 'M', 'L', 'H']]


def read_input_file():
    filename = "input/input5.txt"

    with open(filename) as f:
        content = f.read().splitlines()

    # part II
    for item in content:
        if item.startswith('move') is False:
            continue
        else:
            _, number_of_moves, _, stack_from, _, stack_to = item.split(' ')
            number_of_moves = int(number_of_moves)
            stack_to = int(stack_to)
            stack_from = int(stack_from)
            temporary_stack = []  # first move the crates in a temporaty stack to retain order later
            for _ in range(number_of_moves):
                crate = stack_of_crates[stack_from].pop()
                temporary_stack.append(crate)
            for _ in range(number_of_moves):
                crate = temporary_stack.pop()
                stack_of_crates[stack_to].append(crate)

    crates_on_top = ""
    for stack_number in range(1, len(stack_of_crates)):
        crate = stack_of_crates[stack_number].pop()
        crates_on_top += crate

    print(f'partII: {crates_on_top=}')


if __name__ == '__main__':
    read_input_file()
