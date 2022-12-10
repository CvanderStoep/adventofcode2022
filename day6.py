# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

def read_input_file():
    filename = "input/input6.txt"

    with open(filename) as f:
        content = f.read().splitlines()

    datastream = content[0]
    start_of_packet_marker = 0
    sequence_found = False
    while not sequence_found:
        current_data_stream = datastream[start_of_packet_marker: start_of_packet_marker + 4]

        # convert the current stream to a set containing only unique letters

        if len(set(current_data_stream)) == 4:  # start found
            break
        start_of_packet_marker += 1

        # sequence_found = True
        # for i in range(1,4):
        #     next_letter = current_data_stream[i]
        #     if next_letter in current_data_stream[0:i]:
        #         sequence_found = False
        #         break
        # start_of_packet_marker += 1
    print(f'partI: start of packet', start_of_packet_marker + 4)


    # part II
    # print('partI: number of overlapping assignments= ', number_of_overlapping_assignments)


if __name__ == '__main__':
    read_input_file()
