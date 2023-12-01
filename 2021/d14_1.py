import util

inputVal = util.parse('input14.txt')
template = 'BVBNBVPOKVFHBVCSHCFO'
inputVal = util.parse('test.txt')
template = 'NNCB'

m = {}
countMap = {}
s = template

for l in inputVal:
    l = l.split(' -> ')
    m[l[0]] = l[1]

for c in s:
    if c in countMap:
        countMap[c] += 1
    else:
        countMap[c] = 1


for j in range(10):
    newS = ''
    for i in range(len(s)-1):
        first = s[i]
        second = s[i+1]
        btw = m[first+second]
        newS += first+btw
        if btw in countMap:
            countMap[btw] += 1
        else:
            countMap[btw] = 1
    newS += s[-1]
    #print(newS)
    s = newS

print(countMap)
print(len(newS))
high = 0
low = 99999999999999
for c in countMap:
    high = max(high,countMap[c])
    low = min(low, countMap[c])
print('high: %i low: %i' %(high, low))
print(high-low)

