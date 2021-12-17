from itertools import product
from aoc import *

lines = read_lines(day=17)
txt = read_string(day=17)
#txt = "target area: x=20..30, y=-10..-5"

print(len(lines), len(txt))

# target area: x=240..292, y=-90..-57

xmin, xmax, ymin, ymax = ints(txt)

print(xmin, xmax, ymin, ymax)

def inarea(x, y):
    return (xmin <= x <= xmax) and (ymin <= y <= ymax)

def sim(dx, dy):
    x = 0
    y = 0

    yy = 0

    hit = False

    while x <= xmax and y >= ymin:
        x += dx
        y += dy

        # print(x, y)

        if inarea(x, y):
            print("HIT", x, y)
            hit = True
            break

        if y == ymin:
            break

        if y > yy:
            yy = y

        if dx < 0:
            dx += 1
        if dx > 0:
            dx -= 1

        dy -= 1

    return hit, yy

print("sim")
print(sim(7, 2))

s = set()

from random import random

best = -float("inf")
for dx, dy in product(range(-400, 400), range(-400, 400)):
    h, yy = sim(dx, dy)
    
    if h:
        s.add((dx, dy))
    if h and yy > best:
        best = yy

print(best) 
print(len(s))