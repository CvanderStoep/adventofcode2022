def read_input_file():
    filename = "input/input2.txt"

    # A, B, C = rock, paper, scissors player 1
    # X, Y, Z = rock, paper, scissors player 2
    # X, Y, Z = loose, draw, win strategy for part II

    with open(filename) as f:
        content = f.read().splitlines()

    choiceValue = {"X": 1, "Y": 2, "Z": 3}
    scoreTable = {}
    scoreTable[("A", "X")] = 3
    scoreTable[("A", "Y")] = 6
    scoreTable[("A", "Z")] = 0
    scoreTable[("B", "X")] = 0
    scoreTable[("B", "Y")] = 3
    scoreTable[("B", "Z")] = 6
    scoreTable[("C", "X")] = 6
    scoreTable[("C", "Y")] = 0
    scoreTable[("C", "Z")] = 3

    # part II
    TranslationTable = {} # this translates the strategy (X, Y, Z) to player2's choice.
    TranslationTable[("A", "X")] = "Z"
    TranslationTable[("A", "Y")] = "X"
    TranslationTable[("A", "Z")] = "Y"
    TranslationTable[("B", "X")] = "X"
    TranslationTable[("B", "Y")] = "Y"
    TranslationTable[("B", "Z")] = "Z"
    TranslationTable[("C", "X")] = "Y"
    TranslationTable[("C", "Y")] = "Z"
    TranslationTable[("C", "Z")] = "X"

    totalScore = 0
    totalScore2 = 0

    for line in content:
        # part I
        player1, player2 = line.split(" ")
        totalScore += scoreTable[(player1, player2)] + choiceValue[player2]
        # part II
        player2 = TranslationTable[(player1, player2)]
        totalScore2 += scoreTable[(player1, player2)] + choiceValue[player2]

    # part I
    print(f'totalscore part I= {totalScore}')
    # part II
    print(f'totalscore part II= {totalScore2}')


if __name__ == '__main__':
    read_input_file()
