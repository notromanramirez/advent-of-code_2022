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
        
# print(clines)

letter2num = {'D': 3,'R': 2,'U': 1,'L': 0}
num2letter = {3: 'D',2: 'R',1: 'U',0: 'L'}
inst_list = list()
for line in clines:
    a, b = line.split(' ')
    inst_list.append((letter2num[a], int(b)))

# define the region in which the head will move
xmin, ymin = np.inf, np.inf
xmax, ymax = -np.inf, -np.inf

# KNOT NUMBER: for part 2: 9, for part 1: 1
# the head is row 0
# the ith tail is row i
KNOT_NUMBER = 9
knots = np.empty(shape=(KNOT_NUMBER + 1, 2), dtype=int)
knots.fill(0)

# move head
for (dr, dist) in inst_list:
    # current location += num_steps * direction * vertical/horizontal
    knots[0, 0] += dist * (dr - 1) * ((dr + 1) % 2)
    knots[0, 1] += dist * (dr - 2) * ((dr + 0) % 2)
    
    # adjust bounds if I go further
    if knots[0, 0] < xmin: xmin = knots[0, 0]
    if knots[0, 1] < ymin: ymin = knots[0, 1]
    if knots[0, 0] > xmax: xmax = knots[0, 0]
    if knots[0, 1] > ymax: ymax = knots[0, 1]
  
# what are my total bounds
ROWS = xmax - xmin + 1
COLS = ymax - ymin + 1

def print_bridge(np2da, sy, sx, k):
    board = np2da.copy()
    board[sy, sx] = 's'
    
    for i in range(len(k)-1, -1, -1):
        board[k[i, 1], k[i, 0]] = str(i)
    
# =============================================================================
#     for i, (a, b) in enumerate(k):
#         board[b, a] = str(i)
# =============================================================================
    for line in board:
        print("".join(line))
    print()
    
def print_tail_visits(b, tv):
    board = b.copy()
    for y in range(len(board)):
        for x in range(len(board[y])):
            if tv[y, x]:
                board[y, x] = '#'
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
sy, sx = -ymin, -xmin
for i in range(len(knots)):
    knots[i] = [sx, sy]

# print_bridge(bridge, sy, sx, knots)

# RUN THE ALGORITHM

# for every direction in the list
for (dr, dist) in inst_list:
    # for each step in the direction
    for i in range(dist):
        # move all knots!
        for k, (a, b) in enumerate(knots):
            
            # move the head
            if k == 0:
                
                knots[k, 0] += (dr - 1) * ((dr + 1) % 2)
                knots[k, 1] += (dr - 2) * ((dr + 0) % 2)
            
            # move the rest of the knots
            else:
        
                # 3: down
                if (knots[k-1, 1] - knots[k, 1]) >= 2:
                    # none
                    knots[k, 1] += 1
                    # down-right
                    if (knots[k-1, 0] - knots[k, 0]) >= 1: knots[k, 0] += 1
                    # down-left
                    if (knots[k-1, 0] - knots[k, 0]) <= -1: knots[k, 0] -= 1
                # 2: right
                elif (knots[k-1, 0] - knots[k, 0]) >= 2:
                    # none
                    knots[k, 0] += 1
                    # down-right
                    if (knots[k-1, 1] - knots[k, 1]) >= 1: knots[k, 1] += 1
                    # up-right
                    if (knots[k-1, 1] - knots[k, 1]) <= -1: knots[k, 1] -= 1
                # 1: up
                elif (knots[k-1, 1] - knots[k, 1]) <= -2:
                    # none
                    knots[k, 1] -= 1
                    # up-right
                    if (knots[k-1, 0] - knots[k, 0]) >= 1: knots[k, 0] += 1
                    # up-left
                    if (knots[k-1, 0] - knots[k, 0]) <= -1: knots[k, 0] -= 1
                # 0: left
                elif (knots[k-1, 0] - knots[k, 0]) <= -2:
                    # none
                    knots[k, 0] -= 1
                    # down-left
                    if (knots[k-1, 1] - knots[k, 1]) >= 1: knots[k, 1] += 1
                    # up-left
                    if (knots[k-1, 1] - knots[k, 1]) <= -1: knots[k, 1] -= 1
                
                # print(knots)
            # print('moved knot:', k)    
            # place the pound marker
            tail_visits[knots[-1, 1], knots[-1, 0]] = True
            
            print_bridge(bridge, sy, sx, knots)  

# print_bridge(bridge, sy, sx, knots)
# print_tail_visits(bridge, tail_visits)
    
# count all the pound markers
print(sum(tail_visits.flatten()))

