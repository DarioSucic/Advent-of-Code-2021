from collections import deque
from aoc import *

lines = read_lines(day=14)
txt = read_string(day=14).strip()

a, b = txt.split("\n\n")
b = b.split("\n")
d = dict(l.split(" -> ") for l in b)

t = {}
for k, v in d.items():
    t[k] = (k[0]+v, v+k[1])

c = Counter()
for k in d:
    c[k] = a.count(k)

cnt = Counter(a)

for _ in range(40):
    cc = c.copy()
    for k in cc:
        v = c[k]
        cnt[d[k]] += v
        cc[k] -= v
        for key in t[k]:
            cc[key] += v
    c = cc

print(max(cnt.values()) - min(cnt.values()))