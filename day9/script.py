import numpy as np
import pandas as pd
from datetime import date
import math

def get_day():
    return date.today().strftime('%-d')


def get_input():
    with open(f'./day{get_day()}/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day{get_day()}/testinput{task}.txt', 'r') as input:
            return input.readlines()


def part1():
    #input = [x.strip('\n').split(' ') for x in get_testinput(1)]
    input = [x.strip('\n').split(' ') for x in get_input()]
    input = list(map(lambda sublist : list(map(int, sublist)), input))
    
    next_values = list()

    for row in input:
        diffs = [row]
        for diff in diffs:    
            diff = [diff[i+1] - diff[i] for i in range(len(diff)-1)]
            
            diffs.append(diff)
            if len(set(diff)) == 1:
                diffs[-1].append(diff[0])
                for i in range(1, len(diffs)):
                    # Append the sum of the last element of the current and previous (one layer further down) row of differences.
                    diffs[-i-1].append(diffs[-i-1][-1] + diffs[-i][-1]) 
                next_values.append(diffs[0][-1])
                break
        
    #print('next_values:', next_values)
    return sum(next_values)    


def part2():
    return


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1: ", main(True))

print("Part 2: ", main(False))
