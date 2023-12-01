import util
from queue import Queue

inputVal = util.parse('input12.txt')
inputVal = util.parse('test.txt')

g = {}
for line in inputVal:
    e = line.split('-')
    if e[0] in g:
        g[e[0]].add(e[1])
    else:
        g[e[0]] = {e[1]}
    if e[1] in g:
        g[e[1]].add(e[0])
    else:
        g[e[1]] = {e[0]}

print(g)
allPaths = []
def createPath(curPath, node, smallCave):
    if node == 'end':
        curPath.append(node)
        allPaths.append(curPath)
        return True
    if node in smallCave:
        if smallCave[node] == 0:
            return False
        else:
            smallCave[node] = 0
    elif node.islower():
        if node == 'start':
            smallCave['start'] = 0
        elif node == 'end':
            smallCave['end'] = 0
        else:
            smallCave[node] = 1
    curPath.append(node)
    for e in g[node]:
        path = list(curPath)
        createPath(curPath, e, dict(smallCave))
    return False

count = 0
for n in g:
    if n == 'start':
       createPath([], n, dict())

print(len(allPaths))
#print(allPaths)
