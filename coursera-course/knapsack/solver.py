#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
import numpy as np


def recurse_options():
    #https://www.geeksforgeeks.org/generate-all-the-binary-strings-of-n-bits/

    return options

def loop_options():
    #do my loop with n iterations, flipping and copying

    return options


def solve_brutish(file_location):
    t = np.loadtxt(file_location, dtype=int)

    capacity = t[0,1]
    n = t[0,0]

    ##generate sequence of zeros of length n: s
    perms = np.zeros((1, n), dtype=int)
    for i in range (0, n):
        tmp = np.copy(perms) #copy existing matrix
        tmp[:,i] = 1 # set value of column i to 1
        perms = np.append(perms, tmp, axis = 0) # append to existing matrix
    
    value = t[1:,].transpose()[0:,][0] #get value item
    weight = t[1:,].transpose()[1:,][0] #get weight item
    option_value = np.sum((value * perms), axis=1) # get value per permutation
    option_weight = np.sum((weight * perms), axis=1) # get weight per permutation
    ok = np.where(option_weight <= capacity) # get valid permutations
    value = option_value[ok].max() # get valid permutation with max value
    answer = perms[np.where(option_value==value)][0] #this is the silly one, need to match on value as we dont have index
    
    return ' '.join(map(str, answer)) #np.array2string(answer)


def solve_naive(file_location):
    # Modify this code to run your optimization algorithm

    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
 
    taken = [0]*len(items)

    value = 0
    weight = 0

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':

    options = ['naive', 'brutish']
    choose = 1
    import sys
    if len(sys.argv) > 0:
        #file_location = sys.argv[1].strip()
        file_location = "/data/repos/discrete-opt/coursera-course/knapsack/data/ks_4_0"

        print(globals()['solve_' + options[choose]](file_location))    
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

