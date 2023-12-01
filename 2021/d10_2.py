import util
from queue import LifoQueue

inputVal = util.parse('input10.txt')
#inputVal = util.parse('test.input')
#inputVal = ['{([(<{}[<>[]}>']

#score = {')': 3, ']':57, '}':1197,'>':25137}
score = {')': 1, ']':2, '}':3,'>':4}
#err = {'(': 0, '[':0, '{':0,'<':0}
err = {')': 0, ']':0, '}':0,'>':0}
need = {')': 0, ']':0, '}':0,'>':0}
m = {'(': [], '[':[], '{':[],'<':[]}
close = {')',']','}','>'}
op = {'(','[','{','<'}
pair1 = {'(':')', '[':']', '{':'}', '<':'>'}
pair = {')':'(', ']':'[', '}':'{', '>':'<'}
#s = LifoQueue()
s =[]

inComplete = []
for line in inputVal:
    isValid = True
    for c in line:
        if c in op:
            s.append(c)
        elif c in close:
            if s and s[-1] == pair[c]:
                s.pop()
            else:
                err[c] += 1
                isValid = False
                break
    if isValid:
        inComplete.append(line)

output = []
for line in inComplete:
    s = []
    for c in line:
        if c in op:
            s.append(c)
        elif c in close:
            if s and s[-1] == pair[c]:
                s.pop()
    sc = 0
    print(s)
    while s:
        c = s.pop()
        sc *= 5
        #print(pair[c])
        sc += score[pair1[c]]
    print(sc)
    output.append(sc)

output.sort()
print(output)
print(len(output)/2+1)
index = int((len(output)-1)/2)
print(output[index])
