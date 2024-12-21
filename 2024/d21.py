import util
import time
import re
import random
import numpy as np
np.set_printoptions(linewidth=100, formatter={'all': lambda x: f'{x:<2}'})
# np.set_printoptions(linewidth=100)
lines = util.parse('test.txt')
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
         '1': ['^<','','<','<<','v','v<','v<<','vv','<vv','<<vv','^<<'],
         '2': ['^','>','','<','>v','v','v<','vv>','vv','vv<','^<'],
         '3': ['^>','>>','>','','>>v','>v','v','>>vv','>vv','vv','^'],
         '4': ['^^<','^','^<','^<<','','<','<<','v','<v','<<v','^^<<'],
         '5': ['^^','>^','^','^<','>','','<','v>','v','<v','^^<'],
         '6': ['^^>','^>>','^>','^','>>','>','','>>v','>v','v','^^'],
         '7': ['^^^<','^^','^^<','^^<<','^','^<','^<<','','<','<<','^^^<<'],
         '8': ['^^^','^^>','^^','^^<','^>','^','^<','>','','<','^^^<'],
         '9': ['^^^>','^^>>','^^>','^^','^>>','^>','^','>>','>','','^^^'],
         'A': ['>','>>v','>v','v','>>vv','>vv','vv','>>vvv','>vvv','vvv','']}
DirectionalMoves = {'^':['','v','v<','v>','>'],
                   'v':['^','','<','>','>^'],
                   '<':['>^','>','','>>','>>^'],
                   '>':['<^','<','<<','','^'],
                   'A':['<','v<','v<<','v']}
DirectionalKeyMap = {'^':0,'v':1,'<':2,'>':3,'A':4}
curKey = ['A','A','A'] #numpad, robot1, robot2
def main():
    count = 0
    m = [['7','8','9'],['4','5','6'],['1','2','3'],['X','0','A']]
    m = np.matrix(m,np.dtype('U100'))
    print(m)
    lines = ['029A']
    for l in lines:
        mCount = 0
        prevK = 'A'
        for k in l:
            print("pressing",k)
            numpad = moveNumpad(k, curKey[0]) + 'A'
            print("numpad",move)
            for numK in numpad:
                robot1 = moveDirectional(numK, curKey[1]) + 'A'
                for r1K in robot1:
                    robot2 = moveDirectional(r1K, curKey[2])
                    for r2K in robot2:
                        human = moveDirectional(r2K+'A')
            #move = moveDirectional(move+'A', curKey[2])
            #move = moveDirectional(move+'A', prevK)
            mCount += len(human)+1 #add A at the end for our own press
            prevK = k
            input('continue')
        count += int(l[:-1]) * mCount
        print(count)
    print(count)
def moveNumpad(key,curKey):
    #curKey = 'A'
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
    curKey = 'A'
    count = ''
    for k in key:
        locK = DirectionalKeyMap[curKey]
        count += DirectionalMoves[k][locK]
        curKey = k
    return count
start = time.time()
main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")

#p2 5758 too low
