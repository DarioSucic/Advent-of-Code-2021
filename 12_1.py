from collections import deque
from aoc import *

lines = read_lines(day=12)
txt = read_string(day=12)

d = defaultdict(list)

def count_paths(key, tree, goal, visited):
    if key == goal:
        return 1
    
    total = 0
    for k in tree[key]:
        if k in visited: continue
        nv = visited | {key} if key.islower() else visited
        total += count_paths(k, tree, goal, nv)

    return total

for line in lines:
    a, b = line.split("-")
    d[a].append(b)
    d[b].append(a)

print(count_paths("start", d, "end", set()))