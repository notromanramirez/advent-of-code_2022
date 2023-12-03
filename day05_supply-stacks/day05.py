"""
Created on Mon Dec  5 12:35:24 2022
@author: Roman Ramirez, rr8rk@virginia.edu
Advent of Code 2022, Day 5: Supply Stacks
"""

with open('input.txt') as f:
    clines = [line.replace('\n', '') for line in f.readlines()]
    
def part_one():

    crates = [list() for x in range((len(clines[0]) + 1) // 4)]
        
    for line in clines:
        
        
        if len(line) > 0:
            # do this if we're reading the supply input
            if '[' in line:
                
                line_crates = [line[(x * 4) + 1] for x in range((len(line) + 1) // 4)]
                for i, lc in enumerate(line_crates):
                    if lc != ' ':
                        crates[i].insert(0, line_crates[i])
            
            # do this if we're executing the instructions
            elif line[0] == 'm':
                
                # for c in crates:
                #     print(c)
                # print('')
                
                inst_move, inst_from, inst_to = [int(x) for x in line.split(' ') if x.isdigit()]
                
                for i in range(inst_move):
                    temp = crates[inst_from-1].pop()
                    crates[inst_to-1].append(temp)
    
    
    message = ''.join([c[-1] for c in crates])
    print(message)
    

def part_two():

    crates = [list() for x in range((len(clines[0]) + 1) // 4)]
        
    for line in clines:
        
        
        if len(line) > 0:
            # do this if we're reading the supply input
            if '[' in line:
                
                line_crates = [line[(x * 4) + 1] for x in range((len(line) + 1) // 4)]
                for i, lc in enumerate(line_crates):
                    if lc != ' ':
                        crates[i].insert(0, line_crates[i])
            
            # do this if we're executing the instructions
            elif line[0] == 'm':
                
                # for c in crates:
                #     print(c)
                # print('')
                
                inst_move, inst_from, inst_to = [int(x) for x in line.split(' ') if x.isdigit()]
                
                temp_list = list()
                for i in range(inst_move):
                    temp = crates[inst_from-1].pop()
                    temp_list.insert(0, temp)
                for i in range(len(temp_list)):
                    crates[inst_to-1].append(temp_list[i])
    
    
    message = ''.join([c[-1] for c in crates])
    print(message)

part_one()
part_two()