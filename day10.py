# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)


def read_input_file():
    filename = "input/input10.txt"
    with open(filename) as f:
        content = f.read().splitlines()
    return content


def process_input_lines(input_lines):
    commands = []
    for line in input_lines:
        split_line = line.split(" ")
        commands.append(split_line)
    return commands


def process_commands(commands):
    cycle = 0
    x_register = 1
    register_dictionary = {}

    for command in commands:
        instruction = command[0]
        if instruction == "noop":
            cycle += 1
            register_dictionary[cycle] = x_register
        else:
            value = int(command[1])
            for _ in range(2):
                cycle += 1
                register_dictionary[cycle] = x_register
            x_register += value

    return register_dictionary


if __name__ == '__main__':
    content = read_input_file()
    commands = process_input_lines(content)
    register = process_commands(commands)  # value of the register during the cycle
    print(f'{register= }')

    signal_strength = 0
    for i in range(20, 225, 40):
        signal_strength += i * register[i]

    print(f'partI: {signal_strength= } ')

    print(f'partII:  ')

    for cycle in range(1, 241):
        sprite = register[cycle]
        position = (cycle - 1) % 40
        if abs(sprite - position) <= 1:
            print('#', end='')
        else:
            print('.', end='')
        if cycle % 40 == 0:
            print()

