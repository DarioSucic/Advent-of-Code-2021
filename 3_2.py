from aoc import *

lines = [line.strip() for line in read_lines(day=3)]
txt = read_string(day=3)

def most_common(lines, i, flip):
    o = 0
    z = 0
    for line in lines:
        if line[i] == "1":
            o += 1
        else:
            z += 1
    
    if o == z:
        return "0" if flip else "1"

    if flip:
        o, z = z, o

    return "1" if o >= z else "0"



tmp = lines[:]
i = 0
while len(tmp) != 1:
    mc = most_common(tmp, i, False)
    tmp = [line for line in tmp if line[i] == mc]
    i += 1
oxy = tmp[0]

tmp = lines[:]
i = 0
while len(tmp) != 1:
    mc = most_common(tmp, i, True)
    tmp = [line for line in tmp if line[i] == mc]
    i += 1
co2 = tmp[0]

oxy = int(oxy, base=2)
co2 = int(co2, base=2)

print(oxy*co2)