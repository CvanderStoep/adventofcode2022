import sys
import numpy as np
from itertools import pairwise, chain


def main() -> None:
    def raster(c1x, c1y, c2x, c2y) -> set:
        if c1x > c2x: c1x, c2x = c2x, c1x  # swap min, max x
        if c1y > c2y: c1y, c2y = c2y, c1y  # swap min, max y

        return set([tuple((c1x, c1y))] + [tuple((c2x, c2y))] \
                   + [tuple((x, c1y)) for x in range(c1x + 1, c2x)] \
                   + [tuple((c1x, y)) for y in range(c1y + 1, c2y)])

    itxt = open("input/input14.txt", mode='r').readlines()
    itxt = [i.split(' -> ') for i in itxt]
    itxt = [[tuple(map(int, j.split(','))) for j in i] for i in itxt]
    rock = [raster(*c1, *c2) for l in itxt for c1, c2 in pairwise(l)]
    rock = set(chain(*rock))  # flatten

    sand = set()

    while True:
        s = np.array((500, 0))

        while True:
            if tuple(s + (0, 1)) not in rock.union(sand):
                s += (0, 1)
            elif tuple(s + (-1, 1)) not in rock.union(sand):
                s += (-1, 1)
            elif tuple(s + (1, 1)) not in rock.union(sand):
                s += (1, 1)
            else:
                break

            if s[1] > 99999:
                print(len(sand))
                return

        sand.add(tuple(s))


if __name__ == '__main__':
    sys.exit(main())