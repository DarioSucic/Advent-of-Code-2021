from aoc import *

lines = read_lines(day=7)
txt = read_string(day=7)

xs = ints(txt)

uniq = set(xs)

s = min(uniq, key=lambda s: sum(abs(x-s) for x in xs))
print(sum(abs(x-s) for x in xs))