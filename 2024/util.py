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


