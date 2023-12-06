import numpy as np
import pandas as pd
from datetime import date
from collections import defaultdict

def get_day():
    return date.today().strftime('%-d')


def get_input():
    with open(f'./day5/input.txt', 'r') as input:
        return input.readlines()
    

def get_testinput(task):
    if task not in [1, 2]:
        raise Exception('Not a valid task.')
    else:
        with open(f'./day5/testinput{task}.txt', 'r') as input:
            return input.readlines()


# Calculates the destination for a given source given the maps of a single connection.
def get_destination_for_source(source, maps):
    for m in maps:
        m = list(map(int, m))

        if source in range(m[1], m[1] + m[2]):
            #destination = m[0] + source - m[1]
            diff = source - m[1]
            return m[0] + diff
        
    return source


def main(is_task1):
    input = [x.strip('\n') for x in get_input() if x.strip('\n') != '']
    #input = [x.strip('\n') for x in get_testinput(1 if is_task1 else 2) if x.strip('\n') != '']
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
    
    locations = dict()      # key: Source, val: Location of the source.
    
    if is_task1:
        for source in seeds:
            destination = source
            for maps in map_dict.values():
                destination = get_destination_for_source(destination, maps)      # The destination is the new source for the next connection (each connection has a number of maps).
            locations[source] = destination
    
    else:
        seeds_ranges = list()
        for idx in range(len(seeds)):
            if idx % 2 == 0:
                seeds_ranges.append(range(seeds[idx], seeds[idx] + seeds[idx+1]))
        #print(seeds_ranges)
        #print("=" * 20)

        range_mappings = list()
        for maps in map_dict.values():
            output_ranges, input_ranges = dest_ranges_for_layer(maps)
            range_mappings.append([output_ranges, input_ranges])
        
        cur_ranges = seeds_ranges
        for layer, range_mapping in enumerate(range_mappings):
            ffff = defaultdict(int)
            #print(layer, range_mapping)
            new_ranges = set()
            for cur_range in cur_ranges:
                
                input_ranges = range_mapping[1]
                did_something = False
                for idx, input_range in enumerate(input_ranges):
                    
                    # print('cur', cur_range)
                    # print('in', input_range)
                    if cur_range[0] >= input_range[0] and cur_range[-1] <= input_range[-1]:
                        out_range = range_mapping[0][idx]
                        # print('cur', cur_range)
                        # print('in', input_range)
                        # print('out', out_range)
                        # print(out_range[cur_range[0] - input_range[0]])
                        # print(out_range[cur_range[-1] - input_range[-1] - 1])
                        
                        if out_range[cur_range[0] - input_range[0]] != out_range[cur_range[-1] - input_range[-1] - 1]:
                            new_ranges.add(range(out_range[cur_range[0] - input_range[0]], out_range[cur_range[-1] - input_range[-1] - 1]))
                        # print('new:', new_ranges[-1])
                        #print("fully inside")
                        did_something = True
                        
                        break
                    elif cur_range[0] <= input_range[0] and cur_range[-1] >= input_range[-1]:
                        new_ranges.add(range_mapping[0][idx])
                        if cur_range[0] - input_range[0] > 0: cur_ranges.append(range(cur_range[0], input_range[0]))
                        if input_range[-1] - cur_range[-1] > 0: cur_ranges.append(range(input_range[-1], cur_range[-1]))
                        did_something = True
                        
                        break
               
                    elif cur_range[0] < input_range[0] and cur_range[-1] <= input_range[-1] and cur_range[-1] > input_range[0]:
                        out_range = range_mapping[0][idx]
                        # print('cur', cur_range)
                        # print('in', input_range)
                        # print('out', out_range)
                        did_something = True
                        #print(out_range[-1] - (input_range[-1] - cur_range[-1]))
                        new_ranges.add(range(out_range[0], out_range[input_range[-1] - cur_range[-1]]))
                        cur_ranges.append(range(cur_range[0], input_range[0]))
                        
                        break
                    elif cur_range[0] > input_range[0] and cur_range[-1] > input_range[-1] and cur_range[0] < input_range[-1]:
                        out_range = range_mapping[0][idx]
                        
                        new_ranges.add(range(cur_range[0] - input_range[0], out_range[-1]))

                        did_something = True
                        cur_ranges.append(range(input_range[-1], cur_range[-1]))
                        
                        break
                
                if not did_something:
                    new_ranges.add(cur_range)                
                    
                
            #print(layer, new_ranges)
            
            cur_ranges = list(new_ranges)
        
        #print(new_ranges)
        lowers = [x[-1]+1 for x in new_ranges]
    
    if is_task1:
        print("seeds and locations:", locations)
        return np.min(list(locations.values()))
    else:
        return np.min(lowers)


def dest_ranges_for_layer(maps):
    output_ranges, input_ranges = list(), list()
    for m in maps:
        output_ranges.append(range(m[0], m[0] + m[2]))
        input_ranges.append(range(m[1], m[1] + m[2]))
    return output_ranges, input_ranges


def get_source_for_destination(destination, maps):
    for m in maps:
        m = list(map(int, m))

        if destination in range(m[1], m[1] + m[2]):
            return destination + m[1] - m[0]

    return destination


print("Task 1: ", main(True))

print("Task 2: ", main(False))
