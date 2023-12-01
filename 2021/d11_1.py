import util
from queue import Queue

inputVal = util.parse('input11.txt')
#inputVal = util.parse('test.input')
#inputVal = util.parse('test.txt')

m = []
surround = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for line in inputVal:
    row = util.splitNum(line)
    m.append(row)
maxR = len(m)
maxC = len(m[0])

def flash(q):
    flashed = set()
    flashCount = 0
    while not q.empty():
        flashCount += 1
        (r,c) = q.get()
        if (r,c) in flashed:
            continue
        m[r][c] = m[r][c] % 10
        flashed.add((r,c))
        for (i,j) in surround:
            nR = r+i
            nC = c+j
            if nR < 0 or nR >= maxR or nC < 0 or nC >= maxC:
                continue
            if m[nR][nC] == 0 or m[nR][nC] >= 10:
                continue
            if (nR,nC) in flashed:
                continue
            m[nR][nC] += 1
            if m[nR][nC] >= 10:
                #m[nR][nC] = m[nR][nC] % 10
                q.put((nR,nC))
    return flashCount

def step():
    q = Queue()
    for r in range(len(m)):
        for c in range(len(m[0])):
            m[r][c] += 1
            if m[r][c] >= 10:
                #m[r][c] = m[r][c] % 10
                q.put((r,c))
    flashCount = flash(q)
    return flashCount

totalFlash = 0
size = maxR * maxC
#for i in range(200):
i = 0
while True:
    flashCount = step()
    if (flashCount == size):
        print('Sync at: %i' %(i+1))
        break
    totalFlash += flashCount
    #print(flashCount)
    i += 1
print(totalFlash)
