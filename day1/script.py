import numpy as np
import pandas as pd
from datetime import date
from num2words import num2words
from words2num import w2n

def get_input():

    day = date.today().strftime('%-d')

    with open(f'./day1/input.txt', 'r') as input:
        return input.readlines()


# Returns first and last digit of the string.
# include_words is a boolean that is used to include the words for each digit (task 2).
def calc_digits(row, include_words):
    digits = [-1, -1]

    nums = [str(x) for x in range(10)]
    
    if include_words:
        nums.extend([num2words(x) for x in range(10)])

    min_first_idx = np.inf
    max_last_idx = -1

    for num in nums:
        first_idx = row.find(num)
        last_idx = row.rfind(num)
        
        if first_idx < min_first_idx and first_idx != -1:
            digits[0] = int(num) if row[first_idx].isdigit() else int(w2n(row[first_idx : first_idx + len(num)]))
            min_first_idx = first_idx

        if last_idx > max_last_idx:
            digits[1] = int(num) if row[last_idx].isdigit() else int(w2n(row[last_idx : last_idx + len(num)]))
            max_last_idx = last_idx

    return digits 


def main(is_task2):
    input = get_input()
    print(input)

    sum = 0

    for row in input:
        digits = calc_digits(row, is_task2)
        sum += digits[0] * 10 + digits[1]

    return sum

print("Task 1: ", main(False))
    
print("Task 2: ", main(True))
