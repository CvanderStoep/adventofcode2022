import logging

import numpy


def evaluate(math_operations, starting_point):
    """
    This function takes an expression, which is either an integer
    or a string consisting of an operator and two sub-expressions.
    If the expression is an integer, it returns the integer.
    If it is not an integer, it evaluates the left and right sub-expressions recursively,
    and then applies the operator to the resulting values.
    The starting point is 'root' taking from a dictionary of key/value pairs

    input: math_operations is a dictionary {}
    {'root': 'a * b', 'a': 'c + d', 'b': 2, 'c': 3, 'd': 5} evaluates to 16
    """
    expression = math_operations[starting_point]

    if isinstance(expression, int):
        return expression

    left, operator, right = expression.split(" ")

    # for partII, both numbers at the root have to be equal -> the difference = 0
    # this makes the binary search for the root possible
    if starting_point == 'root':
        operator = "-"

    left = evaluate(math_operations, left)
    right = evaluate(math_operations, right)

    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    elif operator == '/':
        return left / right
    else:
        raise ValueError(f"Unknown operator: {operator}")
    

def read_input_file(filename):
    math_operations = {}
    with open(filename) as f:
        content = f.read().splitlines()

    for line in content:
        monkey, expression = line.split(": ")
        try:
            expression = int(expression)
        except ValueError:
            pass

        math_operations.update({monkey: expression})

    return math_operations


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.WARNING,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    filename = "input/input21.txt"
    math_operations= read_input_file(filename)
    logging.debug(math_operations)
    humn_number_left = 0
    humn_number_right = 10  # starting interval to be expanded until it is large enough to start binary search

    math_operations["humn"] = humn_number_left
    value_left = evaluate(math_operations, 'root')

    math_operations["humn"] = humn_number_right
    value_right = evaluate(math_operations, 'root')

    # make starting interval large enough to contain both positive and negative values
    while numpy.sign(value_left) == numpy.sign(value_right):
        humn_number_right *= 1000
        math_operations["humn"] = humn_number_right
        value_right = evaluate(math_operations, 'root')
    print(f'{humn_number_left= }, {value_left= }, {humn_number_right= }, {value_right= }')

    # binary search cuts the interval in half every time until the zero root is found.
    number_found = False
    while not number_found:
        logging.info(humn_number_left)
        math_operations["humn"] = humn_number_left
        value_left = evaluate(math_operations,'root')

        math_operations["humn"] = humn_number_right
        value_right = evaluate(math_operations,'root')

        humn_number_middle = (humn_number_left + humn_number_right) // 2
        math_operations["humn"] = humn_number_middle
        value_middle = evaluate(math_operations,'root')

        if value_middle == 0:
            number_found = True

        if numpy.sign(value_middle) == numpy.sign(value_left):
            humn_number_left = humn_number_middle
        else:
            humn_number_right = humn_number_middle

    print(f'partII: {humn_number_middle= }')

