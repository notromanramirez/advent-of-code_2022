"""
Created on Fri Dec  9 10:00:27 2022
@author: Roman Ramirez, rr8rk@virginia.edu
Advent of Code 2022, Day 8: Treetop Tree House
"""

import numpy as np

INPUT_FILENAME = 'input.txt'

# getting the number of rows and cols in tree grid
ROWS, COLS = None, None 
with open(INPUT_FILENAME) as f:
    
    for i, line in enumerate(f.readlines()):
        COLS = len(line.strip())
        ROWS = i + 1
        
# creating trees
trees = np.empty(shape=(ROWS,COLS), dtype=int)

# all trees are not visible, if they are visible from any direction
# then they are considered visible
with open(INPUT_FILENAME) as f:
    
    for y, line in enumerate(f.readlines()):
        for x, num in enumerate(line.strip()):
            trees[y][x] = int(num)
            
    

def part_one():            
    # print(trees, '\n')       
    
    # check from top looking down
    
    def top():
        
        is_visible = np.empty(shape=(ROWS, COLS), dtype=bool)
        is_visible.fill(False)
    
        for x in range(COLS):
            highest_tree_height = -np.inf
            for y in range(ROWS):
                if trees[y][x] > highest_tree_height:
                    highest_tree_height = trees[y][x]
                    is_visible[y][x] = True
        return is_visible
                
    # print(top(), '\n')
    
    # check from bottom looking up
    
    def bottom():
        
        is_visible = np.empty(shape=(ROWS, COLS), dtype=bool)
        is_visible.fill(False)
        
        for x in range(COLS):
            highest_tree_height = -np.inf
            for y in range(ROWS-1, -1, -1):
                if trees[y][x] > highest_tree_height:
                    highest_tree_height = trees[y][x]
                    is_visible[y][x] = True
        return is_visible           
                
    # print(bottom(), '\n')
    
    # check from right looking left
    
    def left():
        
        is_visible = np.empty(shape=(ROWS, COLS), dtype=bool)
        is_visible.fill(False)
    
        for y in range(ROWS):
            highest_tree_height = -np.inf
            for x in range(COLS):
                if trees[y][x] > highest_tree_height:
                    highest_tree_height = trees[y][x]
                    is_visible[y][x] = True
        return is_visible         
                
    # print(left(), '\n')
    
    # check from left looking right
    
    def right():
        
        is_visible = np.empty(shape=(ROWS, COLS), dtype=bool)
        is_visible.fill(False)
        
        for y in range(ROWS):
            highest_tree_height = -np.inf
            for x in range(COLS-1, -1, -1):
                if trees[y][x] > highest_tree_height:
                    highest_tree_height = trees[y][x]
                    is_visible[y][x] = True
        return is_visible           
                
    # print(right(), '\n')
    
    total = top() | bottom() | left() | right()
    
    # print(total)
    print(sum(total.flatten()))

def part_two():            
    # print(trees, '\n')
    
    # up viewing distance
    def vd_up(x, y):
        view_distance = 0
        blocked_view = False
        for ny in range(y-1, -1, -1):
            if not blocked_view:
                view_distance += 1
            if trees[y][x] <= trees[ny][x]:
                blocked_view = True
                
        return view_distance
            
    
    # down viewing distance
    def vd_down(x, y):
        view_distance = 0
        blocked_view = False
        for ny in range(y+1, COLS, 1):
            if not blocked_view:
                view_distance += 1
            if trees[y][x] <= trees[ny][x]:
                blocked_view = True
                
        return view_distance
    
    # left viewing distance
    def vd_left(x, y):
        view_distance = 0
        blocked_view = False
        for nx in range(x-1, -1, -1):
            if not blocked_view:
                view_distance += 1
            if trees[y][x] <= trees[y][nx]:
                blocked_view = True
                
        return view_distance
    
    # right viewing distance
    def vd_right(x, y):
        view_distance = 0
        blocked_view = False
        for nx in range(x+1, COLS, 1):
            if not blocked_view:
                view_distance += 1
            if trees[y][x] <= trees[y][nx]:
                blocked_view = True
                
        return view_distance
    
    
    vds_up = np.array([[vd_up(x, y) for x in range(COLS)] for y in range(ROWS)], dtype=int)
    vds_down = np.array([[vd_down(x, y) for x in range(COLS)] for y in range(ROWS)], dtype=int)
    vds_left = np.array([[vd_left(x, y) for x in range(COLS)] for y in range(ROWS)], dtype=int)
    vds_right = np.array([[vd_right(x, y) for x in range(COLS)] for y in range(ROWS)], dtype=int)
    
    scenic_scores = vds_up * vds_down * vds_left * vds_right
    print(max(scenic_scores.flatten()))

part_one()    
part_two()