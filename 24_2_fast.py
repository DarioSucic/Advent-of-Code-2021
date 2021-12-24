from aoc import *

def execb(z, w, c1, c2, c3):
    x = z % 26 + c2
    z = z // c1
    if x != w:
        z = z*26 + w + c3
    return z

def dfs(coeffs, valid_zw_pairs, part2):
    def _dfs(z, i, digits, part2=False):
        if i == 14:
            model_num = int("".join(map(str, digits))) if z == 0 else None
            return model_num
            
        c1, c2, c3 = coeffs[i]
        zws = valid_zw_pairs[i]

        ws = range(1, 10) if not zws else (w for _z, w in zws if (z % 26) == _z)
        if not part2: ws = reversed(tuple(ws))
        
        for w in ws:
            if (model_num := _dfs(execb(z, w, c1, c2, c3), i+1, digits + [w], part2)):
                return model_num

    return _dfs(0, 0, [], part2)


txt = read_string(day=24)
blocks = txt.split("inp w\n")[1:]
coeffs = [(cs[2], cs[3], cs[9]) for cs in map(ints, blocks)]

valid_zw_pairs = [None] * len(coeffs)
for i, (_, c2, _) in enumerate(coeffs):
    valid_zw_pairs[i] = [(z, w) for z in range(26) for w in range(1, 10) if (z + c2) == w]

from time import perf_counter_ns as pc
for part2 in [False, True]:
    st = pc()
    print(f"part {part2+1}: {dfs(coeffs, valid_zw_pairs, part2)}")
    et = pc()
    print(f"{et-st:>10,}")