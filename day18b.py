# solution from AOC reddit
# https://github.com/silentw0lf/advent_of_code_2022/blob/main/18/solve.py

"""""
part1;
search all neigbours for all cubes and increases surface area for each ajacent cube that are not a cube itself

part2;
start at the outside of the cube-space and work outside-in using BFS
adjacent cubes are only placed on the queue by non-cubes.

"""

import re

with open("input/input18-2.txt") as f:
    cubes = [tuple(map(int, re.findall("(\d+)", l))) for l in f.readlines()]

minout = [min(c[i] - 1 for c in cubes) for i in range(3)]
maxout = [max(c[i] + 1 for c in cubes) for i in range(3)]

def in_space(cube):
    return all(minout[i] <= cube[i] <= maxout[i] for i in range(3))


def get_neighbors(cube):
    return [tuple(sum(x) for x in zip(cube, d)) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]


# part 1
exposed = 0
for cube in cubes:
    for n in get_neighbors(cube):
        if n not in cubes:
            exposed += 1

# part 2
exposed_outside = 0
seen = set()
queue = [tuple(maxout)]
while queue:
    curr_cube = queue.pop(0)
    if curr_cube in cubes:
        exposed_outside += 1
    else:
        if curr_cube not in seen:
            seen.add(curr_cube)
            for n in get_neighbors(curr_cube):
                if in_space(n):
                    queue.append(n)

print(exposed)
print(exposed_outside)
