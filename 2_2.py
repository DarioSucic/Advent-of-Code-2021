from aoc import *

lines = read_lines(day=2)
txt = read_string(day=2)

hor = 0
depth = 0
aim = 0

from math import *

for line in lines:
    d, a = line.split()
    a = int(a)
    if d == "forward":
        hor += a
        depth += a*aim
    if d == "down":
        aim += a
    if d == "up":
        aim -= a

print(depth*hor)