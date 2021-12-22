
from aoc import *

import numpy as np
import numba as nb

txt = read_string(day=22)
lines = txt.split('\n')

boxes = []
for l in lines:
    f = l.split(" ")[0] == "on"
    x0, x1, y0, y1, z0, z1 = ints(l)
    boxes.append(([(x0, x1+1), (y0, y1+1), (z0, z1+1)], f))

xs = sorted(set(x for b, f in boxes for x in b[0]))
ys = sorted(set(y for b, f in boxes for y in b[1]))
zs = sorted(set(z for b, f in boxes for z in b[2]))

xmap = { x: i for i, x in enumerate(xs) }
ymap = { y: i for i, y in enumerate(ys) }
zmap = { z: i for i, z in enumerate(zs) }

g = np.zeros((len(xs)-1, len(ys)-1, len(zs)-1), dtype=bool)

print(g.shape)

for b, f in boxes:
    (x0, x1), (y0, y1), (z0, z1) = b
    g[xmap[x0]:xmap[x1], ymap[y0]:ymap[y1], zmap[z0]:zmap[z1]] = f

@nb.njit
def sum_volumes(g, xs, ys, zs):
    xi, yi, zi = np.where(g)
    
    total = 0
    for x, y, z in zip(xi, yi, zi):
        vol = (xs[x+1] - xs[x]) * (ys[y+1] - ys[y]) * (zs[z+1] - zs[z])
        total += vol

    return total

xs, ys, zs = map(lambda a: np.array(a, dtype=np.uint64), (xs, ys, zs))

print(sum_volumes(g, xs, ys, zs))