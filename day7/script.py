import numpy as np
import pandas as pd
from datetime import date
import math
from collections import defaultdict
from collections import Counter

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
    input = [x.strip('\n').split(' ') for x in get_testinput(1)]
    input = [x.strip('\n').split(' ') for x in get_input()]
    input = [(hand, int(bid)) for hand, bid in input]

    hands_with_strength = defaultdict(list)

    for hand, bid in input:
        hands_with_strength[get_strength(hand)].append((hand, bid))

    for strength, hands_bids in hands_with_strength.items():
        hands_bids = [([*hand], bid) for hand, bid in hands_bids]     # Converts string to char lists
        hands_with_strength[strength] = sorted([(convert_hand_to_int(hand), bid) for hand, bid in hands_bids], reverse=True)

    sum = 0
    i = 0
    for strength in sorted(hands_with_strength.keys(), reverse=True):
        for hand, bid in hands_with_strength[strength]:
            sum += (len(input) - i) * bid
            i += 1
   
    return sum


# Returns hand as a list of ints based on card_values.
def convert_hand_to_int(hand, is_task1):
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, 'J': 1}

    for i in range(len(hand)):
        if hand[i] in card_values.keys():
            hand[i] = card_values[hand[i]]
        else:
            hand[i] = int(hand[i])
    
    return hand


# Ordering: Five of a kind: 5, four of a kind: 4, full house: 3.5, three of a kind: 3, two pair: 2, one pair: 1, high card: 0
def get_strength(hand):
    counts = dict(Counter(hand))
    count_vals = counts.values()
    highest_freq, lowest_freq = np.max(list(count_vals)), np.min(list(count_vals))

    if highest_freq in [4, 5]:
        return highest_freq
    elif highest_freq == 3:
        if lowest_freq == 2:
            return 3.5
        else: 
            return 3
    elif highest_freq == 1:
        return 0
    else:
        if len(count_vals) == 3:
            return 2
        else:
            return 1


def part2():
    return


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1: ", main(True))

print("Part 2: ", main(False))
