import re, math

from itertools import islice, permutations
from pathlib import Path
from collections import defaultdict, Counter


# --- Parsing -----------------------------------------------------------------

RE_INT   = re.compile(r"-?\d+")
RE_FLOAT = re.compile(r"\d?\.\d+")

def ints(s: str):
    return list(map(int, RE_INT.findall(s)))

def floats(s: str):
    return list(map(float, RE_FLOAT.findall(s)))

# --- Misc. -------------------------------------------------------------------

def identity(x):
    return x

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def crt(a, n):
    """Chinese Remainder theorem.
        Solves the simultaneous congruence (for x):

        x ≡ aᵢ (mod nᵢ),  i ∈ 1..k

        nᵢ must be pairwise coprime
        0 ≤ aᵢ < nᵢ
    """
    N = math.prod(n)
    total = 0
    for a_i, n_i in zip(a, n):
        p = N // n_i
        total += a_i * mul_inv(p, n_i) * p
    return total % N

# --- Iteration / Collections -------------------------------------------------

def chunks(a, k):
    for i in range(0, len(a), k):
        yield a[i:i+k]

def take(it, n):
    return list(islice(it, n))

def nth(it, n):
    return next(islice(it, n, None))

# --- Input -------------------------------------------------------------------

def resolve_path(**kwargs) -> Path:
    for folder in kwargs.get("folders", ["inputs/{day}", "."]):
        path = Path(folder.format(**kwargs)) / "input"
        if path.exists():
            return path

def read_string(**kwargs):
    with open(resolve_path(**kwargs)) as file:
        return file.read()

def read_lines(**kwargs):
    return read_string(**kwargs).splitlines()

def read_grid(f=identity, **kwargs):
    return [list(map(f, line)) for line in read_lines(**kwargs)]

# --- Spatial -----------------------------------------------------------------

def dirs(x, y, w, h, diag=False):
    if diag:
        if x - 1 >= 0 and y-1 >= 0:
            yield x-1, y-1
        if x + 1 < w and y-1 >= 0:
            yield x+1, y-1
        if x - 1 >= 0 and y+1 < h:
            yield x-1, y+1
        if x + 1 < w and y+1 < h:
            yield x+1, y+1

    if x - 1 >= 0:
        yield x-1, y
    if x + 1 < w:
        yield x+1, y
    if y - 1 >= 0:
        yield x, y-1
    if y + 1 < h:
        yield x, y+1