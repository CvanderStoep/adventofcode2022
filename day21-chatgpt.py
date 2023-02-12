from collections import defaultdict

def evaluate_expression(expression, values):
    if type(expression) == int:
        return expression
    elif type(expression) == str:
        return values[expression]
    elif type(expression) == tuple:
        operator, left, right = expression
        if operator == '+':
            return evaluate_expression(left, values) + evaluate_expression(right, values)
        elif operator == '-':
            return evaluate_expression(left, values) - evaluate_expression(right, values)
        elif operator == '*':
            return evaluate_expression(left, values) * evaluate_expression(right, values)
        elif operator == '/':
            return evaluate_expression(left, values) / evaluate_expression(right, values)

def evaluate_monkey(root, monkeys, values, visited, queue):
    if root in visited:
        return
    if type(monkeys[root]) == int:
        values[root] = monkeys[root]
        visited.add(root)
        queue.append(root)
        return
    evaluate_monkey(monkeys[root][1], monkeys, values, visited, queue)
    evaluate_monkey(monkeys[root][2], monkeys, values, visited, queue)
    values[root] = evaluate_expression(monkeys[root], values)
    visited.add(root)
    queue.append(root)

def monkey_value(monkeys, root):
    values = {}
    visited = set()
    queue = []
    evaluate_monkey(root, monkeys, values, visited, queue)
    return values[root]

monkeys = {
    "root": ("+", "pppw", "sjmn"),
    "dbpl": 5,
    "cczh": ("+", "sllz", "lgvd"),
    "zczc": 2,
    "ptdq": ("-", "humn", "dvpt"),
    "dvpt": 3,
    "lfqf": 4,
    "humn": 5,
    "ljgn": 2,
    "sjmn": ("*", "drzm", "dbpl"),
    "sllz": 4,
    "pppw": ("/", "cczh", "lfqf"),
    "lgvd": ("*", "ljgn", "ptdq"),
    "drzm": ("-", "hmdt", "zczc"),
    "hmdt": 32
}
root = "root"
print(monkey_value(monkeys, root)) # Output: 152
