import util
import time
import sys
from operator import mul
from functools import reduce
import logging
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
from queue import PriorityQueue
np.seterr(divide='ignore', invalid='ignore')
np.set_printoptions(linewidth=100, formatter={'all': lambda x: f'{x:<1}'})

sys.setrecursionlimit(99999)
lines = util.parse('test.txt')
#lines = util.parse('test.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
seen = dict()
def main():
    param = util.splitOnElement(lines,"")
    avail = set(param[0][0].split(', '))
    countPos = 0
    # print(avail)
    for pattern in param[1]:
        # pos += recurse(avail, pattern)
        i = len(pattern)
        print("Processing", pattern)
        arrange = []
        while i > 0:
            isPos = recurse(avail, pattern[:i]) and recurse(avail, pattern[i:], arrange)
            if isPos:
                print("Found one", pattern[:i], pattern[i:], countPos+1)
                countPos += 1
            i -= 1
    print(countPos)
def recurse(avail, pattern, arrange):
    # print("Checking", pattern)
    if pattern == '':
        return True
    possible = False
    if pattern in seen:
        # print("Found in seen")
        return seen[pattern]
    if pattern in avail:
        # print("Found in avail")
        possible = True
    i = len(pattern)-1 #last index
    while i > 0:
        possible = recurse(avail, pattern[:i]) and recurse(avail, pattern[i:])
        if possible:
            arrange.append(pattern[:i]
            break
        i -= 1
    seen[pattern] = possible
    # print('Returning', possible)
    # input('continue')
    return possible
    
start = time.time()
main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")
