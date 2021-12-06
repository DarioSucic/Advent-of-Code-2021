from aoc import *

lines = read_lines(day=6)
txt = read_string(day=6)

xs = Counter(ints(txt))

for i in range(256):
    zeros = xs[0]
    for k in range(1, 10):
        xs[k-1] = xs[k]
    
    xs[6] += zeros
    xs[8] += zeros

print(sum(xs.values()))
