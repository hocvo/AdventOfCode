import util

inputVal = util.parse('input6.txt')[0]
#inputVal = '16,1,2,0,4,2,7,1,2,14'
inputVal = inputVal.split(',')
inputVal = list(map(int, inputVal))

count = {}
for i in inputVal:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

output = 999999999999
for i in range(len(count)):
    fuel = 0
    for j in count:
        if j == i:
            continue
        # fuel += abs(j - i) * count[j]
        steps = abs(j-i)
        f = 0
        for s in range(steps):
            f += s+1
        fuel += f * count[j]
    output = min(fuel, output)
print(output)
# 96438974
# 96798233
