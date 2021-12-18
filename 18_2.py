import enum
from itertools import product
from aoc import *

lines = read_lines(day=18)
txt = read_string(day=18)

print(len(lines), len(txt))

def iterate(a, idxs):
    for i, x in enumerate(a):
        if isinstance(x, int) or isinstance(x, list) and len(x) == 2 and isinstance(x[0], int) and isinstance(x[1], int):
            yield x, idxs + [i]
        else:
            yield from iterate(x, idxs + [i])

def magnitude(pair):
    if isinstance(pair, int):
        return pair
    else:
        a, b = pair
        return 3*magnitude(a) + 2*magnitude(b)

def add_to_path(a, path, x, lr):
    for i in path[:-1]:
        a = a[i]
    i = path[-1]
    if isinstance(a[i], list):
        a[i][lr] += x
    else:
        a[i] += x

def explode(a):
    it = list(iterate(a, []))
    for i, (x, path) in enumerate(it):
        if isinstance(x, list) and len(path) == 4:
            if i > 0:
                add_to_path(a, it[i-1][1], x[0], -1)
            if i < len(it)-1:
                add_to_path(a, it[i+1][1], x[1], 0)
            
            for j in path[:-1]:
                a = a[j]
            a[path[-1]] = 0

            return True


def split(a):
    for i, (x, path) in enumerate(iterate(a, [])):
        for j, v in enumerate(x if isinstance(x, list) else [x]):
            if isinstance(v, int) and v >= 10:
                if isinstance(x, list):
                    path = path + [j]

                for k in path[:-1]:
                    a = a[k]

                from math import floor, ceil
                a[path[-1]] = [floor(v/2), ceil(v/2)]
                return True

nums = list(map(eval, lines))
a = nums[0]

def add(l, r):
    from copy import deepcopy
    a = [l] + [r]
    a = deepcopy(a)
    while True:
        c = explode(a)
        if c: continue
        c = split(a)
        if c: continue
        break
    return a


n = len(nums)
best = -float("inf")

for i in range(n):
    for j in range(n):
        best = max(best, magnitude(add(nums[i], nums[j])))
print(best)