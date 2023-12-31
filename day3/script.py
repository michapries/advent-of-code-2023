import numpy as np
import pandas as pd
from datetime import date
import math

def get_day():
    return date.today().strftime('%-d')


def get_input():
    with open(f'./day3/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day3/testinput{task}.txt', 'r') as input:
            return input.readlines()


# Returns a single number and all of its indices based on i and j of its leftmost digit in the array.
def get_number_indices(i, j, arr):
    indices = []  # List of index tuples.
    num = ''

    # Iterate from left to right.
    for k in range(j, arr.shape[1]):
        if arr[i, k].isdigit():
            indices.append((i, k))
            num = num + arr[i, k]
        else:
            break
    
    if num != '':
        return int(num), indices
    else:
        return -1, indices


# Just to make sure, extract all possible symbols from the input.
def get_possible_symbols():
    symbols = set()
    with open(f'./day3/input.txt', 'r') as input:
        for x in input.read():
            if not x.isdigit() and x not in ['.', '\n']:
                symbols.add(x)

    return symbols


# Returns true if a symbol is adjacent to the given index in the array.
def is_symbol_adjacent(i, j, arr):
    possible_symbols = get_possible_symbols()
    for new_i in range(i-1, i+2):
        for new_j in range(j-1, j+2):
            if new_i < arr.shape[0] and new_j < arr.shape[1] and arr[new_i, new_j] in possible_symbols:
                return True

    return False


def extract_numbers_indices(arr):
    # Indices of all numbers that have been seen so far 
    # Keys: Numbers with their first index as id to avoid clashes if numbers occur multiple times ( e.g. 776_(0, 10) and 776_(128, 16) )
    # Values: Lists of the numbers' indices.
    numbers_indices = dict()

    # Fill numbers_indices.
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            num, indices = get_number_indices(i, j, arr)
            
            if num != -1:    
                prev_indices = []
                if len(numbers_indices) > 0:
                    last_key = list(numbers_indices)[-1] 
                    prev_indices = list(numbers_indices[last_key])

                # prev_indices contains the indices of the last added number in numbers_indices.
                # We only need to check the first index of indices against this.
                if indices[0] not in prev_indices:
                    if num in [x.split('_')[0] for x in numbers_indices.keys()]:
                        numbers_indices[str(num) + '_' + str(indices[0])].extend(indices)
                    else:
                        numbers_indices[str(num) + '_' + str(indices[0])] = indices

    return numbers_indices


def task_one():
    input = [x.strip('\n') for x in get_input()] 
    
    sum = 0

    arr = np.array([list(x) for x in input])   

    numbers_indices = extract_numbers_indices(arr)
                       
    # Check for adjacency.
    for num, indices in [(n.split('_')[0], ind) for n, ind in numbers_indices.items()]:     # The list comprehension unpacks the actual number from the unique key.
        for idx in indices:
            if is_symbol_adjacent(idx[0], idx[1], arr):
                sum += int(num)
                break

    return sum


# Returns a list of the indices of all asterisks.
def get_all_asterisks(arr):
    return np.array(np.where(arr == '*')).T


# i, j are the indices of the asterisk. Returns the indices of all digits around it (might be of the same number).
def get_adjacent_numbers_to_asterisk(i, j, arr):
    for new_i in range(i-1, i+2):
        for new_j in range(j-1, j+2):
            if new_i < arr.shape[0] and new_j < arr.shape[1] and arr[new_i, new_j].isdigit():
                return True 


def task_two():
    input = [x.strip('\n') for x in get_input()] 
    
    sum = 0
    
    arr = np.array([list(x) for x in input])    

    numbers_indices = extract_numbers_indices(arr)

    # Key: asterisk index separated by comma (e.g. 124,29), Value: list of adjacent numbers
    asterisks_numbers = {}

    for i, j in get_all_asterisks(arr):
        seen_nums = []
        for new_i in range(i-1, i+2):
            for new_j in range(j-1, j+2):
                if new_i < arr.shape[0] and new_j < arr.shape[1] and arr[new_i, new_j].isdigit():
                    for unique_num, indices in numbers_indices.items():
                        actual_num = int(unique_num.split('_')[0])
                        for idx in indices: 
                            #print(idx, (i, j))
                            if idx == (new_i, new_j) and unique_num not in seen_nums:
                                seen_nums.append(unique_num)
                                key = str(i) + ',' + str(j)
                                if key not in asterisks_numbers.keys():
                                    asterisks_numbers[key] = [actual_num]
                                else:
                                    asterisks_numbers[key].append(actual_num)

    # Check if len = 2 and multiply and add accordingly.
    for numbers in asterisks_numbers.values():
        if len(numbers) == 2:
            sum += numbers[0] * numbers[1]

    return sum


def main(is_task2):
    if not is_task2:
        return task_one()
    else:
        return task_two()


print("Task 1: ", main(False))

print("Task 2: ", main(True))
