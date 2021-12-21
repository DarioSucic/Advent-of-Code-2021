from itertools import cycle
from aoc import *

txt = read_string(day=21)
lines = txt.split('\n')

_, p1, _, p2 = ints(txt)
print(p1, p2)

dice = iter(cycle(range(1, 101)))

def turn(p):
    return p + sum(take(dice, 3))

s1, s2 = 0, 0

rolls = 0
i = 0
while s1 < 1000 and s2 < 1000:
    if i % 2 == 0:
        p1 = (turn(p1) - 1) % 10 + 1
        s1 += p1
        rolls += 3
    else:
        p2 = (turn(p2) - 1) % 10 + 1
        s2 += p2
        rolls += 3
    i += 1

print(min(s1, s2), rolls)
print(min(s1, s2)*rolls)