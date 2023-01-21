import time


class Timer:
    timers = {}

    def __init__(
            self,
            name=None,
            text="Elapsed time: {:0.4f} seconds",
            logger=print,
    ):
        self._start_time = None
        self.name = name
        self.text = text
        self.logger = logger

        # Add new named timers to dictionary of timers
        if name:
            self.timers.setdefault(name, 0)

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise ArithmeticError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    # Other methods are unchanged

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise ArithmeticError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))
        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time


class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderTraversal(node):
    if node is None:
        return []
    leftTraversal = inorderTraversal(node.left)
    middleTraversal = [node.val]
    rightTraversal = inorderTraversal(node.right)
    return leftTraversal + middleTraversal + rightTraversal


def inorderTraversalFast(node):
    if node is None:
        return []
    leftTraversal = inorderTraversalFast(node.left)
    rightTraversal = inorderTraversalFast(node.right)
    leftTraversal.append(node.val)
    leftTraversal.extend(rightTraversal)
    return leftTraversal


def inorderTraversalFaster(node):
    def inorderTraversalFasterHelper(node, answer):
        if node is None:
            return
        inorderTraversalFasterHelper(node.left, answer)
        answer.append(node.val)
        inorderTraversalFasterHelper(node.right, answer)

    answer = []
    inorderTraversalFasterHelper(node, answer)
    return answer


def inorderTraversalFastest(node):
    def inorderTraversalFastestHelper(node, answer):
        if node.left is not None:
            inorderTraversalFastestHelper(node.left, answer)
        answer.append(node.val)
        if node.right is not None:
            inorderTraversalFastestHelper(node.right, answer)

    answer = []
    inorderTraversalFastestHelper(node, answer)
    return answer


# root = Treenode(1)
# root.left = Treenode(2)
# root.right = Treenode(3)
# root.left.left = Treenode(4)
# root.left.right = Treenode(5)
# root.right.left = Treenode(6)
def generate_test_tree(depth: int):
    if depth == 0:
        return None
    root = Treenode(1)
    root.left = generate_test_tree(depth - 1)
    root.right = generate_test_tree(depth - 1)
    return root


t1 = Timer()
t1.start()
root = generate_test_tree(20)
t1.stop()

t1.start()
print(len(inorderTraversal(root)))
t1.stop()

t1.start()
print(len(inorderTraversalFast(root)))
t1.stop()

t1.start()
print(len(inorderTraversalFaster(root)))
t1.stop()

t1.start()
print(len(inorderTraversalFastest(root)))
t1.stop()
