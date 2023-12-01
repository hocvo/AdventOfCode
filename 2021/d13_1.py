import util
from queue import Queue

inputVal = util.parse('input13.txt')
foldTxt = util.parse('fold.txt')
#inputVal = util.parse('test.txt')
#foldTxt = util.parse('fold_test.txt')

fold = []
for l in foldTxt:
    l = l.strip('fold along ')
    l = l.split('=')
    l[1] = int(l[1])
    fold.append(l)

m = set()
for l in inputVal:
    l = l.split(',')
    m.add((int(l[0]),int(l[1])))

print(len(m))

def printM():
    maxX = 0
    maxY = 0
    for (x,y) in m:
        maxX = max(maxX,x)
        maxY = max(maxY,y)
    for i in range(maxX+1):
        for j in range(maxY+1):
            if (i,j) in m:
                print('#',end='')
            else:
                print('.',end='')
        print('')

#printM()
for f in fold:
    mCopy = set(m)
    if f[0] == 'y':
        foldLine = f[1]
        print('folding at y = %i' % foldLine)
        for (x,y) in mCopy:
            if y >= foldLine:
                m.remove((x,y))
                d = y - foldLine
                newY = foldLine - d
                m.add((x,newY))
    elif f[0] == 'x':
        foldLine = f[1]
        print('folding at x = %i' % foldLine)
        for (x,y) in mCopy:
            if x >= foldLine:
                m.remove((x,y))
                d = x - foldLine
                newX = foldLine - d
                m.add((newX,y))
    #printM()

print(len(m))
printM()

#WVNQAOIC
#EDSGKCHM
#EbSGKCHM
