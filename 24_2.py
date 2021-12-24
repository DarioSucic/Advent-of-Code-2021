from aoc import *

txt = read_string(day=24)
lines = txt.split('\n')

def execb(z, w, c1, c2, c3):
    x = z % 26 + c2
    z = z // c1
    if x != w:
        z = z*26 + w + c3
    return z
     
def program(p: str):
    z = 0
    for w, (c1, c2, c3) in zip(map(int, p), coeffs):
        z = execb(z, w, c1, c2, c3)
    return z

blocks = txt.split("inp w\n")[1:]
coeffs = []

for b in blocks:
    xs = ints(b)
    c1, c2, c3 = xs[2], xs[3], xs[9]
    print(c1, c2, c3, sep="\t")
    coeffs.append((c1, c2, c3))


m = {}
for i, (c1, c2, c3) in enumerate(coeffs):
    #if c2 < 0:
    m[i] = {z: w for z in range(26) for w in range(1, 10) if (z + c2) == w}
    print(i, "\t", m[i])

solutions = set()

global cnt
cnt = 0

def dive(z, i, path):
    global cnt
    cnt += 1
    if i == 14:
        if z == 0:
            solutions.add(int("".join(map(str, path))))
        return

    c1, c2, c3 = coeffs[i]
    d = m[i]

    if not d:
        # Brute force
        for w in range(1, 10):
            path.append(w)
            dive(execb(z, w, c1, c2, c3), i+1, path)
            path.pop()
    else:
        # Filter
        for _z, w in d.items():
            if z % 26 != _z:
                continue
            path.append(w)
            dive(execb(z, w, c1, c2, c3), i+1, path)
            path.pop()

from time import perf_counter_ns as pc

st = pc()
dive(0, 0, [])
et = pc()

print(f"Runtime: {et-st:>12,} ns")

print(max(solutions))
print("Cnt:", cnt)


