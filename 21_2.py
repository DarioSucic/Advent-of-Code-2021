from itertools import cycle, product
from aoc import *

txt = read_string(day=21)
lines = txt.split('\n')

_, p1, _, p2 = ints(txt)
print(p1, p2)

def move(p, r):
    return (p + r - 1) % 10 + 1

def play(p1, p2, s1, s2, memo={}):
    
    key = (p1, p2, s1, s2)
    if key in memo:
        return memo[key]
    
    sc = (0, 0)
    for r in product((1, 2, 3), repeat=3):
        r = sum(r)
        _p1 = move(p1, r)
        _s1 = s1 + _p1
        if _s1 >= 21:
            sc = (sc[0]+1, sc[1])
        else:
            a, b = play(p2, _p1, s2, _s1)
            sc = (sc[0]+b, sc[1]+a)

    memo[key] = sc
    return sc

print(max(play(p1, p2, 0, 0)))