import util
import re
import numpy as np
lines = util.parse('d4.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))

def searchHorizon(lines):
    count = 0
    for l in lines:
        count += len(re.findall("XMAS", l))
        count += len(re.findall("SAMX", l))
    return count
def searchVertical(lines):
    count = 0
    numCol = len(lines[0])
    # print (''.join())
    for col in range(numCol):
        l = ''.join(util.column(lines, col))
        count += len(re.findall("XMAS", l))
        count += len(re.findall("SAMX", l))
    return count    
def searchDiagnal(lines):
    count = 0
    for r in range(len(lines)):
        l = ''.join(util.diagonalForward(lines, r,0))
        count += len(re.findall("XMAS", l))
        count += len(re.findall("SAMX", l))
    for c in range(1,len(lines[0])):
        l = ''.join(util.diagonalForward(lines, 0,c))
        count += len(re.findall("XMAS", l))
        count += len(re.findall("SAMX", l))
    for r in range(len(lines)):#5 backward
        l = ''.join(util.diagonalBackward(lines, r,len(lines[0])-1))
        count += len(re.findall("XMAS", l))
        count += len(re.findall("SAMX", l))
    for c in range(len(lines[0])-1):
        l = ''.join(util.diagonalBackward(lines, 0,c))
        count += len(re.findall("XMAS", l))
        count += len(re.findall("SAMX", l))
        
    return count
def part1():
    count = 0#need 18 for test.txt
    count += searchHorizon(lines)#5
    count += searchVertical(lines)#3
    count += searchDiagnal(lines)#5
    # for i in reversed(range(5)):
        # print(i)
    # print(util.diagonalBackward(lines, 0,9))
    print(count)

#part 2
def part2():
    count = 0
    for r in range(1, len(lines)-1):
        for c in range(1,len(lines[r])-1):
            if lines[r][c] == 'A':
                if lines[r-1][c-1] == 'M' and lines[r+1][c+1] == 'S' and lines[r-1][c+1] == 'S' and lines[r+1][c-1] == 'M':
                    count += 1
                elif lines[r-1][c-1] == 'S' and lines[r+1][c+1] == 'M' and lines[r-1][c+1] == 'S' and lines[r+1][c-1] == 'M':
                    count += 1
                elif lines[r-1][c-1] == 'S' and lines[r+1][c+1] == 'M' and lines[r-1][c+1] == 'M' and lines[r+1][c-1] == 'S':
                    count += 1
                elif lines[r-1][c-1] == 'M' and lines[r+1][c+1] == 'S' and lines[r-1][c+1] == 'M' and lines[r+1][c-1] == 'S':
                    count += 1
    print(count)

part1()
part2()