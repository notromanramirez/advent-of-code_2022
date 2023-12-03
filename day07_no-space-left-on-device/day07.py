"""
Created on Mon Dec 12 15:53:38 2022
@author: Roman Ramirez, rr8rk@virginia.edu
Advent of Code 2022: Day 07: No Space Left On Device
"""

import numpy as np

clines = list()
with open('tinput.txt') as f:
    for line in f.readlines():
        clines.append(line.replace('\n', ''))

class Item():
    
    def __init__(self, name):
        self.children = list()
        self.name = name
        
class Dir(Item):
    
    def __init__(self, name):
        super().__init__(name)
        
class File(Item):
    
    def __init__(self, size, name):
        super().__init__(name)
        self.size = size
        
def parse(line_list):
    for line in line_list:
        blocks = line.split(' ')
        
        # ACTION CHECKS
        
        # if is a user action: cd / ls
        if blocks[0] == '$':
            if blocks[1] == 'cd':
                # go to that directory
                pass
            if blocks[1] == 'ls':
                pass
        # if it's a new item
        else:
            if blocks[0] == 'dir':
                
            size, name = blocks
            
            
parse(clines)