import util

inputVal = util.parse('input14.txt')
template = 'BVBNBVPOKVFHBVCSHCFO'
#inputVal = util.parse('test.txt')
#template = 'NNCB'

m = {}
countMap = {}


for l in inputVal:
    l = l.split(' -> ')
    m[l[0]] = l[1]

for c in template:
    if c in countMap:
        countMap[c] += 1
    else:
        countMap[c] = 1

pairs = dict()
for c in range(len(template)-1):
    p = template[c]+template[c+1]
    if p in pairs:
        pairs[p] += 1
    else:
        pairs[p] = 1
print(m)
print(pairs)
for j in range(40):
    pairTmp = dict(pairs)
    for p in pairTmp:
        newC = m[p]
        count = pairTmp[p]
        if count == 0:
            continue
        if newC in countMap:
            countMap[newC] += count
        else:
            countMap[newC] = count
        pairs[p] -= count
        pair1 = p[0] + newC
        pair2 = newC + p[1]
        if pair1 in pairs:
            pairs[pair1] += count
        else:
            pairs[pair1] = count
        if pair2 in pairs:
            pairs[pair2] += count
        else:
            pairs[pair2] = count
    print(pairs)

length = 0
for p in pairs:
    length += pairs[p]
print(length)

high = 0
low = 99999999999999
for c in countMap:
    high = max(high,countMap[c])
    low = min(low, countMap[c])
print('high: %i low: %i' %(high, low))
print(high-low)

