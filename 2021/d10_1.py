import util
from queue import LifoQueue

inputVal = util.parse('input10.txt')
#inputVal = util.parse('test.input')
#inputVal = ['{([(<{}[<>[]}>']

score = {')': 3, ']':57, '}':1197,'>':25137}
err = {'(': 0, '[':0, '{':0,'<':0}
err = {')': 0, ']':0, '}':0,'>':0}
m = {'(': [], '[':[], '{':[],'<':[]}
close = {')',']','}','>'}
op = {'(','[','{','<'}
pair = {'(':')', '[':']', '{':'}', '<':'>'}
pair = {')':'(', ']':'[', '}':'{', '>':'<'}
#s = LifoQueue()
s =[]
def checkError(c, openC, closeC):
    if c == openC:
        m[c].append(c)
    elif c == closeC:
         if m[openC]:
            m[openC].pop()
         else:
            err[openC] += 1

for line in inputVal:
    for c in line:
        if c in op:
            s.append(c)
        elif c in close:
            if s and s[-1] == pair[c]:
                s.pop()
            else:
                err[c] += 1
                break

print(err)
total = 0
for e in err:
    total += err[e] * score[e]

print(total)
