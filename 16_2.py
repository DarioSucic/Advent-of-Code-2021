from aoc import *

lines = read_lines(day=16)
txt = read_string(day=16)

#txt = "9C0141080250320F1802104A08"

h = "".join(f"{int(c, base=16):04b}" for c in txt.strip())

print(h)

def parsesub(i, h):
    num = ""
    done = False
    while True:
        block = h[i:i+5]
        i += 5
        num += block[1:]
        if block[0] == "0":
            break
        
    return i, int(num, base=2)


opmap = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda ps: int(ps[0]  > ps[1]),
    6: lambda ps: int(ps[0]  < ps[1]),
    7: lambda ps: int(ps[0] == ps[1])
}

def parse_packet(i, h, depth=0):
    vn = int(h[i:i+3], base=2)
    i += 3
    tid = int(h[i:i+3], base=2)
    i += 3

    print(f"[depth={depth}] :: (vn, tid) = ({vn}, {tid})")

    if tid == 4:
        # literal
        i, num = parsesub(i, h)
        print(f"[depth={depth}] :: num:", num)
        return i, num
    else:
        op = opmap[tid]
        ltid = h[i]
        i += 1

        print(f"[depth={depth}] :: op_{tid} = {op}")
        
        nums = []

        if ltid == "0":
            ps = int(h[i:i+15], base=2)
            i += 15
    
            print(f"[depth={depth}] :: parse fixed {ps}")
            ii = i + ps
            while i < ii:
                print(f"[depth={depth}] :: fi:", i)
                i, num = parse_packet(i, h, depth+1)
                nums.append(num)
        else:
            np = int(h[i:i+11], base=2)
            i += 11
            print(f"[depth={depth}] :: parse n")
            for _ in range(np):
               i, num = parse_packet(i, h, depth+1)
               nums.append(num)

        print(f"[depth={depth}] :: nums:", nums)
        return i, op(nums)

print(parse_packet(0, h))