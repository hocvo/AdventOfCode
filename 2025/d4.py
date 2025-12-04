from tensorflow.python.ops.metrics_impl import false_negatives

import util
import time
import numpy as np
from collections import deque
np.seterr(divide='ignore', invalid='ignore')
np.set_printoptions(linewidth=100, formatter={'all': lambda x: f'{x:<1}'})

lines = util.parse('d4.txt')

def part1():
    count = 0
    m = lines
    for i in range(len(m)):
        m[i] = list(m[i])
    m = np.matrix(m)
    R = m.shape[0]
    C = m.shape[1]
    q = deque()
    q.append((0,0))
    prev = -1
    while prev < count:
        prev = count
        # print(m)
        rollIdx = set()
        for i in range(R):
            for j in range(C):
                if m[i,j] != '@':
                    continue
                # i,j = q.pop()
                neighbors = util.allNeighborsIndexNp(m,i,j)
                # for n in neighbors:
                #     if m[n] == '@':
                #         q.append(n)
                toiletRolls = 0
                for n in neighbors:
                    if m[n] == '@':
                        toiletRolls += 1
                if toiletRolls < 4:
                    count += 1
                    rollIdx.add((i,j))
        for rI in rollIdx:
            m[rI] = '.'
    print(count)
start = time.time()
part1()
# part2()
stop = time.time()
print(stop-start)