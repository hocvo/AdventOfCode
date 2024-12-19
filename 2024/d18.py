import util
import time
import re
import random
import numpy as np
np.set_printoptions(linewidth=100, formatter={'all': lambda x: f'{x:<1}'})
lines = util.parse('d18.txt')
MSIZE = 71
FALLEN = 1024
MAXSIZE = 999999
#lines = util.parse('test.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))

def main():
    count = 0
    endPos = (MSIZE-1,MSIZE-1)
    m = np.full((MSIZE,MSIZE),'.')
    falls = []
    i = 0
    for i in range(FALLEN):
        l = lines[i]
        loc = l.split(',')
        index = (int(loc[0]),int(loc[1]))
        m[index] = '#'
    print(m)
    for j in range(i,len(lines)):
        l = lines[j]
        loc = l.split(',')
        index = (int(loc[0]),int(loc[1]))
        m[index] = '#'
        # print(m)
        dist = np.full((MSIZE,MSIZE), MAXSIZE)
        prev = {}
        dijsktra(m, dist, (0,0), prev)
        if dist[endPos] == MAXSIZE:
            print("Found coor:", index)
            break
        
    # prev = {}
    # endPos = (MSIZE-1,MSIZE-1)
    # count = dist[endPos]
    # curPos = endPos
    # while curPos in prev:
        # curPos = prev[curPos]
        # m[curPos] = "#" #block the path
        
        # # call dijsktra again
        # # newPrev = {}
        # dist = np.full((m.shape[0],m.shape[1]), MAXSIZE)
        # face = np.zeros((m.shape[0],m.shape[1]), dtype=int)
        # score = dijsktra(m, dist, (0,0), {})
        # # print("new score", score, "==", minScore)

        # # if score = min with blocked path, that mean there is a new path
        # # add count tile for new path before continue (cur path still block)
        # if dist[endPos] == MAXSIZE:
            # print("Found coor:", curPos)
        
        #reset the path and count the current tile that is blocked
        # m[curPos] = tmp
    print(count)
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
def dijsktra(m, dist, initPos, prev):
    # eScore = 999999
    
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
            score = dist[curPos] + 1
            # print("Neighbors score:",n, rot, score)
            if score < dist[n]:
                dist[n] = score
                prev[n] = curPos
    # print(dist)
    # print(eScore)
    # input("continue")
    # return eScore
def getMin(q, dist):
    minDist = MAXSIZE
    pos = 0
    for i in range(len(q)):
        if dist[q[i]] < minDist:
            minDist = dist[q[i]]
            pos = i
    return q.pop(pos)
start = time.time()
main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")