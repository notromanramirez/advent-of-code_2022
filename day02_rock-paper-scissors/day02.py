"""
Created on Fri Dec  2 11:38:42 2022
@author: Roman Ramirez, rr8rk@virginia.edu
Advent of Code 2022, Day 02
"""

# PART ONE

def part_one():
    score = 0
    with open('input.txt') as f:
        for line in f.readlines():
            # the two letters in the line of input
            a, b = line.strip().split(' ')
            # value from 0 to 2 representing opp. input
            c = ord(a) - 65
            # value from 0 to 2 representing my input
            d = ord(b) - 23 - 65
            # value from 0 to 2 representing the outcome
            e = (d - c + 1) % 3
            # adding the score for a given match
            score += (d + 1) + (e * 3)  
        print(score)

def part_two():
    score = 0
    with open('input.txt') as f:
        for line in f.readlines():
            # the two letter in the line of input
            a, b = line.strip().split(' ')
            # value from 0 to 2 representing opp. input
            c = ord(a) - 65
            # value from 0 to 2 representing the desired outcome
            d = ord(b) - 23 - 65
            # value from 0 to 2 representing what I should choose given the
            # opp. input and desired outcome
            e = (c + d - 1) % 3
            # adding the score for a given match
            score += (e + 1) + (d * 3)
        print(score)
        
part_one()
part_two()        