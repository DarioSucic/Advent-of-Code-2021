from aoc import *

lines = read_lines(day=11)
txt = read_string(day=11)

grid = read_grid(int, day=11)

def dirs(x, y, w, h):
    if x - 1 >= 0 and y-1 >= 0:
        yield x-1, y-1

    if x + 1 < w and y-1 >= 0:
        yield x+1, y-1
    
    if x - 1 >= 0 and y+1 < h:
        yield x-1, y+1
    
    if x + 1 < w and y+1 < h:
        yield x+1, y+1

    if x - 1 >= 0:
        yield x-1, y
    if x + 1 < w:
        yield x+1, y
    if y - 1 >= 0:
        yield x, y-1
    if y + 1 < h:
        yield x, y+1

def update(x, y, flashed):
    for xx, yy in dirs(x, y, len(grid[0]), len(grid)):
        if (xx, yy) in flashed:
            continue
        else:
            grid[yy][xx] += 1
            global total
            if grid[yy][xx] > 9:
                flashed.add((xx, yy))
                grid[yy][xx] = 0
                total += 1
                update(xx, yy, flashed)

global total
total = 0

i = 1
while True:

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1

    flashed = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            v = grid[y][x]
            if v > 9:
                flashed.add((x, y))
                grid[y][x] = 0
                total += 1
                update(x, y, flashed)

    for line in grid:
        if line != [0] * len(grid[0]):
            break
    else:
        print(i)
        break

    i += 1