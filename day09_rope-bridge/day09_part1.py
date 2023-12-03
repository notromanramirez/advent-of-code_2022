"""
Created on Sat Dec 10 14:45:56 2022
@author: Roman Ramirez, rr8rk@virginia.edu
Advent of Code 2022, Day 9: Rope Bridge
"""

import numpy as np

INPUT_FILENAME = 'tinput.txt'

clines = list()
with open(INPUT_FILENAME) as f:
    for line in f.readlines():
        clines.append(line.replace("\n", ''))
        
print(clines)

letter2num = {'D': 3,'R': 2,'U': 1,'L': 0}
num2letter = {3: 'D',2: 'R',1: 'U',0: 'L'}
inst_list = list()
for line in clines:
    a, b = line.split(' ')
    inst_list.append((letter2num[a], int(b)))

# define the region in which the head will move
xmin, ymin = np.inf, np.inf
xmax, ymax = -np.inf, -np.inf

# initialize head coordinates
hx, hy = 0, 0

# move head
for (dr, dist) in inst_list:
    # current location += num_steps * direction * vertical/horizontal
    hx += dist * (dr - 1) * ((dr + 1) % 2)
    hy += dist * (dr - 2) * ((dr + 0) % 2)
    
    # adjust bounds if I go further
    if hx < xmin: xmin = hx
    if hy < ymin: ymin = hy
    if hx > xmax: xmax = hx
    if hy > ymax: ymax = hy
  
# what are my total bounds
ROWS = xmax - xmin + 1
COLS = ymax - ymin + 1

def print_bridge(np2da, sy, sx, hy, hx, ty, tx):
    board = np2da.copy()
    board[sy, sx] = 's'
    board[ty, tx] = 'T'
    board[hy, hx] = 'H'
    for line in board:
        print("".join(line))
    print()

# INITIALIZATIONS
# for visualizing
bridge = np.empty(shape=(COLS, ROWS), dtype=str)
bridge.fill('.')
# for remembering all tail visits
tail_visits = np.empty(shape=(COLS, ROWS), dtype=bool)
tail_visits.fill(False)

# starting points
sy, hy, ty = -ymin, -ymin, -ymin
sx, hx, tx = -xmin, -xmin, -xmin

print_bridge(bridge, sy, sx, hy, hx, ty, tx)

# RUN THE ALGORITHM

for (dr, dist) in inst_list:
    for i in range(dist):
        # move the head
        hx += (dr - 1) * ((dr + 1) % 2)
        hy += (dr - 2) * ((dr + 0) % 2)
        
        # move the tail
        
        # WIP: THE DIAGONAL IS FUCKED LMAO
        
        # 3: down
        if (hy - ty) >= 2:
            # none
            ty += 1
            # down-right
            if (hx - tx) == 1: tx += 1
            # down-left
            if (hx - tx) == -1: tx -= 1
        # 2: right
        elif (hx - tx) >= 2:
            # none
            tx += 1
            # down-right
            if (hy - ty) == 1: ty += 1
            # up-right
            if (hy - ty) == -1: ty -= 1
        # 1: up
        elif (hy - ty) <= -2:
            # none
            ty -= 1
            # up-right
            if (hx - tx) == 1: tx += 1
            # up-left
            if (hx - tx) == -1: tx -= 1
        # 0: left
        elif (hx - tx) <= -2:
            # none
            tx -= 1
            # down-left
            if (hy - ty) == 1: ty += 1
            # up-left
            if (hy - ty) == -1: ty -= 1
        # print_bridge(bridge, sy, sx, hy, hx, ty, tx)   
        
        # place the pound marker
        tail_visits[ty, tx] = True

# print_bridge(bridge, sy, sx, hy, hx, ty, tx)
    
# count all the pound markers
print(sum(tail_visits.flatten()))