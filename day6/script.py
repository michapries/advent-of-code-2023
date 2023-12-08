import numpy as np
import pandas as pd
from datetime import date
import math

def get_day():
    return date.today().strftime('%-d')


def get_input():
    with open(f'./day6/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day6/testinput{task}.txt', 'r') as input:
            return input.readlines()


def main(is_task1):
    #input = [x.strip('\n').split() for x in get_testinput(1)]
    input = [x.strip('\n').split() for x in get_input()]

    td_dict = dict()

    if is_task1:
        for i in range(1, len(input[0])):
            td_dict[int(input[0][i])] = int(input[1][i])
    else:
        td_dict[int(''.join(input[0][1:]))] = int(''.join(input[1][1:]))

    distances = list()
    for total_time in td_dict.keys():

        # This basically is the length of the list of all holding times that yield a longer distance than the record.
        distances.append(2 * len([get_distance(holding_time, total_time) for holding_time in range(math.ceil(total_time/2)) if get_distance(holding_time, total_time) > td_dict[total_time]]))

        # If the total time is even (i.e., the number of possible choices is odd due to the possibiliy of zero), the middle element needs to be counted once.
        if total_time % 2 == 0:
            distances[-1] += 1
        
    return math.prod(distances)


# Returns distance that the boat will travel when held for holding_time and the total time is total_time
def get_distance(holding_time, total_time):
    return (total_time - holding_time) * holding_time


print("Task 1: ", main(True))

print("Task 2: ", main(False))
