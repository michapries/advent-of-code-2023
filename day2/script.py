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


# Replaces semicolons by commas (because semicolons are useless anyway) and performs the necessary splits.
# Returns list of all num color combinations (e.g. '6 red') of a game.
def extract_num_color_strings(row):
    row = row.split(': ')[1].replace(';', ',')
    comma_split = [x.strip() for x in row.split(',')]
    return comma_split


def task_one():
    input = get_input()
    
    id_sum = 0

    for row in input:       
        game_id = int(row[5:row.find(':')])
        
        num_color_strings = extract_num_color_strings(row)

        for elem in num_color_strings:
            num, color = elem.split(' ')

            if color == 'red' and int(num) > 12:
                break
            elif color == 'green' and int(num) > 13:
                break
            elif color == 'blue' and int(num) > 14:
                break
        else:                           # If the inner for loop was never broken, this case is reached.
            id_sum += game_id

    return id_sum


def task_two():
    input = get_input()

    power_sum = 0

    for row in input:
        # Dict of current maximums for each color.
        max_dict = {'red': 0, 'green': 0, 'blue': 0}

        num_color_strings = extract_num_color_strings(row)

        for elem in num_color_strings:
            num, color = elem.split(' ')
            
            if int(num) > max_dict[color]:
                max_dict[color] = int(num)

        power_sum += math.prod(list(max_dict.values()))

    return power_sum


def main(is_task2):
    if not is_task2:
        return task_one()
    else:
        return task_two()


print("Task 1: ", main(False))

print("Task 2: ", main(True))
