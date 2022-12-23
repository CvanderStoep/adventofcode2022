class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderTraversal(node):
    if node is None:
        return []
    return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)


root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)
root.right.left = Treenode(6)
print(inorderTraversal(root))

