# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

""""
---> i
|
j   maze[j][i]
\/
"""
import queue

def valid_move(maze, moves):
    start = [key for key, value in maze.items() if value == "O"]
    i = start[0][1]
    j = 0
    # lenm = len(moves)
    # if lenm % 10 == 0:
    #     print(f'{len(moves)= }')

    rows, cols = maze_size(maze)
    # rows, cols = 27, 122

    t = 0  # starting time
    for move in moves:
        t += 1
        # shifted_maze = maze_shift(maze, t)
        shifted_maze = shifted_maze_list[t]
        # if t%5 == 0:
        #     printMaze(shifted_maze)
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        elif move == "W":
            pass
        if not (0 <= i < cols and 0 <= j < rows):
            return False
        elif shifted_maze.get((j,i)) in ("#", ">", "<", "v", "^", "O"):
            return False

    return True

def printMaze(maze, path=""):
    start = [key for key, value in maze.items() if value == "O"]
    i = start[0][1]
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        elif move == "W":
            pass
        pos.add((j, i))

    rows, cols = maze_size(maze)
    # rows, cols = 27, 122


    for j in range(rows):
        for i in range(cols):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(maze.get((j,i), ".") +  " ", end="")
        print()


def find_exit(maze, moves):
    """"
    check if the current moves lead to the exit
    as the start and exit are fixed in time, no need to shift the maze
    """
    start = [key for key, value in maze.items() if value == "O"]
    i = start[0][1]
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        elif move == "W":
            pass

    if maze.get((j,i)) == "X":
        print("Found: " + moves)
        print(f'{len(moves)= }')
        printMaze(maze, moves)
        # with open("input/output24.txt", "w") as f:
        #     f.writelines("Found: " + moves)
        #     f.writelines("\n")
        #     f.writelines(f'{len(moves)= }')

        return True
    return False

def find_position(maze, moves):
    """"
    find the (j,i) position after a series of moves
    """
    start = [key for key, value in maze.items() if value == "O"]
    i = start[0][1]
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        elif move == "W":
            pass

    return j,i


def maze_to_dict(maze):
    maze_dict = {}

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if maze[j][i] != ".":
                maze_dict.update({(j,i): maze[j][i]})

    return maze_dict

def maze_size(maze_dictionary):

    edges = [key for key, value in maze_dictionary.items() if value == "#"]
    row_min_max = min(edges)[0], max(edges)[0]
    col_min_max = min(edges)[1], max(edges)[1]
    rows = row_min_max[1] - row_min_max[0] + 1
    cols = col_min_max[1] - col_min_max[0] + 1

    return rows, cols

def maze_shift(maze, t=0):

    # print(f'maze_shift at {t= }')

    shifted_maze = {}
    rows, cols = maze_size(maze)
    rows -= 2  # disregard the edges
    cols -= 2

    blizzards = [key for key, value in maze.items() if value in (">", "<", "v", "^")]

    for blizzard in blizzards:
        blizzard_type = maze.get(blizzard)
        match blizzard_type:
            case ">":
                j = blizzard[0]
                i = blizzard[1] + t
            case "<":
                j = blizzard[0]
                i = blizzard[1] - t
            case "^":
                j = blizzard[0] - t
                i = blizzard[1]
            case "v":
                j = blizzard[0] + t
                i = blizzard[1]
            case _:
                print('anders')

        i = (i-1) % cols + 1
        j = (j-1) % rows + 1
        shifted_maze.update({(j, i): blizzard_type})

    edges = [key for key, value in maze.items() if value in ("#", "X", "O")]
    for edge in edges:
        shifted_maze.update({(edge[0], edge[1]): maze.get(edge)})


    return shifted_maze

def read_input_file(filename):
    with open(filename) as f:
        content = f.read().splitlines()

    maze = []
    for line in content:
                maze.append(list(line))

    maze_dict = maze_to_dict(maze)
    return maze_dict

if __name__ == '__main__':
    filename = "input/input24test2.txt"
    maze = read_input_file(filename)

    paths = queue.Queue()
    paths.put("")
    path = ""

    shifted_maze_list = []
    for t in range(500):
        shifted_maze_list.append(maze_shift(maze, t=t))

    unique_entries = set()

    while not find_exit(maze, path):
        path = paths.get()
        for j in ["L", "R", "U", "D", "W"]:
            new_path = path + j
            if valid_move(maze, new_path):
                new_position = find_position(maze, new_path)
                entry = (len(new_path), new_position)
                if entry not in unique_entries:
                    paths.put(new_path)
                    unique_entries.add(entry)




    # print(f'partI: {maze}')
    # print(f'partII: {maze}')


