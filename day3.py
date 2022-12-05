def read_input_file():
    filename = "input/input3.txt"

    with open(filename) as f:
        content = f.read().splitlines()

    prioritySum = 0
    for item in content:
        half_string_length = int(len(item) / 2)
        firstCompartment = item[0:half_string_length]
        secondCompartment = item[half_string_length:]
        compartmentOverlap = list(set(firstCompartment).intersection(secondCompartment))[0]
        priority = ord(compartmentOverlap)
        if priority >= 97:      # a - z
            priority -= 96
        else:                   # A - Z
            priority -= 38
        prioritySum += priority

    # part I
    print('partI: sum of priorities= ', prioritySum)

    # part II


if __name__ == '__main__':
    read_input_file()
