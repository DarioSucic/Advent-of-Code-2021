from aoc import *

lines = read_lines(day=10)
txt = read_string(day=10)

m = Counter()

opening = [ "{", "(", "[", "<" ]
closing = [ "}", ")", "]", ">" ]

pairs = [("{", "}"), ("(", ")"), ("[", "]"), ("<", ">")]

tbl = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

scrs = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

total = 0
for line in lines:
    opened = []
    print(line)
    for c in line:
        if c in opening:
            opened.append(c)
        else:
            i = opening.index(opened.pop())
            if c != closing[i]:
                print(c)
                total += tbl[c]
                break
            
print(total)