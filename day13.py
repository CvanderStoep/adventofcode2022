# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)
import json
from functools import cmp_to_key


def read_input_file(filename):
    with open(filename) as f:
        content = f.read().split('\n\n')
    return list(map(lambda block: block.split('\n'), content))


def compare_packets(left_packet, right_packet) -> int:
    if type(left_packet) is int and type(right_packet) is int:
        if left_packet < right_packet:
            return -1
        if right_packet < left_packet:
            return 1
        return 0

    if type(left_packet) is int:
        return compare_packets([left_packet], right_packet)

    if type(right_packet) is int:
        return compare_packets(left_packet, [right_packet])

    if len(left_packet) == 0 and len(right_packet) == 0:
        return 0

    if len(left_packet) == 0:
        return -1

    if len(right_packet) == 0:
        return 1

    comparison = compare_packets(left_packet[0], right_packet[0])
    match comparison:
        case -1:
            return -1
        case 1:
            return 1
        case 0:
            return compare_packets(left_packet[1:], right_packet[1:])
        case _:
            print('mag niet gebeuren')


if __name__ == '__main__':
    filename = "input/input13test.txt"
    content = read_input_file(filename)
    print(content)
    sum_of_indices = 0
    for i, c in enumerate(content):
        print(c)
        left_packet = json.loads(c[0])
        right_packet = json.loads(c[1])
        if compare_packets(left_packet, right_packet) == -1:
            sum_of_indices += i + 1

    print(f'partI: {sum_of_indices= }')
    flatten_content = []
    for c in content:
        flatten_content.extend([json.loads(c[0]), json.loads(c[1])])

    flatten_content.append([[2]])
    flatten_content.append([[6]])

    flatten_content.sort(key=cmp_to_key(compare_packets))
    print(flatten_content)

    first_index = flatten_content.index([[2]]) + 1
    second_index = flatten_content.index([[6]]) + 1
    decoder_key = first_index * second_index

    print(f'partII: {decoder_key= } ')
