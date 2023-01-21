"""
Advent of Code 2022 Day 17
"""
import sys

from itertools import cycle

# from advent_tools import get_daily_input

DAY = 17

TEST = sys.argv[1] == "test" if len(sys.argv) > 1 else False
TEST = True

TEST_DATA = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

if TEST:
    def get_daily_input(_):
        for line in TEST_DATA.strip().split("\n"):
            a = line.strip("\n")
            yield line.strip("\n")


class RockPile:
    rock_shapes = {
        "line": [
            "0011110",
        ],
        "cross": [
            "0001000",
            "0011100",
            "0001000",
        ],
        "elbow": [
            "0000100",
            "0000100",
            "0011100",
        ],
        "column": [
            "0010000",
            "0010000",
            "0010000",
            "0010000",
        ],
        "square": [
            "0011000",
            "0011000",
        ]
    }

    def __init__(self, wind_directions: str):
        self.wind_direction = cycle(wind_directions)
        self.rock_shape = cycle(self.rock_shapes)
        self.pile: list[int] = []

    @property
    def height(self) -> int:
        return len(self.pile)

    def can_shift(self, direction: str, pile_level: int, rock: list[int]) -> bool:
        for r in range(len(rock)):
            if (
                    direction == ">" and
                    ((rock[r] & 1) or (rock[r] >> 1 & self.pile[pile_level + r]))
            ) or (
                    direction == "<" and
                    ((rock[r] & 2 ** 6) or (rock[r] << 1 & self.pile[pile_level + r]))
            ):
                return False
        return True

    def can_fall(self, pile_level: int, rock: list[int]) -> bool:
        for r in range(len(rock)):
            if ((pile_level + r >= len(self.pile) - 1) or
                    (rock[r] & self.pile[pile_level + r + 1])):
                return False
        return True

    def drop_next(self) -> None:
        rock = [int(i, 2) for i in self.rock_shapes[next(self.rock_shape)]]
        self.pile = [0] * (3 + len(rock)) + self.pile
        for pile_level in range(len(self.pile)):
            direction = next(self.wind_direction)

            if self.can_shift(direction, pile_level, rock):
                for r in range(len(rock)):
                    rock[r] = rock[r] >> 1 if direction == ">" else rock[r] << 1

            if not self.can_fall(pile_level, rock):
                for r in range(len(rock)):
                    self.pile[pile_level + r] = self.pile[pile_level + r] | rock[r]
                while self.pile[0] == 0:
                    self.pile.pop(0)
                return

    def dump(self) -> str:
        output = ""
        for r in self.pile:
            output += "|" + \
                      "".join(["#" if c == "1" else "." for c in format(r, "07b")]) + \
                      "|\n"
        output += "+-------+"
        return output


def find_pattern(data: list[int]) -> tuple[list[int], list[int]]:
    for p in range(len(data)):
        sd = data[p:]
        for r in range(2, len(sd) // 2):
            if sd[0:r] == sd[r:2 * r]:
                if all([(sd[0:r] == sd[y:y + r]) for y in range(r, len(sd) - r, r)]):
                    return data[:p], data[p:p + r]
    return [], []


def part_1() -> int:
    pile = RockPile(next(get_daily_input(DAY)))
    for _ in range(2022):
        pile.drop_next()
    return pile.height


def part_2() -> int:
    num_rocks = 1000000000000
    sample_size = 10000

    pile = RockPile(next(get_daily_input(DAY)))

    height_deltas = []
    for _ in range(sample_size):
        prev_height = pile.height
        pile.drop_next()
        height_deltas.append(pile.height - prev_height)

    preamble, repetition = find_pattern(height_deltas)
    p_len = len(preamble)
    r_len = len(repetition)

    return sum(preamble) \
           + sum(repetition) * ((num_rocks - p_len) // r_len) \
           + sum(repetition[:((num_rocks - p_len) % r_len)])


def main():
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")


if __name__ == "__main__":
    main()