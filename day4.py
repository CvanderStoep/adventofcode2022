# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE that is a constant

def read_input_file():
    filename = "input/input4.txt"

    with open(filename) as f:
        content = f.read().splitlines()

    number_of_overlaps = 0
    for item in content:
        sections = item.split(',')
        section1, section2 = sections[0], sections[1]
        ranges = section1.split('-')
        section1Left, section1Right = int(ranges[0]), int(ranges[1])
        ranges = section2.split('-')
        section2Left, section2Right = int(ranges[0]), int(ranges[1])

        if (section1Left <= section2Left and section2Right <= section1Right) or \
                (section2Left <= section1Left and section1Right <= section2Right):
            number_of_overlaps += 1

    # part I
    print('partI: number of fully overlapping ranges= ', number_of_overlaps)

    # part II


if __name__ == '__main__':
    read_input_file()
