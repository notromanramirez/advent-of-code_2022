"""
Created on Thu Dec  1 15:24:00 2022
@author: Roman Ramirez, rr8rk@virginia.edu
Advent of Code 2022, Day 01
"""

def main():

    # PART ONE
    
    total_calories = list()
        
    with open('input.txt') as f:
        running = 0
        for line in f.readlines():
            if line != '\n':
                running += int(line.strip())
            else:
                total_calories.append(running)
                running = 0
                
    print(max(total_calories))
    
    # PART TWO
    
    total_calories.sort(reverse=True)
    print(sum(total_calories[0:3]))

if __name__=='__main__':
    main()