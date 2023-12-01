import util, logging, sys
logger = logging.getLogger('AoC')

handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

lines = util.parse('input9.txt')

n = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
def isTouch(head, tail):
    if head == tail:
        return True
    around = []
    for neighbor in n:
        r = head[0]+neighbor[0]
        c = head[1]+neighbor[1]
        around.append((r,c))
    if tail in around:
        return True
    return False

def move(knot, nextKnot, row, col):
    #after move, still same row
    if isTouch(knot, nextKnot):
        return nextKnot
    if knot[0] == nextKnot[0]:
        y = knot[1] - nextKnot[1]
        if y > 0:
            y = 1
        elif y < 0:
            y = -1
        nextKnot = (nextKnot[0], nextKnot[1]+y)
    # same col
    elif knot[1] == nextKnot[1]:
        x = knot[0] - nextKnot[0]
        if x > 0:
            x = 1
        elif x < 0:
            x = -1
        nextKnot = (nextKnot[0]+x, nextKnot[1])
    # diagnal
    else:
        x = knot[0]-nextKnot[0]
        y = knot[1]-nextKnot[1]
        r = nextKnot[0]
        c = nextKnot[1]
        if x > 0:
            r += 1
        elif x < 0:
            r -= 1
        if y > 0:
            c += 1
        elif y < 0:
            c -= 1
        nextKnot = (r,c)
    #logger.debug("Tail move to {}".format(nextKnot))
    return nextKnot

r = 0
c = 0
tailFp = set()
dir = {'U':[1,0], 'D':[-1,0], 'R':[0,1], 'L':[0,-1]}
head = (r,c)
tail = (r,c)
tailFp.add(tail)
logger.debug("Head at {}".format(head))
logger.debug("Tail at {}".format(tail))
knots = list()
kNum = 10
for i in range(kNum):
    knots.append((0,0))
for i in range(len(lines)):
    (d, dist) = lines[i].split(' ')
    dist = int(dist)
    row = dir[d][0]
    col = dir[d][1]
    logger.debug("moving {} {} {}".format(d,dist, dir[d]))
    for k in range(dist):
        #oldHead = head
        head = knots[0]
        # update head
        knots[0] = (head[0]+row, head[1]+col)
        #check knots in sequence and move if necessary
        logger.debug("Head is at {}".format(knots[0]))
        for j in range(kNum-1):
            curKnot = knots[j+1]
            knots[j+1] = move(knots[j],knots[j+1],row, col)
            logger.debug("H{} {}->{}".format(j+1,curKnot,knots[j+1]))
        logger.debug("Tail is at {}".format(knots[kNum-1]))
        tailFp.add(knots[kNum-1])
        #after move, still same row
        #if isTouch(tail, head):
        #    continue
        #if head[0] == tail[0]:
        #    tail = (tail[0], tail[1]+col)
        ## same col
        #elif head[1] == tail[1]:
        #    tail = (tail[0]+row, tail[1])
        ## diagnal
        #else:
        #    tail = oldHead
        #logger.debug("Tail move to {}".format(tail))
        #tailFp.add(tail)
print(len(tailFp))
