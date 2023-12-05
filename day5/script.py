import numpy as np
import pandas as pd
from datetime import date
from collections import defaultdict

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


def part_one():
    input = [x.strip('\n') for x in get_input() if x.strip('\n') != '']
    seeds = list(map(int, input.pop(0).split(': ')[1].split(' ')))
    
    map_dict = dict()

    for elem in input:
        if ':' in elem:
            key_elem = elem.strip(' map:')
        else:
            if key_elem in map_dict.keys():
                map_dict[key_elem].append(list(map(int, elem.split(' '))))
            else:
                map_dict[key_elem] = [list(map(int, elem.split(' ')))]
    
    locations = dict()      # Key: Source, Val: Location of the source.
    for source in seeds:
        destination = source
        for maps in map_dict.values():
                destination = get_destination_for_source(destination, maps)      # The destination is the new source for the next connection (each connection has a number of maps).
        locations[source] = destination
    
    print("seeds and locations:", locations)
    return np.min(list(locations.values()))


# Calculates the destination for a given source given the maps of a single connection.
def get_destination_for_source(source, maps):
    for m in maps:
        m = list(map(int, m))

        if source in range(m[1], m[1] + m[2]):
            diff = source - m[1]
            return m[0] + diff

    return source


def main(is_task1):
    if is_task1:
        return part_one()
    else:
        pass


print("Task 1: ", main(True))

print("Task 2: ", main(False))
