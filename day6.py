# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

def read_input_file():
    filename = "input/input6.txt"
    MARKER_LENGTH = 14

    with open(filename) as f:
        content = f.read().splitlines()

    datastream = content[0]
    start_of_packet_marker = 0
    sequence_found = False
    while not sequence_found:
        current_data_stream = datastream[start_of_packet_marker: start_of_packet_marker + MARKER_LENGTH]

        # convert the current stream to a set containing only unique letters

        if len(set(current_data_stream)) == MARKER_LENGTH:  # start found
            break
        start_of_packet_marker += 1

    print(f'partI: start of packet', start_of_packet_marker + MARKER_LENGTH)


    # part II
    # set markerlength to 4 or 14 for partI and partII respectively


if __name__ == '__main__':
    read_input_file()
