
from typing import List
from aoc import *

# Shoutout to sparkyb
# https://github.com/sparkyb/adventofcode/blob/master/2021/day22.py

class Cube(tuple):
    def __bool__(self):
        return all(b >= a for a, b in self)

    def __and__(self, rhs):
        return Cube((max(l[0], r[0]), min(l[1], r[1])) for l, r in zip(self, rhs))

    def __sub__(self, rhs):
        common = self & rhs
        if not common:
            return [self]

        parts = []
        for i, (l, r) in enumerate(zip(self, rhs)):
            if r[0] > l[0]:
                parts.append(Cube((*common[:i], (l[0], r[0]-1), *self[i+1:])))
            if r[1] < l[1]:
                parts.append(Cube((*common[:i], (r[1]+1, l[1]), *self[i+1:])))
        
        return [p for p in parts if p]

    def volume(self):
        return math.prod(b-a+1 for a, b in self)


txt = read_string(day=22)
lines = txt.split('\n')

steps = []
for l in lines:
    x0, x1, y0, y1, z0, z1 = ints(l)
    cube = Cube(((x0, x1), (y0, y1), (z0, z1)))
    
    steps.append((cube, l[:2] == "on"))


cubes: List[Cube] = []
for new_cube, on in steps:
    next_cubes = []
    for prev_cube in cubes:
        next_cubes += prev_cube - new_cube
    if on:
        next_cubes += [new_cube]

    cubes = next_cubes

result = sum(map(Cube.volume, cubes))

print(result) # 1182153534186233
