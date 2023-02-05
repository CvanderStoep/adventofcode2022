# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

# https://adventofcode.com/2022/day/20
from dataclasses import dataclass
import itertools
from itertools import cycle
import re


def read_input_file(filename, key):
    with open(filename) as f:
        content = f.read().splitlines()
        content = [int(v) * key for v in content]
    return content


if __name__ == '__main__':
    filename = "input/input20.txt"
    decription_key = 811589153  # part I
    # decription_key = 1  # part II
    original_list= read_input_file(filename, decription_key)
    zero = (original_list.index(0), 0)

    # you need to include the index as well as the files includes duplicate numbers
    original_list = [a for a in enumerate(original_list)]
    moved_list = original_list.copy()
    length = len(moved_list) - 1

    for _ in range(10):  # part II, for part I; only run this once.
        for ii in original_list:
            idx_old = moved_list.index(ii)
            moved_list.remove(ii)
            idx_new = (idx_old + ii[1] + length) % length  # make sure it is positive and modulo
            moved_list.insert(idx_new, ii)

    nul_index = moved_list.index(zero)
    print(f'{nul_index= }')
    thousand = (nul_index + 1000) % len(moved_list)
    two_thousand = (nul_index + 2000) % len(moved_list)
    three_thousand = (nul_index + 3000) % len(moved_list)

    answerI = moved_list[thousand][1] + moved_list[two_thousand][1] + moved_list[three_thousand][1]

    print(f'partI: {answerI= }')
    print(f'partII:')
