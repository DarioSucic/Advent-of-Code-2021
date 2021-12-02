from aoc import *

lines = read_lines(day=2)
txt = read_string(day=2)

x = 0
y = 0

for line in lines:
    d, a = line.split()
    a = int(a)
    if d == "forward":
        x += a
    if d == "down":
        y += a
    if d == "up":
        y -= a

print(x*y)