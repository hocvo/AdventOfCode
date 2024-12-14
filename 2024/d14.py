import util
import time
import re
from operator import mul
from functools import reduce
import logging
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
lines = util.parse('d14.txt')
logger = logging.getLogger('AoC')
logging.basicConfig(filename='d14.log', level=logging.INFO)
#lines = util.parse('test.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
Ppattern = 'p=(\d*),(\d*)'
Vpattern = 'v=(-?\d*),(-?\d*)'
XTILE = 101
#XTILE = 11
XMID = int(XTILE/2)
YTILE = 103
#YTILE = 7
YMID = int(YTILE/2)
TIME = 100
def main():
    safeFactor = 0
    quad = [1,0,0,0,0]
    for r in lines:
        pMatch = re.search(Ppattern,r)
        p = (int(pMatch.group(1)), int(pMatch.group(2)))
        vMatch = re.search(Vpattern,r)
        v = (int(vMatch.group(1)), int(vMatch.group(2)))
        x = move(p[0],v[0],XTILE)
        y = move(p[1],v[1],YTILE)
#        print("moving",p,v, "to", x,y)
        if x < XMID:
            if y < YMID:
                quad[1] += 1
            elif y > YMID:
                quad[3] += 1
        elif x > XMID:
            if y < YMID:
                quad[2] += 1
            elif y > YMID:
                quad[4] += 1
    safeFactor = reduce(mul, quad)
    #print(quad)
    print(safeFactor)
def main2():
    minSec = 0
    for i in range(100000):
        pos = list()
        for r in lines:
            pMatch = re.search(Ppattern,r)
            p = (int(pMatch.group(1)), int(pMatch.group(2)))
            vMatch = re.search(Vpattern,r)
            v = (int(vMatch.group(1)), int(vMatch.group(2)))
            p = ((p[0]+v[0])% XTILE, (p[1]+v[1])%YTILE)
            pos.append(p)
        #util.printMatrix(m)
    print(minSec)
def createMatrix(pos):
    m = list()
    for i in range(YTILE):
        m.append(list())
        for j in range(XTILE):
            if (i,j) in pos:
                m[i].append('1')
            else:
                m[i].append('.')
    return m
def move(p, v, limit):
    newPos = (p + v*TIME) % limit
    return newPos

start = time.time()
#main()
m = np.random.rand(5, 5)
x = np.random.randn(50, 50)
x[15, :] = 0.
x[:, 40] = 0.

plt.spy(x, precision = 0.1, markersize = 5)

main2()
stop = time.time()
print("Main run in: ", stop-start, "seconds")
#73888848 too low
#95670432 too low
#226868688 too high
#216115424 not right
#220574870 swap X,Y TILE
#214400550
