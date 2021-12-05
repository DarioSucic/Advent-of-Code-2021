from aoc import *

lines = read_lines(day=5)
txt = read_string(day=5)

import numpy as np

grid = np.zeros((5000, 5000), dtype=int)

m = defaultdict(int)

for line in lines:
    a, b = line.split(" -> ")
    ax, ay = map(int, a.split(","))
    bx, by = map(int, b.split(","))

    dx = abs(ax-bx)
    dy = abs(ay-by)

    if dx == 0:
        grid[min(ay,by):min(ay,by)+dy+1, ax] += 1
    elif dy == 0:
        grid[ay, min(ax,bx):min(ax,bx)+dx+1] += 1


print((grid >= 2).sum())