from aoc import *

lines = read_lines(day=3)
txt = read_string(day=3)


counters = [0 for _ in range(len(lines[0]))]
for line in lines:
    for i, c in enumerate(line):
        counters[i] += c == "1"

n = len(lines)

x = "".join("1" if c > n//2 else "0" for c in counters[:-1])
y = "".join("0" if c > n//2 else "1" for c in counters[:-1])

x = int(x, base=2)
y = int(y, base=2)

print(x*y)
