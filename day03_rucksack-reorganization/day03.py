"""
Created on Sat Dec  3 11:51:09 2022
@author: Roman Ramirez, rr8rk@virginia.edu
Advent of Code, Day 03
"""
def part_one():
    priorities = 0
    with open("input.txt") as f:
        for line in f.readlines():
            cline = line.strip()
            a, b = cline[0:len(cline) // 2], cline[len(cline) // 2:len(cline)]
            
            match = None
            for ac in a:
                for bc in b:
                    if ac == bc:
                        match = ac
                        
            if match.islower():
                priorities += ord(match) - 96
            elif match.isupper():
                priorities += ord(match) - 38
                
    print(priorities)
    
def part_two():
    priorities = 0
    group = list()
    with open("input.txt") as f:
        for i, line in enumerate(f.readlines()):
            
            group.append(line.strip())
            
            if len(group) == 3:
                match = None
                a = group.pop()
                b = group.pop()
                c = group.pop()
                for ac in a:
                    for bc in b:
                        for cc in c:
                            if ac == bc == cc:
                                match = ac
                            
                if match.islower():
                    priorities += ord(match) - 96
                elif match.isupper():
                    priorities += ord(match) - 38
                
                
    print(priorities)

part_one()    
part_two()