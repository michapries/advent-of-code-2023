import numpy as np
import pandas as pd
from datetime import date
import math
from collections import defaultdict

def get_day():
    return date.today().strftime('%-d')


def get_input():
    with open(f'./day10/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day10/testinput{task}.txt', 'r') as input:
            return input.readlines()

    
def get_connecting_neighbors(grid, i, j):
    node = grid[i][j]
    up = ['|', '7', 'F', 'S']
    down = ['|', 'L', 'J', 'S']
    left = ['-', 'L', 'F', 'S']
    right = ['-', 'J', '7', 'S']

    valid_directions = defaultdict(list)
    if node in down and grid[i-1][j] in up and i-1 < grid.shape[0]:
        valid_directions[f'{grid[i-1][j]}_{str(i-1)}_{str(j)}'] = (i-1, j)
    if node in up and grid[i+1][j] in down and i+1 < grid.shape[0]:
        valid_directions[f'{grid[i+1][j]}_{str(i+1)}_{str(j)}'] = (i+1, j)

    if node in left and grid[i][j+1] in right and j+1 < grid.shape[1]:
        valid_directions[f'{grid[i][j+1]}_{str(i)}_{str(j+1)}'] = (i, j+1)
    if node in right and grid[i][j-1] in left and j-1 < grid.shape[1]:
        valid_directions[f'{grid[i][j-1]}_{str(i)}_{str(j-1)}'] = (i, j-1)

    return dict(valid_directions)


def animal_search(grid, i, j):
    already_visited = list()
    iterations = 0
    while True:
        neighbors = {k.split('_')[0]: v for k, v in get_connecting_neighbors(grid, i, j).items() if v not in already_visited and k != 'S'}
        if not neighbors:
            break
        neighbor_vals = list(neighbors.values())
        
        already_visited.append((i, j))

        i, j = neighbor_vals[0][0], neighbor_vals[0][1]
        iterations += 1
        
    return math.ceil(iterations/2)


def part1():
    #grid = np.array([[*x.strip('\n')] for x in get_testinput(1)])
    grid = np.array([[*x.strip('\n')] for x in get_input()])
    s = [x[0] for x in np.where(grid == 'S')]
    print(animal_search(grid, s[0], s[1]))


def part2():
    return


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1: ", main(True))
print("Part 2: ", main(False))
