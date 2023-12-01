import util, logging, sys
logger = logging.getLogger('AoC')

handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

lines = util.parse('input10.txt')
vals = []
for i in range(len(lines)):
    l = lines[i]
    if l == 'noop':
        vals.append(0)
    else:
        vals.append(0)
        vals.append(int(l.split(' ')[1]))
#print(vals)

logger.info("Length vals={}".format(len(vals)))
m = [20,60,100,140,180,220]
result = 0
X = 1
for i in range(len(vals)):
    if i+1 in m:
        logger.debug("At {} iter, X={}: X*i={}".format(i+1, X,X*(i+1)))
        result += (i+1) * X
    X += vals[i]
print(result)

newline = [40,80,120,160,200,240]
curLine = ''
X = 1
j = 0
for i in range(len(vals)):
    if i in newline:
        print(curLine)
        curLine = ''
        j = 0
    spite = [X-1,X,X+1]
    logger.debug("spit={} i={}".format(spite,i))
    if j in spite:
        curLine += '#'
    else:
        curLine += '.'
    j += 1
    X += vals[i]
print(curLine)
