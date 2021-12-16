from aoc import *

lines = read_lines(day=16)
txt = read_string(day=16)

#txt = "38006F45291200"

h = "".join(f"{int(c, base=16):04b}" for c in txt.strip())

print(h)

def parsesub(i, h):
    num = ""
    done = False
    while True:
        block = h[i:i+5]
        i += 5
        if block[0] == "0":
            num += block[1:]
            break
        else:
            num += block[1:]
    
    num = int(num, base=2)
    
    return i, num


i = 0
total = 0
while i < len(h):
    if int(h[i:]) == 0:
        break
    vn = int(h[i:i+3], base=2)
    i += 3
    tid = int(h[i:i+3], base=2)
    i += 3


    print(f"(vn, tid) = ({vn}, {tid})")

    if tid == 4:
        # literal
        i, num = parsesub(i, h)
        print("parse literal", i, num)
    else:
        ltid = h[i]
        i += 1

        if ltid == "0":
            # next 15
            ps = int(h[i:i+15], base=2)
            i += 15
            print(f"parse fixed {ps}")
            #ii = i + i
            #while i <= ii:
            #    i, num = parsesub(i, h)
            #    print("parse fixed", i, num)
                
            #assert i == ii
        else:
            # next 11
            np = int(h[i:i+11], base=2)
            i += 11
            
            print(f"parse n {np}")
            #for _ in range(np):
            #    i, num = parsesub(i, h)
            #    print("parse n", i, num)

    total += vn
    print("total:", total)

print(total)