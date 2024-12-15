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
TIME = 8135
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
    print(quad)
    print(safeFactor)

def getNumCluster(m, p):
    count = 0
    q = list()
    (x,y) = p
    q.append((y,x))
    seen = set()
    while q:
        (r,c) = q.pop(0)
        if (r,c) in seen:
            continue
        seen.add((r,c))
        count += 1
        for (i,j) in util.neighborsCrossIndex(m,r,c):
            if m[i][j] > 0:
                q.append((i,j))
    return count

def visualize(frame):
    global matrix, ani,plt
    global i, maxCluster
    # print(matrix)
    # clus = (0,0)
    for robot in robots:
        clusterCount = getNumCluster(matrix,robot[0])
        if clusterCount > maxCluster:
            print("found higher cluster at ",i, clusterCount, robot[0])
            # clus = robot[0]
            # input("press enter to continue")
            maxCluster = clusterCount
    if i == 8149:
        input("press enter to continue")
        # ani.event_source.pause()
        # plt.close()
    i += 1
    matrix = np.zeros((YTILE, XTILE), dtype=int)
    for j in range(len(robots)):
        (x,y) = robots[j][0]
        v = robots[j][1]
        (newX, newY) = ((x+v[0])%XTILE, (y+v[1])%YTILE)
        robots[j] = ((newX, newY),v)
        matrix[newY][newX] = 50
    # for r in range(len(matrix)):
        # for c in range(len(matrix[r])):
            # if matrix[r][c] > 0:
                # matrix[r][c] = matrix[r][c] - 25
    
    if i % 100 == 0:
        print("i:",i)
    # print(i,np.count_nonzero(matrix))
    im.set_data(matrix)
    return [im]

def move(p, v, limit):
    newPos = (p + v*TIME) % limit
    return newPos

# start = time.time()
# main()

i = TIME
matrix = np.zeros((YTILE, XTILE), dtype=int)
maxCluster = 5
fig, ax = plt.subplots()
#init position
robots = list()
for r in lines:
    pMatch = re.search(Ppattern,r)
    p = (int(pMatch.group(1)), int(pMatch.group(2)))
    vMatch = re.search(Vpattern,r)
    v = (int(vMatch.group(1)), int(vMatch.group(2)))
    x = move(p[0],v[0],XTILE)
    y = move(p[1],v[1],YTILE)
    robots.append(((x,y),v))
    matrix[y][x] = 50
# Create an image plot
im = ax.imshow(matrix, cmap='cividis')

# print(matrix)
# Create the animation
ani = FuncAnimation(fig, visualize, frames=500, interval=1000, blit=False)

# Show the animation
plt.show()
print(i)
# stop = time.time()
# print("Main run in: ", stop-start, "seconds")
