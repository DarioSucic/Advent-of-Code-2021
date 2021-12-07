from aoc import *

lines = read_lines(day=7)
txt = read_string(day=7)

xs = ints(txt)

uniq = set(xs)

f = lambda n: n*(n+1)//2

s = min(uniq, key=lambda s: sum(f(abs(x-s)) for x in xs))
print(sum(f(abs(x-s)) for x in xs))