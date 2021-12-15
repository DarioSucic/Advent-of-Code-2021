from collections import deque
from aoc import *

lines = read_lines(day=15)
txt = read_string(day=15)

def preprocess(g):
    import numpy as np
    g = np.array(g)
    h, w = g.shape
    o = np.tile(g, (5, 5))
    for a in range(5):
        for b in range(5):
            v = a + b
            z = o[b*h:(b+1)*h, a*w:(a+1)*w]
            o[b*h:(b+1)*h, a*w:(a+1)*w] = ((z - 1) + v) % 9 + 1
    return o

g = read_grid(int, day=15)
g = preprocess(g)

w = len(g[0])
h = len(g)

m = {}
for x in range(w):
    for y in range(h):
        # N E S W
        dm = [None] * 4

        if y - 1 >= 0:
            dm[0] = g[y-1][x]
        
        if x + 1 < w:
            dm[1] = g[y][x+1]
            
        if y + 1 < h:
            dm[2] = g[y+1][x]

        if x - 1 >= 0:
            dm[3] = g[y][x-1]
            
        m[(x, y)] = dm

def get_new_pos(i, x, y):
    if i == 0: new_pos = (x, y-1)
    elif i == 1: new_pos = (x+1, y)
    elif i == 2: new_pos = (x, y+1)
    elif i == 3: new_pos = (x-1, y)
    return new_pos


def generate_path(start, goal, prev):
    path = []
    p = goal
    while p != start:
        path.append(p)
        p = prev[p]
    path.append(start)
    path.reverse()
    return path

import heapq

def dijkstra(graph, start, goal):
    Q = [(0, start)]
    dist = {v: float("inf") for v in graph}
    dist[start] = 0
    prev = {}

    while Q:
        # u = min(Q, key=dist.__getitem__)
        _, u = heapq.heappop(Q)
        for i, d in enumerate(graph[u]):
            if d == None: continue
            v = get_new_pos(i, *u)

            alt = dist[u] + d
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (alt, v))


    path = generate_path(start, goal, prev)
    return path, dist[goal]

start = (0, 0)
goal = (w-1, h-1)

path, dist = dijkstra(m, start, goal)

print(dist)