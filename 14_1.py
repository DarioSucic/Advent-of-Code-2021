from collections import deque
from aoc import *

lines = read_lines(day=14)
txt = read_string(day=14)

a, b = txt.split("\n\n")
b = b.split("\n")[:-1]
b = [l.split(" -> ") for l in b]

d = dict(b)

s = a
print(len(s))
for _ in range(10):
    js = []
    i = 0
    while i < len(s)-1:
        a, b = s[i], s[i+1]
        c = a+b
        if c in d:
            js.append((i+1, d[c]))
        
        i += 1

    ns = list(s)
    for k, (j, c) in enumerate(js):
        ns.insert(k+j, c)

    ns = "".join(ns)

    #NBCCNBBBCBHCB
    #CCBNBBCNBHHCB

    if _ < 4:
        print(ns)

    s = ns
    print(len(s))

    # for k, v in d.items():
    #     s = s.replace(k, k[0] + v + k[1])
    # print(len(s))

c = Counter(s)
print("out", max(c.values()) - min(c.values()))