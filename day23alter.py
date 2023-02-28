from time import time
from collections import deque, Counter

CARD_DIR = {
    'N': -1j,
    'S': 1j,
    'E': 1,
    'W': -1,
}


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


def nearby(elf):
    dirs = [-1 - 1j, 0 - 1j, 1 - 1j, -1, 1, -1 + 1j, 0 + 1j, 1 + 1j]
    for d in dirs:
        yield elf + d


def look_around(elf, direction):
    if direction == 'N':
        dirs = [-1 - 1j, 0 - 1j, 1 - 1j]
    elif direction == 'S':
        dirs = [-1 + 1j, 0 + 1j, 1 + 1j]
    elif direction == 'E':
        dirs = [1 - 1j, 1, 1 + 1j]
    else:  # direction == 'W':
        dirs = [-1 - 1j, -1, -1 + 1j]

    for d in dirs:
        yield elf + d


def print_scan(elves):
    elf_real = [int(elf.real) for elf in elves]
    elf_imag = [int(elf.imag) for elf in elves]

    for y in range(min(elf_imag), max(elf_imag) + 1):
        for x in range((min(elf_real)), max(elf_real) + 1):
            if complex(x, y) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    print('')


@timer_func
def day23(filepath, part2=False):
    with open(filepath) as fin:
        lines = fin.readlines()

    elves = [complex(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '#']

    # print_scan(elves)
    print(elves)

    rounds = 0
    took_step = True
    look_direction = deque(['N', 'S', 'W', 'E'])
    duplicates = set()
    while took_step:
        elves_set = set(elves)
        next_step = [None] * len(elves)
        took_step = False
        rounds += 1
        duplicates.clear()
        for i, elf in enumerate(elves):
            for n in nearby(elf):
                if n in elves_set:
                    took_step = True
                    for look in look_direction:
                        for nn in look_around(elf, look):
                            if nn in elves_set:
                                break
                        else:
                            next_step[i] = elf + CARD_DIR[look]
                            break
                    break
        counts = Counter(next_step)
        for i, elf in enumerate(next_step):
            if counts[elf] == 1:
                elves[i] = elf

        # if rounds ==1:
        #     print(elves)
        #     print(next_step)
        #     print_scan(elves)

        if not part2 and rounds == 10:
            break

        look_direction.rotate(-1)
    if not part2:
        elf_real = [int(elf.real) for elf in elves]
        elf_imag = [int(elf.imag) for elf in elves]

        val = (max(elf_real) - min(elf_real) + 1) * (max(elf_imag) - min(elf_imag) + 1) - len(elves)
    else:
        val = rounds
    # print_scan(elves)
    return val


def main():
    # assert day23('input/input23test.txt') == 110
    print(f"Part 1: {day23('input/input23.txt')}")

    # assert day23('input/input23test.txt', True) == 20
    print(f"Part 2: {day23('input/input23.txt', True)}")


if __name__ == '__main__':
    main()