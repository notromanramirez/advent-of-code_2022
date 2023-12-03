"""
Created on Tue Dec  6 00:07:38 2022
@author: Roman Ramirez, rr8rk@virginia.edu
Advent of Code 2022, Day 6: Tuning Trouble
"""

import numpy as np

cline = None
with open('input.txt') as f:
    for line in f.readlines():
        cline = line.replace('\n', '')


## part one
def find_sop_marker(s):
      
    for i in range(4, len(s)):
        checker = s[i-4:i]
        if False in np.array([[x != y for i, x in enumerate(checker) if i != j] for j, y in enumerate(checker)]).flatten():
            pass
        else:
            return i

## part two
def find_som_marker(s):
      
    for i in range(14, len(s)):
        checker = s[i-14:i]
        if False in np.array([[x != y for i, x in enumerate(checker) if i != j] for j, y in enumerate(checker)]).flatten():
            pass
        else:
            return i
        
                
print(find_sop_marker(cline))
print(find_som_marker(cline))
             