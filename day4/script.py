import numpy as np
import pandas as pd
from datetime import date
from operator import eq

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


def main(is_task2):
    input = [x.strip('\n') for x in get_input()] 
    
    sum = 0
    card_frequencies = [1] * len(input)

    for idx, row in enumerate(input):
        split = [x.split(' ') for x in row.replace('  ', ' ').split(': ')[1].split(' | ')] 
        for i in range(len(split)):
            split[i] = [int(x) for x in split[i]]
        
        shared_elems = len(set(split[0]).intersection(split[1]))

        # Task 1
        sum += 2 ** (shared_elems - 1) if shared_elems > 0 else 0

        # Task 2
        for i in range(1, shared_elems+1):
            card_frequencies[idx + i] += card_frequencies[idx]

    if not is_task2:
        return sum
    else:
        return np.sum(card_frequencies)


print("Task 1: ", main(False))

print("Task 2: ", main(True))
