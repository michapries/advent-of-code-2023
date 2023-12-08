import numpy as np
import pandas as pd
from datetime import date
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
    #input = [x.strip('\n') for x in get_input() if x.strip('\n') != '']
    rl = input[0]
    network = dict()
    for map in input[1:]:
        split = map.split(' = ')
        network[split[0]] = tuple(split[1].replace(')', '').replace('(', '').replace(' ', '').split(','))
    
    return rl, network


def part1():
    rl, network = parse(0)
    
    i = 0
    cur_node = 'AAA'

    while True:
        cur_direction = rl[i % len(rl)]
        i += 1
        new_node = network[cur_node][0] if cur_direction == 'L' else network[cur_node][1]
        if new_node == 'ZZZ':
            return i
        else:
            cur_node = new_node

        
def part2():
    return
                

def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1: ", main(True))

print("Part 2: ", main(False))
