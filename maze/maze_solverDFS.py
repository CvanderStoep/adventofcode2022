def createMaze():
    maze = []
    maze.append(["#", "O", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "X", "#"])

    return maze


def createMaze2():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", "#", " ", " ", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", "#", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


def print_maze(maze, path=""):
    j, i = find_start_position(maze)

    positions = set()
    for move in path:
        j, i = process_move(j,i,move)
        positions.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in positions:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def is_valid_path(maze, moves):
    j, i = find_start_position(maze)

    for move in moves:
        j, i = process_move(j,i, move)

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif maze[j][i] == "#":
            return False

    return True

def process_move(j,i,move):

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

def find_position(maze, moves):
    """"
    find the (j,i) position after a series of moves
    """
    j, i = find_start_position(maze)

    for move in moves:
        j, i = process_move(j,i,move)

    return j,i

def find_start_position(maze):
    for i, pos in enumerate(maze[0]):
        if pos == "O":
            return 0, i

def is_end_of_maze(maze, moves):
    """"
    input maze & series of moves
    returns True/False whether the end of the maze is found
    """

    j, i = find_start_position(maze)

    for move in moves:
        j, i = process_move(j, i, move)

    if maze[j][i] == "X":
        print("Found: " + moves)
        print_maze(maze, moves)
        return True

    return False


# MAIN ALGORITHM
if __name__ == '__main__':

    maze = createMaze2()
    start_path= ""
    start_position = find_start_position(maze)
    explored_positions=[start_position]
    all_paths=[start_path]

    while len(all_paths) > 0:
        current_path = all_paths.pop()
        print(current_path)
        if is_end_of_maze(maze, current_path):
            break
        for move in ["L", "R", "U", "D"]:
            next_path = current_path + move
            if is_valid_path(maze, next_path):
                new_position = find_position(maze, next_path)
                if new_position not in explored_positions:
                    all_paths.append(next_path)
                    explored_positions.append(new_position)
