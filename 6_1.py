from aoc import *

lines = read_lines(day=6)
txt = read_string(day=6)

xs = ints(txt)

for _ in range(80):
    nxt = []
    for x in xs:
        if x >= 1:
            nxt.append(x-1)
        else:
            nxt.append(6)
            nxt.append(8)
    xs = nxt

print(len(nxt))
