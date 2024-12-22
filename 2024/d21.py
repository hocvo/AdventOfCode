import util
import time
import re
import random
import numpy as np
np.set_printoptions(linewidth=100, formatter={'all': lambda x: f'{x:<2}'})
# np.set_printoptions(linewidth=100)
lines = util.parse('d21.txt')
MAXTRIAL = 20
MAXSIZE = 999999
#lines = util.parse('test.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
NumadMoves = {'0': ['','>v','v','<v','>vv','vv','<vv','>vvv','vvv','<vvv','<'],
         '1': ['^<','','<','<<','v','<v','<<v','vv','<vv','<<vv','^<<'],
         '2': ['^','>','','<','>v','v','<v','>vv','vv','<vv','^<'],
         '3': ['^>','>>','>','','>>v','>v','v','>>vv','>vv','vv','^'],
         '4': ['^^<','^','^<','^<<','','<','<<','v','<v','<<v','^^<<'],
         '5': ['^^','>^','^','^<','>','','<','v>','v','<v','^^<'],
         '6': ['^^>','^>>','^>','^','>>','>','','>>v','>v','v','^^'],
         '7': ['^^^<','^^','^^<','<<^^','^','^<','^<<','','<','<<','^^^<<'],
         '8': ['^^^','^^>','^^','^^<','^>','^','^<','>','','<','^^^<'],
         '9': ['^^^>','^^>>','^^>','^^','^>>','^>','^','>>','>','','^^^'],
         'A': ['>','>>v','>v','v','>>vv','>vv','vv','>>vvv','>vvv','vvv','']}
DirectionalMoves = {'^':['','^','>^','<^','<'],
                   'v':['v','','>','<','v<'],
                   '<':['v<','<','','<<','v<<'],
                   '>':['v>','>','>>','','v'],
                   'A':['>','^>','>>^','^','']}
DirectionalKeyMap = {'^':0,'v':1,'<':2,'>':3,'A':4}
curKey = ['A','A','A'] #numpad, robot1, robot2
def main():
    count = 0
    m = [['7','8','9'],['4','5','6'],['1','2','3'],['X','0','A']]
    m = np.matrix(m,np.dtype('U100'))
    print(m)
    lines = ['029A','980A','179A','456A','379A']
    lines = ['379A']
    for l in lines:
        #curKey = ['A','A','A'] #not neccessary because they always end at A
        #print('Processing', l)
        mCount = 0
        fullpress = ''
        for k in l:
            print("pressing",k)
            robot1 =  moveNumpad(k, curKey[0])
            print("robot1",robot1, 'curKey:', curKey[1])
            robot1 = findShortest(curKey[1], robot1) + 'A'
            print("robot1",robot1)
            for r1K in robot1:
                robot2 = moveDirectional(r1K, curKey[1])
                print("robot2",robot2, 'curKey:',curKey[2])
                robot2 = findShortest(curKey[2], robot2) + 'A' # rearrange keys before process to get best result
                print("robot2",robot2)
                for r2K in robot2:
                    human = moveDirectional(r2K, curKey[2]) + 'A'
                    curKey[2] = r2K
                    print("human",human)
                    mCount += len(human)
                    fullpress += human
                    #for r2K in robot2:
                    #    human = moveDirectional(r2K+'A')
                curKey[1] = r1K
            curKey[0] = k
            input('continue')
        print('Done processing',l,'with',mCount,'pressed', fullpress)
        count += int(l[:-1]) * mCount
    print(count)
def moveNumpad(key,curKey):
    #curKey = 'A'
    #print('Moving num:', key)
    count = ''
    for k in key:
        if curKey == 'A':
            curKey = 10
        else:
            curKey = int(curKey)
        count += NumadMoves[k][curKey]
        curKey = k
    return count
def moveDirectional(key,curKey):
    #curKey = 'A'
    #print('Moving direction:', key)
    count = ''
    for k in key:
        locK = DirectionalKeyMap[curKey]
        direction = DirectionalMoves[k][locK]
        #print("curkey, locK", curKey, locK)
        count += direction
        curKey = k
    return count
def findShortest(curKey, direction):
    tmp = direction
    direction = list(direction)
    direction.sort(key=lambda x:len(DirectionalMoves[x][DirectionalKeyMap[curKey]]))
    if tmp != ''.join(direction):
        print("changing direction", tmp, 'to', ''.join(direction))
    return ''.join(direction)

print(findShortest('>','<v'))
input('start')
start = time.time()
main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")

#p1 155948 too low
#169612 too high
