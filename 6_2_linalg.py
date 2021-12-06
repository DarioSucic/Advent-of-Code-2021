from aoc import *
import numpy as np

txt = read_string(day=6)

# Initial state vector
s = np.zeros(10, dtype=int)
for v in ints(txt):
    s[v] += 1

# Transition matrix
T = np.eye(10, k=1, dtype=int)
T[6, 0] = 1
T[8, 0] = 1

# Eigval decomposition
e, P = np.linalg.eig(T)
P_inv = np.linalg.inv(P)

def solve(s, P, e, P_inv, n):
    D_pow_n = np.diag(e**n)
    T = P @ D_pow_n @ P_inv
    return round(abs((T @ s).sum()))

print(solve(s, P, e, P_inv,  80)) # part 1
print(solve(s, P, e, P_inv, 256)) # part 2
