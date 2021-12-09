from aoc import *

lines = read_lines(day=9)
txt = read_string(day=9)

grid = [list(map(int, line)) for line in lines]
w, h = len(grid[0]), len(grid)

total = 0
for x in range(w):
    for y in range(h):
        v = grid[y][x]

        for xx, yy in dirs(x, y, w, h):
            if grid[yy][xx] <= v:
                break
        else:
            total += v+1

print(total)

