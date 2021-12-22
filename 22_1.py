from itertools import cycle
from aoc import *

txt = read_string(day=22)
lines = txt.split('\n')

print("lines:", len(lines), "\t", "len:", len(txt))

t = 0

c = defaultdict(bool)

for l in lines:
    f = l.split(" ")[0] == "on"
    
    x0, x1, y0, y1, z0, z1 = ints(l)
    
    x0 = max(x0, -50)
    x1 = min(x1, 51)
    y0 = max(y0, -50)
    y1 = min(y1, 51)
    z0 = max(z0, -50)
    z1 = min(z1, 51)
    

    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            for z in range(z0, z1+1):
                c[(x,y,z)] = f

for x in range(-50, 51):
    for y in range(-50, 51):
        for z in range(-50, 51):
            t += c[(x, y, z)]
print(t)