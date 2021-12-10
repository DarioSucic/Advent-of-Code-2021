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

scores = []
for line in lines:
    opened = []
    print(line)
    for c in line:
        if c in opening:
            opened.append(c)
        else:
            i = opening.index(opened[-1])
            if c != closing[i]:
                break
            else:
                opened.pop()
    else:
        ls = 0
        while opened:
            c = closing[opening.index(opened.pop())]
            ls = ls * 5 + scrs[c]
        print(ls)
        scores.append(ls)

scores.sort()
print(scores[len(scores)//2])
