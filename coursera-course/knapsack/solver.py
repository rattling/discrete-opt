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


def brute_force(taken, items, capacity):
    n = len(taken)
    perms = np.zeros(1, n)
    for i in range (0, n-1):
        tmp = np.copy(perms)
        tmp[:i] = 1
        perms = np.append(perms, tmp, axis = 0)
    
    print(perms)



    ##generate sequence of zeros of length n: s
    ##generate table of options
    #for i = 1: n:
        #copy s
        #i col = 1
        #append to s
    #multiply the binaries by their weights/values to get and weight/value total per rows
    #get row with max value where max weight >= capacity
    #if not already, convert it to a list and return it along with total weight and value for it

    #return taken, value, weight

def naive(taken, items, capacity):

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full

    value = 0
    weight = 0

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return taken, value, weight




def solve_it(input_data):
    # Modify this code to run your optimization algorithm

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

    taken, value, weight = naive(taken, items, capacity)

    brute_force(taken, items, capacity)
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 0:
        #file_location = sys.argv[1].strip()
        file_location = "/data/repos/discrete-opt/coursera-course/knapsack/data/ks_4_0"
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

