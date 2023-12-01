import util
from queue import Queue

inputVal = util.parse('input12.txt')
#inputVal = util.parse('test3.txt')

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

count = 0
def createpath(node, smallcave, allowVisit):
    global count
    if node == 'end':
        count += 1
        return True
    if node in smallcave:
        if allowVisit and node != 'start' and node != 'end':
            allowVisit = False
        else:
            return False
    elif node.islower():
        smallcave.add(node)
    for e in g[node]:
        createpath(e, set(smallcave), allowVisit)
    return False

for n in g:
    if n == 'start':
       createpath(n, set(), True)

#print(len(allpaths))
print(count)
