from collections import deque
from itertools import product
from aoc import *

lines = read_lines(day=19)
txt = read_string(day=19)

import numba as nb
import numpy as np

scanners = []
for b in txt.strip().split("\n\n"):
    s = [tuple(ints(l)) for l in b.split("\n")[1:]]
    scanners.append(s)

# https://stackoverflow.com/a/16467849
def roll(v):
    return (v[0],v[2],-v[1])

def turn(v):
    return (-v[1],v[0],v[2])

def _rotations(v):
    for _ in range(2):
        for _ in range(3):
            v = roll(v)
            yield(v)
            for _ in range(3):
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))

def rotations(s):
    return zip(*map(_rotations, s))

@nb.njit
def sub(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

@nb.njit
def overlaps(lsa, lsb):
    sa = set(lsa)
    for a in lsa:
        for cb in lsb:
            delta = sub(cb, a)
            c = 0
            for b in lsb:
                v = sub(b, delta)
                if v in sa:
                    c += 1
                    if c >= 12:
                        return a, cb
    return None

def common(sa, sb):
    lsa = nb.typed.List(sa)
    for sb in rotations(sb):
        lsb = nb.typed.List(sb)
        if (out := overlaps(lsa, lsb)):
            a, b = out
            delta = sub(b, a)
            return {sub(b,delta) for b in sb}
        

beacons = set(scanners[0])
queue = deque(scanners[1:])

while queue:
    s = queue.popleft()
    if (x := common(beacons, s)):
        beacons |= x
    else:
        queue.append(s)

print(len(beacons))
