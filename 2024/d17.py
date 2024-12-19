import util
import time
import re
import random
lines = util.parse('d17.txt')
#lines = util.parse('test.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))

A = 0
B = 0
C = 0
INS = ['adv','bxl','bst','jnz','out','bdv','cdv']
def main():
    global A,B,C
    output = ''
    inp = util.splitOnElement(lines, "")
    regs = inp[0]
    A = int(regs[0].split(': ')[1])
    B = int(regs[1].split(': ')[1])
    C = int(regs[2].split(': ')[1])
    prog = inp[1][0].split(': ')[1].split(',')
    prog = [int(x) for x in prog]
    print("A,B,C",A,B,C)
    print(prog)

    # Test
    # A = 2024
    # prog = [0,1,5,4,3,0]
    expectedOutput = inp[1][0].split(': ')[1]
    j = 10000000000000
    A = j
    while True:
        A = j
        i = 0
        output = []
        while i >= 0 and i+1 < len(prog):
            ins = prog[i]
            operand = prog[i+1]
            curI = i
            # print("PRocessing", ins,operand)
            i = op(ins, operand, curI, output)
            if i == curI:
                i += 2
        testOutput = [str(x) for x in output]
        testOutput = ','.join(testOutput)
        if testOutput == expectedOutput:
            print("Found A", j)
            break
        print("A",j,"Output:",testOutput)
        j += 1
    print(output)
def op(ins, operand, i, output):
    global A,B,C
    if ins == 0:
        A = int(A/pow(2,combo(operand)))
    elif ins == 1:
        B = B ^ operand
    elif ins == 2:
        B = combo(operand) % 8
    elif ins == 3:
        if A == 0:
            return i
        else:
            return operand
    elif ins == 4:
        B = B ^ C
    elif ins == 5:
        output.append(combo(operand)%8)
    elif ins == 6:
        B = int(A/pow(2,combo(operand)))
    elif ins == 7:
        C = int(A/pow(2,combo(operand)))
    return i
        
def combo(operand):
    if operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6: 
        return C
    elif operand == 7:
        #not implemented
        return 0
    else:
        return int(operand)
start = time.time()
main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")