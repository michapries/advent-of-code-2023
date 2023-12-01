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


def main(is_task2):
    if not is_task2:
        pass
    else:
        pass


print("Task 1: ", main(False))

print("Task 2: ", main(True))
