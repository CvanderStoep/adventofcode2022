"""
advent of code 2022
https://adventofcode.com/2022
"""

from typing import List


def read_calories_per_elf(file_name: str) -> List[int]:
    with open(file_name) as f:
        content = f.read().splitlines()

    sumOfCalories = 0
    totalCalories = []

    for line in content:
        if len(line) == 0:
            totalCalories.append(sumOfCalories)
            sumOfCalories = 0
        else:
            sumOfCalories += int(line)
    totalCalories.append(sumOfCalories)

    totalCalories.sort()
    return totalCalories


def compute_part_one(file_name: str) -> int:
    calories_per_elf = read_calories_per_elf(file_name)
    return calories_per_elf[0]


def compute_part_two(file_name: str) -> int:
    calories_per_elf = read_calories_per_elf(file_name)
    return calories_per_elf[0] + calories_per_elf[1] + calories_per_elf[2]


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input1.txt')}")
    print(f"Part II: {compute_part_two('input/input1.txt')}")
