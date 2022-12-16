# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)
class Node:
    def __init__(self, folder_name, folder_size=0, parent=None):
        self.folder_name = folder_name
        self.folder_size = folder_size
        self.parent = parent
        self.children = []


def print_values(node):
    if node is None:
        return []
    child_values = [print_values(n) for n in node.children]
    return [node.folder_size] + child_values


def level_order_traversal(root):
    directory_sizes = []
    if root is None:
        return
    node_queue = [root]
    while len(node_queue) != 0:
        n = len(node_queue)
        while n > 0:
            node = node_queue[0]
            node_queue.pop(0)
            directory_sizes.append(node.folder_size)
            for i in range(len(node.children)):
                node_queue.append(node.children[i])
            n -= 1
    return directory_sizes


def read_input_file():
    filename = "input/input7.txt"

    with open(filename) as f:
        content = f.read().splitlines()

    return content


def process_cd_command(node, line):
    folder_name = line[2]
    # returns a new current node
    if folder_name == '/':
        return node
    elif folder_name == "..":
        return node.parent
    else:
        # change the current directory to the folder
        for child in node.children:
            if child.folder_name == folder_name:
                return child


def process_ls_command():
    pass


def add_size_to_directories(node, file_size):
    while node:
        node.folder_size += file_size
        node = node.parent


def process_output(node, line):
    if line[0] == 'dir':
        # add directory name (line[1]) to the Tree
        child_node = Node(folder_name=line[1], parent=node)
        node.children.append(child_node)
    else:
        # add file size to the current directory size and its parents
        file_size = int(line[0])
        add_size_to_directories(node, file_size)


def process_input_lines(input_lines, position, node):
    line = input_lines[position].split(" ")
    # if the line starts with $ process the command else process the output
    if line[0] == "$":
        if line[1] == 'cd':
            node = process_cd_command(node, line)
        else:
            process_ls_command()
    else:
        process_output(node, line)
    return node


if __name__ == '__main__':
    input_lines = read_input_file()

    root = Node(folder_name='/')
    current_node = root
    current_position = 0

    while current_position < len(input_lines):
        current_node = process_input_lines(input_lines, current_position, current_node)
        current_position += 1

    directories = level_order_traversal(root)
    print(directories)
    small_directories = [d for d in directories if d <= 100_000]
    print(small_directories)
    print('partI: sum of all directory size <= 100.000: ', sum(small_directories))

    total_disk_space = 70_000_000
    minimum_available_space = 30_000_000
    used_space = root.folder_size
    current_available_space = total_disk_space - used_space
    extra_free_space_needed = minimum_available_space - current_available_space
    print(f'{used_space= }')
    print(f'{current_available_space= }')
    print(f'{extra_free_space_needed= }')

    candidate_directories = [d for d in directories if d >= extra_free_space_needed]
    print(sorted(candidate_directories))

    print('partII: size of smallest directory to be deleted:', sorted(candidate_directories)[0])

    print(print_values(root))
