import numpy as np
import pandas as pd
from datetime import date
import math

def get_day():
    return date.today().strftime('%-d')


def get_input():
    with open(f'./day11/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day11/testinput{task}.txt', 'r') as input:
            return input.readlines()


def part1():
    input = np.array([[*x.strip('\n')] for x in get_testinput(1)])
    input = np.array([[*x.strip('\n')] for x in get_input()])

    input = duplicate_empty_rows(input)
    input = np.transpose(duplicate_empty_rows(np.transpose(input)))
    
    galaxies = np.transpose(np.where(input == '#'))

    shortest_paths = np.full((len(galaxies), len(galaxies)), np.inf)
    
    for idx1, galaxy1 in enumerate(galaxies):
        for idx2, galaxy2 in enumerate(galaxies):
            shortest_paths[idx1, idx2] = np.abs(galaxy1[0] - galaxy2[0]) + np.abs(galaxy1[1] - galaxy2[1])

    return int(np.sum(shortest_paths/2))


def duplicate_empty_rows(input):
    inserted = 0
    for idx, row in enumerate(input):
        if np.count_nonzero(row == '.') == input.shape[1]:
            input = np.insert(input, idx+inserted, row, 0)
            inserted += 1
    return input


def part2():
    return


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1: ", main(True))
print("Part 2: ", main(False))
