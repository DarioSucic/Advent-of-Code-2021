from aoc import *
import numpy as np

# Parse input
top, bot = read_string(day=13).strip().split("\n\n")
xs, ys = tuple(zip(*chunks(ints(top), 2)))
folds = list(zip((line[11] for line in bot.split("\n")), ints(bot)))

# Solve
def fold_x(grid, k):
    return grid[:,:k] | grid[:,k+1:][:,::-1]

def fold(grid, d, k):
    if d == "y":
        return fold_x(grid.T, k).T
    else:
        return fold_x(grid, k)

grid = np.zeros((max(ys)+1, max(xs)+1), dtype=bool)
grid[(ys, xs)] = True
for f in folds:
    grid = fold(grid, *f)

# Show result
print("\n".join("".join("#" if c else " " for c in row) for row in grid))
