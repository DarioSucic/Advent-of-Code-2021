from collections import deque
from aoc import *

lines = read_lines(day=12)
txt = read_string(day=12)

d = defaultdict(list)



def count_paths(key, tree, goal, visited, twice, path, paths):
    total = 0
    for k in tree[key]:
        if k in visited:
            continue
        
        if k == goal:
            p = "".join(path)
            if p not in paths:
                total += 1
                paths.add(p)

            continue

        if k.islower():
            if twice is None:
                total += count_paths(k, tree, goal, visited, k, path+[k], paths)
                total += count_paths(k, tree, goal, visited | {k}, None, path+[k], paths)
            else:
                total += count_paths(k, tree, goal, visited | {k}, twice, path+[k], paths)
        else:
            total += count_paths(k, tree, goal, visited, twice, path+[k], paths)

    return total

for line in lines:
    a, b = line.split("-")
    d[a].append(b)
    d[b].append(a)

print(count_paths("start", d, "end", set(["start"]), None, ["start"], set()))