def calculatePriority(letter):
    priority = ord(letter)
    if priority >= 97:  # a - z
        priority -= 96
    else:  # A - Z
        priority -= 38
    return priority


def read_input_file():
    filename = "input/input3.txt"

    with open(filename) as f:
        content = f.read().splitlines()

    # part I
    prioritySum = 0
    for item in content:
        half_string_length = int(len(item) / 2)
        firstCompartment = item[0:half_string_length]
        secondCompartment = item[half_string_length:]
        compartmentOverlap = list(set(firstCompartment).intersection(secondCompartment))[0]

        prioritySum += calculatePriority(compartmentOverlap)

    print('partI: sum of priorities= ', prioritySum)

    # part II
    counter = 0
    prioritySum = 0
    while counter < len(content):
        line1 = set(content[counter])
        line2 = set(content[counter + 1])
        line3 = set(content[counter + 2])
        counter += 3
        badge = list(line1 & line2 & line3)[0] # take the intersection of the 3 lines (sets)
        prioritySum += calculatePriority(badge)

    print('partII: sum of priorities= ', prioritySum)


if __name__ == '__main__':
    read_input_file()
