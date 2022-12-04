def read_input_file():
    # extra empty line added to the input file to avoid corned cases
    filename = "input/input1test.txt"

    with open(filename) as f:
        content = f.read().splitlines()

    sumOfCalories = 0
    totalCalories = []

    for line in content:
        if len(line) == 0:
            totalCalories.append(sumOfCalories)
            sumOfCalories = 0
        else:
            sumOfCalories += int(line)

    totalCalories.sort(reverse=True)

    # part I
    print('Number of calories of the Elve that carries the most calories:', totalCalories[0])

    # part II
    sumOfHighestTreeElves = totalCalories[0] + totalCalories[1] + totalCalories[2]
    print('Sum of calories of highest three Elves:', sumOfHighestTreeElves)


if __name__ == '__main__':
    read_input_file()
