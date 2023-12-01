import util
from queue import Queue

#inputVal = util.parse('input17.txt')
#inputVal = util.parse('test.txt')

#x=34..67, y=-215..-186
xT = range(34,68)
yT = range(-215,-185)
xT = range(20,31)
yT = range(-10,-4)
potentialX = set(xT) # steps that saturate x
sumX = 0
xInRange = False
for i in range(xT[-1]):
    sumX += i
    if sumX in xT:
        xInRange = True
        potentialX.add(i)
    else:
        if xInRange:
            break

potentialY = set(yT)
vY = yT[0]
maxY = 0
while vY < 1000:
    dy = vY
    y = 0
    tmp = 0
    while True:
        y += dy
        tmp = max(tmp,y)
        if y > yT[-1]:
            dy -= 1
        elif y < yT[0]:
            break
        else:
            potentialY.add(vY)
            maxY = max(maxY, tmp)
    vY += 1

print(potentialX)
print(potentialY)
print(maxY)
result = set()
for px in potentialX:
    for py in potentialY:
        valid = False
        while True:
            x = 0
            y = 0
            dx = px
            dy = py
            x += dx
            y += dy
            if x > xT[-1] or y < yT[0]:
                break
            elif x in xT and y in yT:
                valid = True
                break
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
        if valid:
            result.add((x,y))
print(len(result))
print(len(potentialX) * len(potentialY))
#vel = ()
#maxY = 0
#for s in step:
#    potentialX = step[0]
#    potentialY = step[0]
#    inRange = False
#    while True:
#        x = 0
#        y = 0
#        dx = potentialX
#        dy = potentialY
#        for i in range(potentialY):
#            x += dx
#            y += dy
#            if dx > 0:
#                dx -= 1
#            elif dx < 0:
#                dx += 1
#            dy -= 1
#        if x in xT:
#            inRange = True
#            maxY = max(y,maxY)
#        else:
#            if inRange:
#                break
#        potentialY += 1
#    vel=(potentialX,potentialY)
