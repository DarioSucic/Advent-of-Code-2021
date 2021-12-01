from aoc import *

lines = read_lines(day=1)
txt = read_string(day=1)

i = 0
for a, b, c, d in zip(ints(txt), ints(txt)[1:], ints(txt)[2:], ints(txt)[3:]):
    if a + b + c < b + c + d:
        i += 1

print(i)