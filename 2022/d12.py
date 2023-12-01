import util, logging, sys, string
logger = logging.getLogger('AoC')

handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

lines = util.parse('input12.txt')
m = []
S = None
E = None
for i in range(len(lines)):
    l = lines[i]
    m.append(l)
    if 'S' in l:
        S = (i,l.index('S'))
    if 'E' in l:
        E = (i,l.index('E'))


elevParamData = 'S' + string.ascii_lowercase + 'E'
def isValid(x ,y):
    #logger.debug("isValid: {},{}".format(x,y))
    xI = elevParamData.index(x)
    yI = elevParamData.index(y)
    if (xI+1) >= yI:
        return True
    return False
rNum = len(m)
cNum = len(m[0])
q = list()
seen = dict()
q.append((S,0)) # 0 = step count
stepCount = set()
nI = [(0,1),(0,-1),(1,0),(-1,0)]
while q:
    # only step up at most 1
    # if neighbor valid, add to q
    # keep a count with each item in q
    (curPos,count) = q.pop(0)
    if curPos in seen:
        if count > seen[curPos]:
            continue
    seen[curPos] = count
    curElev = m[curPos[0]][curPos[1]]
    logger.debug('Processing {} elev:{} c:{}'.format(curPos, curElev, count))
    if curElev == 'E':
        logger.debug('Found a path with {} steps'.format(count))
        stepCount.add(count)
        continue
    for n in nI:
        row = curPos[0] + n[0]
        col = curPos[1] + n[1]
        if row < 0 or col < 0 or row >= rNum or col >= cNum:
            continue
        if (row, col) in seen:
            continue
        #logger.debug("Neighbor: {}".format(m[row][col]))
        #logger.debug("Neighbor: {},{}".format(row,col))
        if isValid(curElev, m[row][col]):
            #logger.debug("Adding {}".format(m[row][col]))
            q.append(((row,col),count+1))
    # if neighbor = E, done. update count

print(stepCount)
