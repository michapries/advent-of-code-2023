import numpy as np
import pandas as pd
from datetime import date
import math

def get_day():
    return date.today().strftime('%-d')


def get_input():
    with open(f'./day9/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day9/testinput{task}.txt', 'r') as input:
            return input.readlines()


def main(is_part1):
    #input = [x.strip('\n').split(' ') for x in get_testinput(1)]
    input = [x.strip('\n').split(' ') for x in get_input()]
    input = list(map(lambda sublist : list(map(int, sublist)), input))
    
    next_values = 0

    for row in input:
        diffs = [row]
        for diff in diffs:    
            diff = [diff[i+1] - diff[i] for i in range(len(diff)-1)]            
            diffs.append(diff)
            
            if len(set(diff)) == 1:
                diffs[-1].append(diff[0]) if is_part1 else diffs[-1].insert(0, (diff[0]))
                for i in range(1, len(diffs)):
                    # For Part 1: Append the sum of the last element of the current and previous (one layer further down) row of differences.
                    # For Part 2: Prepend the subtraction result of the first element of the current and previous (one layer further down) row of differences.
                    diffs[-i-1].append(diffs[-i-1][-1] + diffs[-i][-1]) if is_part1 else diffs[-i-1].insert(0, (diffs[-i-1][0] - diffs[-i][0])) 
                next_values += diffs[0][-1] if is_part1 else diffs[0][0]
                break

    return next_values


print("Part 1: ", main(True))

print("Part 2: ", main(False))
