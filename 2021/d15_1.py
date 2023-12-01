import util
from queue import Queue

inputVal = util.parse('input15.txt')
#inputVal = util.parse('test.txt')

m = []
for l in inputVal:
    l = util.splitNum(l)
    lTmp = list(l)
    for i in range(1,5):
        for n in lTmp:
            newN = (n+i)%9
            if newN == 0:
                newN = 9
            l.append(newN)
    m.append(l)
mTmp = list(m)
for i in range(1,5):
    for row in mTmp:
        newR = []
        for c in row:
            newC = (c+i)%9
            if newC == 0:
                newC = 9
            newR.append(newC)
        m.append(newR)

maxR = len(m)
maxC = len(m[0])
print(m)
print('%ix%i' %(len(m),len(m[0])))
# Create edge
neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
#neighbors = [(0,1),(1,0)]
seen = set()
edges = set()
nodes = dict()
for i in range(maxR):
    for j in range(maxC):
        #if (i,j) in seen:
        #    continue
        nodes[(i,j)] = 9999999
        #seen.add((i,j))
        #for n in neighbors:
        #    newR = i + n[0]
        #    newC = j + n[1]
        #    if newR >= 0 and newR < maxR and newC >= 0 and newC < maxC:
        #        if (newR,newC) in seen:
        #            continue
        #        edges.add(((i,j),(newR,newC),m[newR][newC]))

q = Queue()
seen = set()
nodes[(0,0)] = 0
q.put((0,0))
while not q.empty():
    (r,c) = q.get()
    if (r,c) in seen:
        continue
#    seen.add((r,c))
    minD = 999
    nextNode = ()
    for n in neighbors:
        newR = r + n[0]
        newC = c + n[1]
        if newR < 0 or newR >= maxR or newC < 0 or newC >= maxC:
            continue
        d = nodes[(r,c)] + m[newR][newC]
        if d < nodes[(newR,newC)]:
            nodes[(newR,newC)] = d
            q.put((newR,newC))
        if d < minD:
            nextNode = (newR,newC)
            minD = d


print(nodes[(maxR-1,maxC-1)])
