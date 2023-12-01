import util
lines = util.parse('input5.txt')
crates = list()
for l in lines:
    if not l:
        break;
    crates.append(l)

stack = dict()
numStack = int(crates[-1].split(' ')[-1])
#print(numStack)
#print(crates[0].split(' '))
#print(len(crates))
for i in range(0,len(crates)-1):
    items = crates[i].split(' ')
    j = 0
    #print(items)
    for s in range(1,10):
        #print(j)
        #print(items[j])
        if j < len(items) and items[j]:
            if stack.get(s) == None:
                stack[s] = list()
            if '[' in items[j]:
                stack[s].append(items[j])
                j += 1
        else:
            j += 4
for i in range(1,10):
    stack[i].reverse()
    print(i,stack[i])

#for i in range(numStack+1, len(lines)):
#    l = lines[i]
#    input = l.split(' ')
#    for k in range(int(input[1])):
#        fr = int(input[3])
#        to = int(input[5])
#        #print('from: ', fr, 'to: ', to)
#        #print(stack[fr])
#        #print(stack[to])
#        stack[to].append(stack[fr].pop())

for i in range(numStack+1, len(lines)):
    l = lines[i]
    input = l.split(' ')
    needToMove = []
    to = int(input[5])
    for k in range(int(input[1])):
        fr = int(input[3])
        needToMove.append(stack[fr].pop())
    for k in range(int(input[1])):
        stack[to].append(needToMove.pop())
for i in range(1,10):
    print(stack[i][-1])

