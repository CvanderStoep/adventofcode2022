# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

def read_input_file():
    filename = "input/input4.txt"

    with open(filename) as f:
        content = f.read().splitlines()

    number_of_overlaps = 0
    for item in content:
        sections = item.split(',')
        section1, section2 = sections[0], sections[1]
        ranges = section1.split('-')
        section1_left, section1_right = int(ranges[0]), int(ranges[1])
        ranges = section2.split('-')
        section2_left, section2_right = int(ranges[0]), int(ranges[1])

        if (section1_left <= section2_left and section2_right <= section1_right) or \
                (section2_left <= section1_left and section1_right <= section2_right):
            number_of_overlaps += 1

    # part I
    print('partI: number of fully overlapping ranges= ', number_of_overlaps)

    # part II


if __name__ == '__main__':
    read_input_file()
