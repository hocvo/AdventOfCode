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
lines = util.parse('d16.txt')
#lines = util.parse('test.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
MIN_SCORE = sys.maxsize
faces = {0:'>', 1:'^', 2:'<', 3:'v'}
def main():
    global MIN_SCORE
    m = lines
    for i in range(len(m)):
        m[i] = list(m[i])
    m = np.matrix(m)
    R = m.shape[0]
    C = m.shape[1]
    # print (m)
    index = np.where(m == 'S')
    curPos = index[0][0], index[1][0]
    print("S pos",curPos)
    print("S", curPos)
    # dfs(m, set(), curPos, 0, 0)
    # print("DFS",MIN_SCORE)
    # MIN_SCORE = bfs(m, curPos, 0)
    # print("BFS",MIN_SCORE)
    prev = dict()
    
    end = np.where(m == 'E')
    endPos = end[0][0], end[1][0]
    print("end pos",endPos)
    # MIN_SCORE = dijsktra2(m, curPos, prev)
    # MIN_SCORE = dijsktra(m, endPos, prev)

    # print(m)
    # print("Dijsktra",MIN_SCORE, tile)
    dist = np.full((m.shape[0],m.shape[1]), 999999)
    face = np.zeros((m.shape[0],m.shape[1]), dtype=int)
    minScore = dijsktra(m,dist, face,curPos, endPos, prev)
    print("Init score",minScore)
    tile = countTile(minScore, prev,m, set())
    print(tile+1)
def countTile(minScore, prev, m, seen):
    tile = 0
    
    index = np.where(m == 'S')
    if 0 == index[0].size:
        return tile
    startPos = index[0][0], index[1][0]
    end = np.where(m == 'E')
    endPos = end[0][0], end[1][0]

    curPos = endPos
    while curPos in prev:
        curPos = prev[curPos]
        # keep track of tile before the junction
        if curPos in seen:
            continue
        seen.add(curPos)
        tmp = m[curPos]
        m[curPos] = "#" #block the path
        
        # call dijsktra again
        newPrev = dict()
        dist = np.full((m.shape[0],m.shape[1]), 999999)
        face = np.zeros((m.shape[0],m.shape[1]), dtype=int)
        score = dijsktra(m, dist, face, startPos, endPos, newPrev)
        # print("new score", score, "==", minScore)

        # if score = min with blocked path, that mean there is a new path
        # add count tile for new path before continue (cur path still block)
        if score == minScore:
            print("tile before new path",tile)
            tile += countTile(minScore, newPrev, m, seen)
        
        #reset the path and count the current tile that is blocked
        m[curPos] = tmp
        tile += 1
    return tile
def dfs(m, seen, curPos, facing, curScore):
    global MIN_SCORE
    (curR,curC) = curPos
    if curPos in seen:
        return
    # print("at", curPos, curScore)
    seen.add(curPos)
    if m[curR,curC] == "#":
        return
    if m[curR,curC] == "E":
        if curScore < MIN_SCORE:
            print("found new min:", curScore)
            MIN_SCORE = curScore
        return        
    if curScore >= MIN_SCORE:
        return
    # draw(m, curPos, facing)
    curScore += 1
    neighbors = util.neighborsCrossIndex(m, curPos[0], curPos[1])
    for n in neighbors:
        seenTmp = seen.copy()
        rot = turn(curPos, facing, n)
        dfs(m, seenTmp, n, rot[0], curScore + rot[1])
    return

def bfs(m, initPos, initFacing):
    q = list()
    q.append((initPos,initFacing,0, set()))
    minScore = sys.maxsize
    
    # plt.ion()
    # figure, ax = plt.subplots()
    # visM = np.vectorize(ord)(m)
    # im = ax.imshow(visM, cmap='cividis')
    # sameDirSeen = set()
    while q:
        (curPos, facing, curScore, seen) = q.pop()
        (curR,curC) = curPos
        # print("at", curPos)
        if curPos in seen:
            continue
        seen.add(curPos)
        # sameDirSeen.add(curPos)
        if m[curR,curC] == "#":
            continue
        if m[curR,curC] == "E":
            if curScore < minScore:
                print("found new min:", curScore)
                minScore = curScore
            continue        
        if curScore >= minScore:
            continue

        # m[curR,curC] = faces[facing]
        # visM = np.vectorize(ord)(m)
        # im = ax.imshow(visM, cmap='cividis')
        # figure.canvas.draw()
        # This will run the GUI event
        # loop until all UI events
        # currently waiting have been processed
        # figure.canvas.flush_events()
        
        # print("at", curPos, curScore)
        curScore += 1
        for n in util.neighborsCrossIndex(m, curPos[0], curPos[1]):
            if n in seen or m[curR,curC] == "#":
                continue
            seenTmp = seen.copy()
            rot = turn(curPos, facing, n)
            q.append((n,rot[0],curScore+rot[1],seenTmp))
        # time.sleep(0.5)
    return minScore

def dijsktra2(m, initPos, prev):
    eScore = 0
    dist = np.full((m.shape[0],m.shape[1]), np.iinfo(np.int32).max)
    face = np.zeros((m.shape[0],m.shape[1]), dtype=int)
    dist[initPos] = 0
    q = []
    for i in range(len(dist)):
        for j in range(len(dist[i])):
            q.append((i,j))
    # print(g)
    while q:
        curPos = getMin(q, dist)
        # print("Processing:",curPos)
        for n in util.neighborsCrossIndex(m, curPos[0], curPos[1]):
            if m[n] == "#" or n not in q:
                continue
            rot = turn(curPos, face[curPos], n)
            score = dist[curPos] + 1 + rot[1]
            # print("Neighbors score:",n, rot, score)
            if score < dist[n]:
                if m[n] == "E":
                    # print("Found End")
                    eScore = score
                dist[n] = score
                face[n] = rot[0]
                if n in prev:
                    # print("Append new Prev to End", prev[n])
                    prev[n].append(curPos)
                else:
                    # print("Set new Prev to End")
                    prev[n] = [curPos]
    # print(dist)
    return eScore

def dijsktra(m, dist, face, initPos, endPos, prev):
    eScore = 999999
    
    # print(m)
    dist[initPos] = 0
    q = []
    for i in range(len(dist)):
        for j in range(len(dist[i])):
            q.append((i,j))
    # print(g)
    while q:
        curPos = getMin(q, dist)
        # print("Processing:",curPos)
        for n in util.neighborsCrossIndex(m, curPos[0], curPos[1]):
            if m[n] == "#" or n not in q:
                continue
            rot = turn(curPos, face[curPos], n)
            score = dist[curPos] + rot[1] + 1
            # print("Neighbors score:",n, rot, score)
            if score < dist[n]:
                if n == endPos:
                    # print("Found End")
                    eScore = score
                dist[n] = score
                face[n] = rot[0]
                # if n in prev:
                    # print("Append new Prev to End", prev[n])
                prev[n] = curPos
                # else:
                    # print("Set new Prev to End")
                    # prev[n] = [curPos]
    # print(dist)
    # print(eScore)
    # input("continue")
    return eScore

def getMin(q, dist):
    minDist = sys.maxsize
    pos = 0
    for i in range(len(q)): 
        (r,c) = q[i]
        if dist[r,c] < minDist:
            minDist = dist[r,c]
            pos = i
    return q.pop(pos)
def turn(curPos, curFacing, nextPos):
    score = 0
    (curR,curC) = curPos
    (nextR,nextC) = nextPos
    nextFacing = curFacing
    if nextC - curC == 1:
        nextFacing = 4 - curFacing
    elif nextC - curC == -1:
        nextFacing =  2 - curFacing
    else:
        if nextR - curR == -1:
            nextFacing =  1 - curFacing
        else:
            nextFacing =  3 - curFacing
    nextFacing = nextFacing % 4
    if nextFacing == 3:
        score = 1000
    else:
        score = 1000 * nextFacing
    return ((nextFacing+curFacing)%4,score)
def draw(m,curPos,facing):
    tmp = m.copy()
    (r,c) = curPos
    if tmp[r,c] == '.':
        tmp[r,c] = faces[facing]
        print(tmp)
start = time.time()
main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")

#89380 using SameSirSeen too high

#445 too low 10134 too high