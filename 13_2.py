from collections import deque
from aoc import *

lines = read_lines(day=13)
txt = read_string(day=13)


a, b = txt.split("\n\n")

ps = []
for line in a.split("\n"):
    x, y = map(int, line.split(","))
    ps.append((x, y))

fs = []
for line in b.strip().split("\n"):
    z = line.split(" ")[-1]
    t = z[0]
    v = int(z.split("=")[-1])
    fs.append((t, v))

def fold(g, ax, v):
    
    if ax == "y":
        g = [list(r) for r in zip(*g)]

    fl = len(g[0][v+1:])
    out = []
    for row in g:
        new_row = row[:v]
        for i in range(fl):
            new_row[v-i-1] |= row[v+1+i]
        out.append(new_row)

        assert len(new_row) == len(row) - fl - 1

    if ax == "y":
        out = [list(r) for r in zip(*out)]
    
    return out
    

min_x = min(ps, key=lambda p: p[0])[0]
min_y = min(ps, key=lambda p: p[1])[1]

max_x = max(ps, key=lambda p: p[0])[0]
max_y = max(ps, key=lambda p: p[1])[1]


width = max_x - min_x
height = max_y - min_y

g = [[False] * (width+1) for _ in range(height+1)]
for x, y in ps:
    g[y][x] = True

for f in fs:
    g = fold(g, *f)


for row in g:
    for c in row:
        c = "#" if c else " "
        print(c, end="")
    print()
