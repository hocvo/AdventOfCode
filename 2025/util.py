import numpy as np
import logging
logger = logging.getLogger('AoC')
def parse(filename):
    val=[]
    with open(filename) as f:
        lines = f.readlines()
        logger.info('Read in {} lines'.format(len(lines)))
        for line in lines:
            val.append(line.strip('\n'))
    return val
def write(filename, obj, delim=' '):
    f = open(filename, 'a')
    if isinstance(obj,list):
        __writeList__(f,obj,delim)
    f.close()

def __writeList__(f, l, delim=' '):
    for item in l:
        if isinstance(item, list):
            __writeList__(f,item)
            f.write('\n')
        else:
            f.write(str(item) + delim)

def printObj(obj, delim=' '):
    if isinstance(obj,list):
        printList(obj,delim)

def printList(l, delim = ' '):
    for item in l:
        if isinstance(item, list):
            printList(item)
            logger.info('')
        else:
            logger.info(str(item) + delim)

def printMatrix(m, delim = ''):
    for row in m:
        print(delim.join(row))

# Python3 program to Split string into characters
def split(word):
    return [char for char in word]

def splitNum(word):
    return [int(char) for char in word]

def sort(word):
    chars = split(word)
    chars.sort()
    out = ''
    for c in chars:
        out += c
    return out

def column(matrix, i):
    return [row[i] for row in matrix]

# def diagonal(matrix, i):
    # return [row[i] for row in matrix]

def diagonalForward(matrix, i,j):
    l = list()
    c = j
    maxCol = len(matrix[0])
    for r in range(i,len(matrix)):
        if c >= maxCol:
            break;
        l.append(matrix[r][c])
        c += 1
    return l

def diagonalBackward(matrix, i,j):
    l = list()
    c = j
    maxCol = len(matrix[0])
    for r in range(i,len(matrix)):
        if c < 0:
            break;
        l.append(matrix[r][c])
        c -= 1
    return l

def diagonal(matrix):
    print("to be implemented")

def allNeighbors(matrix, i,j):
    print("cur: ", matrix[i][j])
    R = len(matrix)
    C = len(matrix[0])
    res = list()
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if (r != i or c != j) and r >= 0 and r < R and c >= 0 and c < C:
                res.append(matrix[r][c])
    return res

def allNeighborsIndex(matrix,i,j):
    R = len(matrix)
    C = len(matrix[0])
    res = list()
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if (r != i or c != j) and r >= 0 and r < R and c >= 0 and c < C:
                res.append((r,c))
    return res

def allNeighborsIndexNp(matrix,i,j):
    R = matrix.shape[0]
    C = matrix.shape[1]
    res = list()
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if (r != i or c != j) and r >= 0 and r < R and c >= 0 and c < C:
                res.append((r,c))
    return res

def neighborsCross(matrix, i,j):
    neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    R = len(matrix)
    C = len(matrix[0])
    res = list()
    for (r,c) in neighbors:
            if r >= 0 and r < R and c >= 0 and c < C:
                res.append(matrix[r][c])
    return res

def neighborsCrossIndex(matrix, i,j):
    neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    matrix = np.matrix(matrix)
    R = matrix.shape[0]
    C = matrix.shape[1]
    res = list()
    for (r,c) in neighbors:
            if r >= 0 and r < R and c >= 0 and c < C:
                res.append((r,c))
    return res
def neighborsX(matrix, i,j):
    neighbors = [(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
    R = len(matrix)
    C = len(matrix[0])
    res = list()
    for (r,c) in neighbors:
            if r >= 0 and r < R and c >= 0 and c < C:
                res.append(matrix[r][c])
    return res

def neighborsXIndex(matrix, i,j):
    neighbors = [(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
    R = len(matrix)
    C = len(matrix[0])
    res = list()
    for (r,c) in neighbors:
            if r >= 0 and r < R and c >= 0 and c < C:
                res.append((r,c))
    return res

def splitOnElement(l, element):
    res = list()
    tmp = list()
    for item in l:
        if item == element:
            res.append(tmp)
            tmp = list()
        else:
            tmp.append(item)
    res.append(tmp)
    return res

def find(matrix, value):
    for r in range(len(matrix)):
        row = matrix[r]
        for c in range(len(row)):
            if value == matrix[r][c]:
                return (r,c)
    return (-1,-1)

#https://www.geeksforgeeks.org/dsa/check-if-two-given-line-segments-intersect/
# function to check if point q lies on line segment 'pr'
def onSegment(p, q, r):
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

# function to find orientation of ordered triplet (p, q, r)
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    # collinear
    if val == 0:
        return 0

    # clock or counterclock wise
    # 1 for clockwise, 2 for counterclockwise
    return 1 if val > 0 else 2


# function to check if two line segments intersect
def doIntersect(seg1,seg2):
    # find the four orientations needed
    # for general and special cases
    o1 = orientation(seg1[0], seg1[1], seg2[0])
    o2 = orientation(seg1[0], seg1[1], seg2[1])
    o3 = orientation(seg2[0], seg2[1], seg1[0])
    o4 = orientation(seg2[0], seg2[1], seg1[1])

    # general case
    if o1 != o2 and o3 != o4:
        return True

    # special cases
    # p1, q1 and p2 are collinear and p2 lies on segment p1q1
    if o1 == 0 and onSegment(seg1[0], seg2[0], seg1[1]):
        return True

    # p1, q1 and q2 are collinear and q2 lies on segment p1q1
    if o2 == 0 and onSegment(seg1[0], seg2[1], seg1[1]):
        return True

    # p2, q2 and p1 are collinear and p1 lies on segment p2q2
    if o3 == 0 and onSegment(seg2[0], seg1[0], seg2[1]):
        return True

    # p2, q2 and q1 are collinear and q1 lies on segment p2q2 
    if o4 == 0 and onSegment(seg2[0], seg1[1], seg2[1]):
        return True

    return False
    
# assume 0,0 is at top left. +x going right
# +y is going down
def pointInPolygon2D(x,y,xy):
    #test horizon:
    segment = [(0,y),(x,y)]
    horizontal_count = 0
    for i in range(len(xy)):
        polygon_segment = [xy[i],xy[(i+1)%len(xy)]]
        horizontal_count += 1 if doIntersect(segment, polygon_segment) else 0
    
    #test vertical:
    segment = [(x,0),(x,y)]
    vertical_count = 0
    # for i in range(len(xy)):
        # polygon_segment = [xy[i],xy[(i+1)%len(xy)]]
        # vertical_count += 1 if doIntersect(segment, polygon_segment) else 0
    if horizontal_count%2 == 1 or vertical_count%2 == 1:
        return True
    # print((x,y), 'is not inside')
    return False
# useful function
#     xy is a list of tuple (x,y)
#     # sorted_x = sorted(xy, key=lambda x: (x[0],x[1]))
#     # sorted_y = sorted(xy, key=lambda x: (x[1],x[0]))
#     max_x = max(xy, key=lambda x: x[0])
#     min_x = min(xy, key=lambda x: x[0])
#     max_y = max(xy, key=lambda x: x[1])
#     min_y = min(xy, key=lambda x: x[1])
