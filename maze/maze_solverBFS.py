import queue
from maze_solve_utils import find_position, find_start_position
from maze_solve_utils import createMaze, createMaze2, createMaze3
from maze_solve_utils import is_valid_path
from maze_solve_utils import is_end_of_maze


# MAIN ALGORITHM
""""
Solving the maze using a BFS algorithms uses a Queue FIFO
"""
if __name__ == '__main__':

    all_paths = queue.Queue()
    all_paths.put("")
    current_path = ""
    maze = createMaze3()
    start_position = find_start_position(maze)
    explored_positions = [start_position]

    while not is_end_of_maze(maze, current_path):
        current_path = all_paths.get()
        print(current_path)
        for move in ["L", "R", "U", "D"]:
            next_path = current_path + move
            if is_valid_path(maze, next_path):
                new_position = find_position(maze, next_path)
                if new_position not in explored_positions:
                    all_paths.put(next_path)
                    explored_positions.append(new_position)

    print(len(explored_positions))
