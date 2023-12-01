import util, logging, sys, math, collections
logger = logging.getLogger('AoC')

handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

lines = util.parse('input11.txt')
monkeys = dict()

newMonkey = False
for i in range(0,len(lines),7):
    logger.debug('adding monkey {} '.format(lines[i]))
    monkeyNum = lines[i].split(' ')[1].strip(':')
    monkeyNum = int(monkeyNum)
    itemStr = lines[i+1].split(': ')[1].split(', ')
    items = []
    for itm in itemStr:
        items.append(int(itm))
    op = lines[i+2].split('= ')[1]
    test = int(lines[i+3].split(' ')[-1])
    throwTrue = int(lines[i+4].split(' ')[-1])
    throwFalse = int(lines[i+5].split(' ')[-1])
    monkeys[monkeyNum] = (items, op, test, throwTrue, throwFalse)

print(monkeys)
logAt = [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
result = dict()
div = 1
for m in monkeys:
    div = div * monkeys[m][2]

for i in range(10000):
    for m in monkeys:
        (items, op, test, t, f) = monkeys[m]
        while items:
            itm = items.pop(0)
            #if 'old' in op.split('* ')[-1]:
            #if '*' in op:
            #    itm = itm % test + test
            #itm = (itm % test) + test
            new = eval(op.replace('old', str(itm))) % div
            #if '+' in op:
            #    new = new % test
            #if '*' in op:
            #if 'old' in op.split('* ')[-1]:
            #    new = new % test + test
            if (new % test) == 0:
                (a, op2, t2, x,y) = monkeys[t]
                #if '*' in op2:
                #    new = new % t2# + t2
                monkeys[t][0].append(new)
            else:
                (a, op2, t2, x,y) = monkeys[f]
                #if '*' in op2:
                #    new = new % t2# + t2
                monkeys[f][0].append(new)
            if m in result:
                result[m] += 1
            else:
                result[m] = 1
    if i+1 in logAt:
        logger.debug('Round {}: {}'.format(i+1,result))
    #print (result)
#result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
#result = dict(sorted(result.items(), key=lambda item: item[1]))
print(result)
l = list(result.values())
l.sort()
print(l[-1] * l[-2])
