import numpy as np
import pandas as pd
from datetime import date

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

def task_one():
    input = get_input()
    
    id_sum = 0

    for row in input:       
        game_id = int(row[5:row.find(':')])
        row = row.split(': ')[1].replace(';', ',')      # Replace semicolons by commas because we don't need the semicolons anyway for task 1.
        
        semi_split = [x.strip() for x in row.split(',')]

        for elem in semi_split:
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


def main(is_task2):
    if not is_task2:
        return task_one()
    else:
        return ""


print("Task 1: ", main(False))

print("Task 2: ", main(True))
