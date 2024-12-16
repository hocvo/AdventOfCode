import util
import time
import re
from operator import mul
from functools import reduce
import logging
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
np.seterr(divide='ignore', invalid='ignore')
np.set_printoptions(linewidth=100, formatter={'all': lambda x: f'{x:<1}'}) 
lines = util.parse('d15.txt')
#lines = util.parse('test.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
MV = {'v':(1,0),
      '^':(-1,0),
      '>':(0,1),
      '<':(0,-1)}
      
def main():
    gps = 0
    input = util.splitOnElement(lines, "")
    m = input[0]
    for i in range(len(m)):
        m[i] = list(m[i])
    m = np.matrix(m)
    moves = input[1][0]
    R = m.shape[0]
    C = m.shape[1]
    # print (m)
    # print(moves)
    
    index = np.where(m == '@')
    (curR,curC) = index[0][0], index[1][0]
    # print((curR,curC))
    for move in moves:
        (curR,curC) = shift(m, (curR,curC), move)
    boxes = np.where(m == 'O')
    for box in boxes[0]:
        gps += 100* box
    for box in boxes[1]:
        gps += box
    print(gps)

def shift(m, pos, direction):
    (curR,curC) = pos
    (nextR,nextC) = (curR + MV[direction][0], curC + MV[direction][1])
    # print("shifting ",pos, "->", (nextR,nextC))
    ret = pos
    shifted = True
    if m[nextR,nextC] == "#":
        return ret
    elif m[nextR,nextC] == "O":
        ret = shift(m, (nextR,nextC), direction)
    if ret != (nextR,nextC):
        # print("swapping",(curR,curC), "<->", (nextR,nextC))
        m[nextR,nextC],m[curR,curC] = m[curR,curC],m[nextR,nextC]
        ret = (nextR,nextC)
    else:
        ret = pos
    # print(m)
    return ret
    
def shift2(m, posList, direction):
    objList = list()
    # print("Processing", posList, [m[r,c] for (r,c) in posList])
    for (curR,curC) in posList:
        (nextR,nextC) = (curR + MV[direction][0], curC + MV[direction][1])
        # print("Checking to move", (curR,curC), m[curR,curC], direction, (nextR,nextC), m[nextR,nextC])
        if (nextR,nextC) in posList:
            continue
        if m[nextR,nextC] == "#":
            return False
        elif m[nextR,nextC] == "[":
            if (nextR,nextC) not in objList:
                objList.append((nextR,nextC))
            if (nextR,nextC+1) not in objList:
                objList.append((nextR,nextC+1))
        elif m[nextR,nextC] == "]":
            if (nextR,nextC) not in objList:
                objList.append((nextR,nextC))
            if (nextR,nextC-1) not in objList:
                objList.append((nextR,nextC-1))
    # print("object in the way:", objList, [m[r,c] for (r,c) in objList])
    canShift = True
    if elementIn(m, objList, {"[","]"}):
        canShift = shift2(m, objList, direction)
    # for (r,c) in objList:
        # if m[r,c] != '.':
            # canShift = False
            # break
    if canShift:
        #todo shift all posList
        # print("Doable, shifting all")
        for i in reversed(range(len(posList))):
            (curR,curC) = posList[i]
            (nextR,nextC) = (curR + MV[direction][0], curC + MV[direction][1])
            # print("swapping",(curR,curC), "<->", (nextR,nextC))
            m[nextR,nextC],m[curR,curC] = m[curR,curC],m[nextR,nextC]
    # print(m)
    return canShift
def elementIn(m, objList, vals):
    for (r,c) in objList:
        if m[r,c] in vals:
            return True
    return False
def main2():
    gps = 0
    input1 = util.splitOnElement(lines, "")
    m = input1[0]
    for i in range(len(m)):
        l = list()
        for c in (m[i]):
            if c == "#":
                l.append("#")
                l.append("#")
            elif c == "O":
                l.append("[")
                l.append("]")
            elif c == "@":
                l.append("@")
                l.append(".")
            else:
                l.append(".")
                l.append(".")
        m[i] = l
    m = np.matrix(m)
    moves = ''.join(input1[1])
    print (m)
    print(moves)
    
    index = np.where(m == '@')
    (curR,curC) = index[0][0], index[1][0]
    print((curR,curC))
    i = 0
    for move in moves:
        # print("Moving @", move, i)
        if shift2(m, [(curR,curC)], move):
            (curR,curC) = (curR + MV[move][0], curC + MV[move][1])
        # print(m)
        i += 1
    print (m)
    boxes = np.where(m == '[')
    for box in boxes[0]:
        gps += 100* box
    for box in boxes[1]:
        gps += box
    print(gps)
start = time.time()
main2()
stop = time.time()
print("Main run in: ", stop-start, "seconds")
