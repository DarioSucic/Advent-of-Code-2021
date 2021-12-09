from aoc import *

lines = read_lines(day=9)
txt = read_string(day=9)

grid = [list(map(int, line)) for line in lines]
w, h = len(grid[0]), len(grid)

lows = []
for x in range(w):
    for y in range(h):
        v = grid[y][x]

        for xx, yy in dirs(x, y, w, h):
            if grid[yy][xx] <= v:
                break
        else:
            lows.append((x, y))

def bfs(x, y, v, been):
    if (x, y) in been or v == 9:
        return
    else:
        been.add((x, y))
    
    for xx, yy in dirs(x, y, w, h):
        if grid[yy][xx] <= v:
            continue
        else:
            bfs(xx, yy, grid[yy][xx], been)

sizes = []
for x, y in lows:
    been = set()
    bfs(x, y, grid[y][x], been)
    sizes.append(len(been))

sizes.sort()

print(math.prod(sizes[-3:]))