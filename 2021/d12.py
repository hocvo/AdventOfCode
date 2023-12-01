import util
inputVal = util.parse('input6.txt')
#inputVal = [16,1,2,0,4,2,7,1,2,14]
inputVal = inputVal[0].split(',')
intputVal = map(list,int)
count = {}
for i in inputVal:
    if i in count:
        count[i] += 1
    else:
        count[i] = 0

most = 0
for i in count:
    most = max(most,count[i])

print('most crab are at %i'  %most)
output = 0
for i in inputVal:
    output += abs(i - most)

print(output)
