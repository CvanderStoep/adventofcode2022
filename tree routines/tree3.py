# Define a class for the tree node
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []


# Define the depth-first search function
def dfs(root):
    # Create a stack to store the nodes we need to visit
    stack = [root]

    # Keep track of the nodes we have visited
    visited = set()

    # While the stack is not empty
    while stack:
        # Pop the top node from the stack
        node = stack.pop()

        # If the node has not been visited yet
        if node not in visited:
            # Visit the node
            print(node.value)

            # Add the node to the visited set
            visited.add(node)

            # Add the children of the node to the stack
            stack.extend(node.children)


# Create the root node
root = Node("A", [Node("B"), Node("C"), Node("D")])

# Traverse the tree using depth-first search
dfs(root)
