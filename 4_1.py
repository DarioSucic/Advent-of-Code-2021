from aoc import *

lines = read_lines(day=4)
txt = read_string(day=4)

parts = txt.split("\n\n")
rnd = list(map(int, parts[0].split(",")))
boards = [[list(map(int, line.split())) for line in part.splitlines()] for part in parts[1:]]

def check_board(board):
    count = 0
    for line in board:
        if line == [True] * 5:
            count += 1

    for col in list(zip(*board)):
        col = list(col)
        if col == [True] * 5:
            count += 1
    
    return count

def score(board):
    total = 0
    for row in board:
        for num in row:
            if num is not True:
                total += num
    return total

def solve():
    counts = {i: 0 for i in range(len(boards))}
    for draw in rnd:
        for b, board in enumerate(boards):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == draw:
                        board[i][j] = True
                        counts[b] += 1
                        if check_board(board) > 0:
                            print(score(board)*draw)
                            return

solve()
