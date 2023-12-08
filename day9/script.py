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


def part1():
    return


def part2():
    return


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1: ", main(True))

print("Part 2: ", main(False))
