"""
Created on Sun Dec  4 19:54:18 2022
@author: Roman Ramirez, rr8rk@virginia.edu
Advent of Code, Day 4: Camp Cleanup
"""

def part_one():

    total = 0
    with open("input.txt") as f:
        
        for line in f.readlines():
            (a0, a1), (b0, b1) = [[int(y) for y in x.split('-')] for x in line.strip().split(",")]
    
            if (a0 <= b0) and (a1 >= b1):
                total += 1
            elif (a0 >= b0) and (a1 <= b1):
                total += 1
                
    print(total)
    
def part_two():

    total = 0
    with open("input.txt") as f:
        
        for line in f.readlines():
            (a0, a1), (b0, b1) = [[int(y) for y in x.split('-')] for x in line.strip().split(",")]
            a = {x for x in range(a0, a1 + 1)}
            b = {x for x in range(b0, b1 + 1)}
    
            if len(a.intersection(b)) != 0:
                total += 1
                
    print(total)
    
part_two()