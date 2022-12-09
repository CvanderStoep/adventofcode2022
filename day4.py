# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

def read_input_file():
    filename = "input/input4.txt"

    with open(filename) as f:
        content = f.read().splitlines()

    number_of_overlaps = 0
    number_of_overlapping_assignments = 0
    for item in content:
        sections = item.split(',')
        section1, section2 = sections[0], sections[1]
        ranges = section1.split('-')
        L1, R1 = int(ranges[0]), int(ranges[1])
        ranges = section2.split('-')
        L2, R2 = int(ranges[0]), int(ranges[1])

        # part I
        if (L1 <= L2 and R2 <= R1) or (L2 <= L1 and R1 <= R2):
            number_of_overlaps += 1

        # part II
        if (L2 <= L1 <= R2) or (L2 <= R1 <= R2) or (L1 <= L2 <= R1) or (L1 <= R2 <= R1):
            number_of_overlapping_assignments += 1

    # part I
    print('partI: number of fully overlapping ranges= ', number_of_overlaps)

    # part II
    print('partI: number of overlapping assignments= ', number_of_overlapping_assignments)


if __name__ == '__main__':
    read_input_file()
