import util
import time
import re
import random
import numpy as np
np.set_printoptions(linewidth=100, formatter={'all': lambda x: f'{x:<2}'})
# np.set_printoptions(linewidth=100)
lines = util.parse('test.txt')
MAXTRIAL = 20
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

count = 0
def main():
    global count
    m = lines
    for i in range(len(m)):
        m[i] = list(m[i])
    m = np.matrix(m, np.dtype('U100'))
    R = m.shape[0]
    C = m.shape[1]
    index = np.where(m == 'S')
    start = index[0][0], index[1][0]
    print("S pos", start)
    print("S", start)
    end = np.where(m == 'E')
    endPos = end[0][0], end[1][0]
    print("end pos",endPos)
    print(m)
    
    time = [start] #index = time, value = location
    time2 = {start:0}
    q = []
    q.append(start)
    seen = set()
    i = 0
    while q:
        curPos = q.pop(0)
        if curPos in seen:
            continue
        seen.add(curPos)
        for n in util.neighborsCrossIndex(m, curPos[0], curPos[1]):
            if n in seen:
                continue
            if m[n] == '.' or n == endPos:
                time.append(n)
                i += 1
                time2[n] = i
                q.append(n)
    # seen = set()
    maxSave = 0
    for i in range(len(time)):
        seen = {}
        curPos = time[i]
        if curPos in seen:
            continue
        for n in util.neighborsCrossIndex(m, curPos[0], curPos[1]):
            if m[n] == '#':
                # startTime is i+1 because it's one block away from #
                saved =recurse(m, time2, n, i, curPos, endPos, MAXTRIAL-1, seen)
                maxSave = max(maxSave, saved)
        # seen.remove(curPos)
        # if curPos in seen:
            # continue
        # seen.add(curPos)
        # for n in util.neighborsCrossIndex(m, curPos[0], curPos[1]):
            # if m[n] == '#':
                # maxSave = 0
                # for n2 in util.neighborsCrossIndex(m, n[0], n[1]):
                    # if n2 == curPos or n2 in seen:
                        # continue
                    # if m[n2] == '.' or n2 == endPos:
                        # saved = time.index(n2) - (i+2)
                        # # print("Found . at",n2, "save",saved)
                        # maxSave = max(maxSave, saved)
                    # # input('continue')
                # if maxSave >= 64:
                    # count += 1
    count = 0
    for k,v in processed.items():
        if v == 70:
            count += 1
            # print(k)
    print(count)
    # print("MaxSave", maxSave)
    # print(save)
    # print(len(time))
processed = {}
def recurse(m, time, pos, startTime, initPos, endPos, trial, seen):
    # print(trial)
    global count
    if trial < 0:
        return 0
    if pos in seen and trial < seen[pos]:
        return 0
    seen[pos] = trial
    R = m.shape[0]
    C = m.shape[1]
    if pos[0] == 0 or pos[0] == R-1 or pos[1] == 0 or pos[1] == C-1:
        # seen.remove(pos)
        return 0
    maxSave = 0
    # print("Processing ", pos, MAXTRIAL-trial)
    # tmp = m.copy()
    # tmp[pos] = str(MAXTRIAL - trial)
    # print(tmp)
    # input('continue')
    neighbors = util.neighborsCrossIndex(m, pos[0], pos[1])
    neighbors.sort(key=lambda x: m[x],reverse=True)
    for n2 in neighbors:
        if n2 == pos or n2 in seen:
            continue
        # print("Processing n2", n2)
        if m[n2] == '.' or n2 == endPos:
            saved = time[n2] - (startTime+ MAXTRIAL-trial +1)
            # if initPos == (3,1):
                # if endPos == n2:
                    # print("found end", saved,startTime, MAXTRIAL,trial)
                    # input('continue')
            if (n2,initPos) in processed and saved > processed[(n2,initPos)]:
                processed[(n2,initPos)] = saved
            elif (n2,initPos) not in processed and saved > 0:
                processed[(n2,initPos)] = saved
            # maxSave = max(maxSave, saved)
            # if n2 == endPos:
                # return maxSave
            # seen[n2] = trial-1
            # print("Found . at",n2, "save",saved)
        elif m[n2] == '#':
            recurse(m, time, n2, startTime, initPos, endPos, trial - 1, seen)
            # maxSave = max(maxSave, recurse(m, time, n2, startTime, initPos, endPos, trial - 1, seen))
            # print("Found # at",n2, " recurse and save", maxSave)
        # input('continue')
    # input('continue')
    del seen[pos]
    return maxSave
def BFS(m, time, startTime, initPos, endPos):
    # q = []
    # q.append((initPos,MAXTRIAL))
    # while q:
        # add to seen
        # 
def main2():
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

#p2 5758 too low