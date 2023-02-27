"""
advent of code 2022
https://adventofcode.com/2022
"""

from typing import List


def read_snafu_numbers(file_name: str) -> List[int]:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content

def convert_snafu_to_digital(snafu: str) -> int:

    snafu = list(snafu)
    snafu.reverse()
    digital_number = 0
    for i, sn_digit in enumerate(snafu):
        match sn_digit:
            case "2":
                number = 2
            case "1":
                number = 1
            case "0":
                number = 0
            case "-":
                number = -1
            case "=":
                number = -2
        digital_number += number * 5**i

    return digital_number



def decimal_to_snafu(decimal: int) -> str:
    trans_rev = {
        4: '-',
        3: '=',
        2: '2',
        1: '1',
        0: '0'
    }
    snafu = ''
    while decimal > 0:
        rem, decimal = decimal % 5, round(decimal / 5)
        snafu += trans_rev[rem]
    return snafu[::-1]


def compute_part_one(file_name: str) -> int:
    snafu_numbers = read_snafu_numbers(file_name)

    sum_of_snafu_numbers = 0
    for snafu in snafu_numbers:
        sum_of_snafu_numbers += convert_snafu_to_digital(snafu)

    print(decimal_to_snafu(sum_of_snafu_numbers))

    return sum_of_snafu_numbers


def compute_part_two(file_name: str) -> int:
    snafu_numbers = read_snafu_numbers(file_name)
    return snafu_numbers


if __name__ == '__main__':
    decimal_to_snafu(25)
    print(f"Part I: {compute_part_one('input/input25.txt')}")
    # print(f"Part II: {compute_part_two('input/input1.txt')}")
