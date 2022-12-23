class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderTraversal(root, answer=[]):
    if root is None:
        return

    inorderTraversal(root.left, answer)
    answer.append(root.val)
    inorderTraversal(root.right, answer)
    return answer


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorderTraversal(root))
