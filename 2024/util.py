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
            logger.info()
        else:
            logger.info(str(item) + delim)

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
    R = len(matrix)
    C = len(matrix[0])
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