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


def main(is_part1):
    input = np.array([[*x.strip('\n')] for x in get_testinput(1)])
    input = np.array([[*x.strip('\n')] for x in get_input()])
    
    multiplicator = 1000000 if not is_part1 else 2

    horizontal_empties = list()
    vertical_empties = list()
    for idx in range(input.shape[1]):
        if np.count_nonzero(input[idx] == '.') == input.shape[1]:
            horizontal_empties.append(idx)
    for idx in range(input.shape[0]):
        if np.count_nonzero(input[:, idx] == '.') == input.shape[0]:
            vertical_empties.append(idx)
    
    galaxies = np.transpose(np.where(input == '#'))
    
    shortest_paths = np.full((len(galaxies), len(galaxies)), np.inf)

    for idx1, galaxy1 in enumerate(galaxies):
        for idx2, galaxy2 in enumerate(galaxies):
            vertical_empties_in_range = [x for x in vertical_empties if x in range(galaxy1[1], galaxy2[1]) or x in range(galaxy2[1], galaxy1[1])]
            vertical_empty_count = len(vertical_empties_in_range)
            horizontal_empties_in_range = [x for x in horizontal_empties if x in range(galaxy1[0], galaxy2[0]) or x in range(galaxy2[0], galaxy1[0])]
            horizontal_empty_count = len(horizontal_empties_in_range)

            cross_point_count = vertical_empty_count + horizontal_empty_count - len(set(vertical_empties_in_range).intersection(horizontal_empties_in_range))

            shortest_paths[idx1, idx2] = np.abs(galaxy1[0] - galaxy2[0]) + np.abs(galaxy1[1] - galaxy2[1]) + horizontal_empty_count*multiplicator + vertical_empty_count*multiplicator - cross_point_count

    return int(np.sum(shortest_paths/2))
    

print("Part 1: ", main(True))
print("Part 2: ", main(False))
