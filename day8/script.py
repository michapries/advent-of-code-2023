import numpy as np
import pandas as pd
from datetime import date
from collections import defaultdict
import math

def get_day():
    return date.today().strftime('%-d')


def get_input():
    with open(f'./day8/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day8/testinput{task}.txt', 'r') as input:
            return input.readlines()


def parse(part):
    if part == 0:
        input = [x.strip('\n') for x in get_input() if x.strip('\n') != '']
    else:
        input = [x.strip('\n') for x in get_testinput(part) if x.strip('\n') != '']

    rl = input[0]
    network = dict()
    for map in input[1:]:
        split = map.split(' = ')
        network[split[0]] = tuple(split[1].replace(')', '').replace('(', '').replace(' ', '').split(','))
    
    return rl, network


def main(is_part1):
    rl, network = parse(0)
    
    # Indices where each of the starting nodes encouters a Z for the first time during the traversal.
    z_indices = [-1] * 6

    cur_nodes = ['AAA'] if is_part1 else [node for node in network.keys() if node[2] == 'A']
    i = 0
    while True:
        cur_direction = rl[i % len(rl)]
        i += 1
        
        new_nodes = list()

        for idx, node in enumerate(cur_nodes):
            new_nodes.append(network[node][0] if cur_direction == 'L' else network[node][1])
            if new_nodes[-1][2] == 'Z':
                z_indices[idx] = i
            
        if is_part1 and new_nodes[0] == 'ZZZ':
            return i
        elif not is_part1 and -1 not in z_indices:
            return math.lcm(*z_indices)
        else:
            cur_nodes = new_nodes


print("Part 1: ", main(True))

print("Part 2: ", main(False))
