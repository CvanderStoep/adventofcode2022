# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

class Monkey:
    def __init__(self, divisible=1, action_true=0, action_false=0):
        self.items = []
        self.divisible = divisible
        self.action_true = action_true
        self.action_false = action_false
        self.operation = []
        self.number_of_inspections = 0


def read_input_file():
    filename = "input/input11.txt"
    with open(filename) as f:
        content = f.read().splitlines()
    return content


def process_input_lines(input_lines):
    commands = []
    for line in input_lines:
        split_line = line.split(" ")
        commands.append(split_line)
    return commands


def process_content(content):
    # for command in commands:
    #     print(command)
    position = 0
    monkey_list = []

    while position < len(content) - 1:
        monkey = Monkey()
        monkey_list.append(monkey)
        position += 1
        items = content[position].split(":")[1].split(",")  # starting items
        for item in items:
            monkey.items.append(int(item))

        position += 1
        operations = content[position].split("=")[1].split(" ")  # operation

        monkey.operation.append(operations[2])
        monkey.operation.append((operations[3]))

        position += 1
        divisible = content[position].split("by")[1]  # divisible
        monkey.divisible = int(divisible)

        position += 1
        action = content[position].split(" ")[-1]  # true
        monkey.action_true = int(action)

        position += 1
        action = content[position].split(" ")[-1]  # false
        monkey.action_false = int(action)

        position += 2

    return monkey_list


def process_operation(monkey, worry_level):
    item_operator = monkey.operation[0]
    item_number = monkey.operation[1]

    if item_number == 'old':
        item_number = worry_level
    else:
        item_number = int(item_number)

    if item_operator == '+':
        worry_level = worry_level + item_number
    else:
        worry_level = worry_level * item_number

    return worry_level


def monkey_round(monkey_list, part):
    ggv = 1
    for monkey in monkey_list:
        ggv = ggv * monkey.divisible

    for monkey in monkey_list:
        for item in monkey.items:
            monkey.number_of_inspections += 1
            worry_level = item
            worry_level = process_operation(monkey, worry_level)
            if part == 1:
                worry_level = worry_level // 3  # needed for part I
            else:
                worry_level = worry_level % ggv  # needed for part II
            divisible = worry_level % monkey.divisible == 0
            if divisible:
                monkey_list[monkey.action_true].items.append(worry_level)
            else:
                monkey_list[monkey.action_false].items.append(worry_level)

        monkey.items = []


if __name__ == '__main__':
    content = read_input_file()
    # commands = process_input_lines(content)

    monkey_list = process_content(content)

    part, number_of_rounds = 1, 20
    part, number_of_rounds = 2, 10000

    for i in range(1, number_of_rounds + 1):
        monkey_round(monkey_list, part)

    monkey_inspection_list = []
    for monkey in monkey_list:
        monkey_inspection_list.append(monkey.number_of_inspections)
    monkey_inspection_list.sort(reverse=True)

    print(monkey_inspection_list)
    monkey_business = monkey_inspection_list[0] * monkey_inspection_list[1]

    print(f'partI:  {monkey_business= }')

    print(f'partII:  ')
