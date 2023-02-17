from typing import List, Tuple

# A, B, C = rock, paper, scissors for opponent
# X, Y, Z = rock, paper, scissors for ourselves for part I
# X, Y, Z = loose, draw, win strategy for part II

WIN_SCORE_TABLE = {("A", "X"): 3, ("A", "Y"): 6, ("A", "Z"): 0,
                   ("B", "X"): 0, ("B", "Y"): 3, ("B", "Z"): 6,
                   ("C", "X"): 6, ("C", "Y"): 0, ("C", "Z"): 3}
CHOICE_SCORE_TABLE = {"X": 1, "Y": 2, "Z": 3}

# This translates the strategy (X, Y, Z) to our own moves.
STRATEGY_TABLE = {("A", "X"): "Z", ("A", "Y"): "X", ("A", "Z"): "Y",
                  ("B", "X"): "X", ("B", "Y"): "Y", ("B", "Z"): "Z",
                  ("C", "X"): "Y", ("C", "Y"): "Z", ("C", "Z"): "X"}


def read_strategy_guide(file_name: str) -> List[Tuple[str, str]]:
    with open(file_name) as f:
        content = f.read().splitlines()

    return list(map(lambda line: (line.split(" ")[0], line.split(" ")[1]), content))


def compute_part_one(file_name: str) -> int:
    strategy_guide = read_strategy_guide(file_name)

    score = 0
    for [opponent_move, own_move] in strategy_guide:
        score += WIN_SCORE_TABLE[(opponent_move, own_move)] + CHOICE_SCORE_TABLE[own_move]

    return score


def compute_part_two(file_name: str) -> int:
    strategy_guide = read_strategy_guide(file_name)

    score = 0
    for [opponent_move, strategy_move] in strategy_guide:
        own_move = STRATEGY_TABLE[(opponent_move, strategy_move)]
        score += WIN_SCORE_TABLE[(opponent_move, own_move)] + CHOICE_SCORE_TABLE[own_move]

    return score


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input2.txt')}")
    print(f"Part II: {compute_part_two('input/input2.txt')}")
