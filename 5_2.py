from aoc import *

lines = read_lines(day=5)
txt = read_string(day=5)

import numpy as np

grid = np.zeros((5000, 5000), dtype=int)

m = defaultdict(int)

def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1

for line in lines:
    a, b = line.split(" -> ")
    ax, ay = map(int, a.split(","))
    bx, by = map(int, b.split(","))

    dx = bx - ax
    dy = by - ay

    x = ax
    y = ay
        
    xx = x + dx
    yy = y + dy

    grid[x, y] += 1
    while (x, y) != (xx, yy):
        x += sign(dx)
        y += sign(dy)
        grid[x, y] += 1


print(grid[:10,:10])

print((grid >= 2).sum())