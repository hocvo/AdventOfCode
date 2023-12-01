import util
inputVal = util.parse('input5.txt')
#inputVal = util.parse('test.input')

m=[]
maxX = 0
maxY = 0
for l in inputVal:
    coors = l.split('->')
    src = coors[0].split(',')
    dst = coors[1].split(',')
    maxX=max(int(src[0]),int(dst[0]),maxX)
    maxY=max(int(src[1]),int(dst[1]),maxY)

maxY +=1
maxX +=1
for i in range(0, maxX+1):
    row = []
    for j in range(0,maxY+1):
        row.append(0)
    m.append(row)
print('X=%i, Y=%i' %(maxX, maxY))
for l in inputVal:
    coors = l.split('->')
    src = coors[0].split(',')
    srcX = int(src[0])
    srcY = int(src[1])
    dst = coors[1].split(',')
    dstX= int(dst[0])
    dstY = int(dst[1])
    if dstX-srcX ==0:
        slope = 0
    else:
        slope = (dstY-srcY)/(dstX-srcX)
    #print(l)
    #print('sX=%i sY=%i dX=%i dY=%i' %(srcX, srcY, dstX, dstY))
    if srcX == dstX:
        lower=min(srcY,dstY)
        upper=max(srcY,dstY)+1
        for i in range(lower,upper):
            #print('%i %i' %(i, srcX))
            #m[srcX][i] += 1
            m[i][srcX] += 1
    elif srcY == dstY:
        lower=min(srcX,dstX)
        upper=max(srcX,dstX)+1
        for i in range(lower,upper):
            m[srcY][i] += 1
            #m[i][srcY] += 1
    if slope == 1 or slope == -1:
        if srcX==srcY and dstX==dstY:
            lower=min(srcX,dstX)
            upper=max(srcX,dstX)+1
            #print(l)
            #print('lower=%i upper=%i' %(lower, upper))
            for i in range(lower,upper):
                m[i][i] += 1
        else: #srcX == dstY and srcY == dstX:
            if dstX < srcX:
                stepX = -1
            else:
                stepX = 1
            if dstY < srcY:
                stepY = -1
            else:
                stepY = 1
            #print(l)
            j = srcY
            for i in range(srcX,dstX+stepX,stepX):
                #print('i=%i j=%i' %(i, j))
                m[j][i] += 1
                j += stepY
    #print(m)

count = 0
for r in m:
    for c in r:
        if c > 1:
            count += 1

print(count)
count2 = 0
for i in range(0,maxX):
    for j in range(0,maxY):
        if m[i][j] > 1:
            count2 += 1
print(count2)
#print(m)
#util.printObj(m)
