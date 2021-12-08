from aoc import *

lines = read_lines(day=8)
txt = read_string(day=8)

mapping = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

counts = defaultdict(int)
for line in lines:
    segs = line.split(" | ")
    lst = segs[-1]
    
    for p in lst.split(" "):
        m = len(p)
        if (i := mapping.get(m, None)) != None:
            counts[i] += 1

print(sum(counts.values()))