import sys
import itertools

from aoc import *

lines = read_lines(day=8)
txt = read_string(day=8)

mapping = {
    "0": "abcefg",
    "1": "cf",
    "2": "acdeg",
    "3": "acdfg",
    "4": "bcdf",
    "5": "abdfg",
    "6": "abdefg",
    "7": "acf",
    "8": "abcdefg",
    "9": "abcdfg"
}

inv = { v: k for k, v in mapping.items() }

alph = "abcdefg"

from itertools import permutations

def decmap(digits):
    for p in permutations(range(7)):

        dm = { c: alph[p_i] for c, p_i in zip(alph, p) }
        
        for digit in digits:
            decoded = "".join(sorted(dm[c] for c in digit))
            if decoded not in mapping.values():
                break
        else:
            return dm


total = 0
for line in lines:

    base, output = line.split(" | ")

    dm = decmap(base.split())

    out = ""
    for digit in output.split():
        decoded = "".join(sorted(dm[c] for c in digit))
        out += inv[decoded]
    total += int(out)

print(total)