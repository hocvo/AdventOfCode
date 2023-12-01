import util
import queue

inputVal = util.parse('input9.txt')
#inputVal = util.parse('test.input')

m = []
maxCol = 0
maxRow = len(inputVal)
neighbor = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for line in inputVal:
    r = util.splitNum(line)
    m.append(r)

maxCol = len(m[0])
print('r:%i c:%i' % (maxRow, maxCol))

def check_surround(r, c):
    loc = m[r][c]
    candidateLow = []
    for n in neighbor:
        i = r + n[0]
        j = c + n[1]
        if i >= 0 and i < maxRow and j >= 0 and j < maxCol:
            surround = m[i][j]
            if (surround <= loc):
                candidateLow.append((i, j))
    return candidateLow


seen = set()
allLow = []
for i in range(maxRow):
    for j in range(maxCol):
        if (i,j) in seen:
            continue
        q = queue.Queue()
        q.put((i, j))
        while not q.empty():
            loc = q.get()
            r = loc[0]
            c = loc[1]
            if (r, c) in seen:
                continue
            seen.add((r, c))
            surround = check_surround(r, c)
            if len(surround) > 0:
                for l in surround:
                    q.put(l)
            else:
                allLow.append(m[r][c])

output = 0
#Part 1
for i in allLow:
    output += i + 1
print(output)
