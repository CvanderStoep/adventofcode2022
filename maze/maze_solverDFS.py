from maze_solve_utils import createMaze, createMaze2, createMaze3
from maze_solve_utils import find_position, find_start_position
from maze_solve_utils import is_valid_path
from maze_solve_utils import is_end_of_maze



# MAIN ALGORITHM
""""
Solving the maze using a DFS algorithms uses a Stack/List - LIFO
"""
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

    print(len(explored_positions))
