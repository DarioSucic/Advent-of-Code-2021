from collections import deque
from itertools import product
from aoc import *

lines = read_lines(day=20)
txt = read_string(day=20).strip()

enh, img = txt.split("\n\n")
img = img.split("\n")

assert len(enh) == 512

def dirs(x, y):
    yield from ((x+i, y+j) for j in (-1,0,1) for i in (-1,0,1))

def pad(a, p, v):
    w, h = len(a[0]), len(a)
    return [*(v*(w+2*p),)*p, *[p*v + r + p*v for r in a], *(v*(w+2*p),)*p]

def alg(img):
    w, h = len(img[0]), len(img)
    out = []
    for y in range(1, w-1):
        o = []
        for x in range(1, h-1):
            v = "".join(img[yy][xx] if (0 <= xx < w and 0 <= yy < h) else "." for xx, yy in dirs(x, y))
            v = v.replace("#", "1").replace(".", "0")
            v = int(v, base=2)
            o.append(enh[v])
        out.append("".join(o))

    return out


img = pad(img, 2, ".")
img = alg(img)

img = pad(img, 2, "#")
img = alg(img)

print(sum(row.count("#") for row in img))