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

# part 2 code
def check_basin(r, c):
    loc = m[r][c]
    candidate = []
    for n in neighbor:
        i = r + n[0]
        j = c + n[1]
        if i >= 0 and i < maxRow and j >= 0 and j < maxCol:
            surround = m[i][j]
            if surround == 9:
                continue
            if loc <= surround:
                candidate.append((i, j))
    return candidate

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
allLow2 = []
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
                allLow2.append((r,c))

output = 0
# Part 1
for i in allLow:
    output += i + 1
print(output)
# Part 2
seen = set()
allBasinSize = []
for low in allLow2:
    q.put(low)
    basinSize = {low}
    while not q.empty():
        loc = q.get()
        r = loc[0]
        c = loc[1]
        if loc in seen:
            continue
        seen.add(loc)
        surround = check_basin(r,c)
        for l in surround:
            q.put(l)
            basinSize.add(l)
    allBasinSize.append(len(basinSize))

output2 = 1
allBasinSize.sort(reverse=True)
for i in range(3):
    output2 *= allBasinSize[i]
print(output2)
