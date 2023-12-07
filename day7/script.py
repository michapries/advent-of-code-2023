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


def main(is_part1):
    input = [x.strip('\n').split(' ') for x in get_testinput(1)]
    input = [x.strip('\n').split(' ') for x in get_input()]
    input = [(hand, int(bid)) for hand, bid in input]

    hands_with_strength = defaultdict(list)

    for hand, bid in input:
        hands_with_strength[get_strength(hand, is_part1)].append((hand, bid))

    for strength, hands_bids in hands_with_strength.items():
        hands_bids = [([*hand], bid) for hand, bid in hands_bids]     # Converts string to char lists.
        hands_with_strength[strength] = sorted([(convert_hand_to_int(hand, is_part1), bid) for hand, bid in hands_bids], reverse=True)

    sum = 0
    i = 0
    for strength in sorted(hands_with_strength.keys(), reverse=True):
        for hand, bid in hands_with_strength[strength]:
            sum += (len(input) - i) * bid
            i += 1
   
    return sum


# Returns hand as a list of ints based on card_values.
def convert_hand_to_int(hand, is_part1):
    converted_hand = hand.copy()
    if is_part1:
        card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    else:
        card_values = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, 'J': 1}

    for i in range(len(hand)):
        if hand[i] in card_values.keys():
            converted_hand[i] = card_values[hand[i]]
        else:
            converted_hand[i] = int(hand[i])
    
    return converted_hand


# Ordering: Five of a kind: 5, four of a kind: 4, full house: 3.5, three of a kind: 3, two pair: 2, one pair: 1, high card: 0
def get_strength(hand, is_part1):
    counts = dict(Counter(convert_hand_to_int([*hand], is_part1)))
    
    if not is_part1:
        if 1 in counts.keys():
            del counts[1]

        # Most frequent cards in the hand.
        max_count_keys = [count_key for count_key, count_val in counts.items() if count_val == max(counts.values())]
        
        # Best card of the most frequent ones.
        if max_count_keys:
            max_card = np.max([key for key in max_count_keys])
        
        # Iff hand = 'JJJJJ', counts and max_card are empty.
        if counts and max_card:
            counts[max_card] += len(hand) - np.sum(list(counts.values()))           # Raise frequency of best card in the hand by the number of jokers in the hand
        else:
            counts[1] = 5
    
    highest_freq, lowest_freq = np.max(list(counts.values())), np.min(list(counts.values()))
    
    # Actual logic for strength calculation.
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
        if len(counts.values()) == 3:
            return 2
        else:
            return 1


print("Part 1: ", main(True))

print("Part 2: ", main(False))
