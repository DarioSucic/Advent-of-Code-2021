from aoc import *

lines = read_lines(day=1)
txt = read_string(day=1)

i = 0
for a, b in zip(ints(txt), ints(txt)[1:]):
    if b > a:
        i += 1

print(i)