import util
from queue import Queue

inputVal = util.parse('input16.txt')
#inputVal = util.parse('test.txt')
#inputVal = 'D2FE28'
#inputVal = '38006F45291200'
#inputVal = 'EE00D40C823060'
#inputVal = ['C0015000016115A2E0802F182340']
#print(inputVal)

vlen = 3
tlen = 3
labelSize = 5
sumVersion = 0
def parse(s, labelList, start, stop=-1, numPkg=-1):
    global sumVersion
    #print(s)
    i = start
    labelProcessing = False
    label = ''
    #labelList = []
    pkgCount = 0
    while i < len(s):
        if stop > 0 and i >= stop:
            break
        if labelProcessing:
            if s[i] == '0':
                labelProcessing = False
            labelPart = s[i+1:i+labelSize]
            i += labelSize
            label += labelPart
            #print(label)
            if not labelProcessing:
                labelInt = int(label,2)
                labelList.append(labelInt)
                label =''
            #print('label: %s' %label)
            continue

        if pkgCount == numPkg:
            break
        #if i%4 > 0: # always start at a new Hex
        #    i += 1
        #    continue
        version = int(s[i:i+vlen],2)
        i += vlen
        sumVersion += version
        #print('version: %i' %version)
        #print(i)
        typeID = int(s[i:i+tlen],2)
        i += tlen
        #print('typeID: %i' %typeID)
        #print(i)
        if typeID == 4:
            labelProcessing = True
        else:
            lenTypeID = int(s[i],2)
            i+= 1
            print('Len ID Type: %i' %lenTypeID)
            labelListTmp = []
            if lenTypeID == 0:
                pkglen = int(s[i:i+15],2)
                #print('next len: %i' %pkglen)
                i+= 15
                #labelList += parse(s[i:i+pkglen])
                i = parse(s,labelListTmp,i,i+pkglen)
                #i += pkglen
                #break
            elif lenTypeID == 1:
                numPkgTmp = int(s[i:i+11],2)
                i+= 11
                #print('Num pkg: %i' %numPkgTmp)
                #labelList += parse(s[i:-1],numPkg)
                for n in range(numPkgTmp):
                    i = parse(s,labelListTmp,i,-1,1)
                #break
            if typeID == 0:
                labelList.append(sum(labelListTmp))
            elif typeID == 1:
                prod = 1
                for n in labelListTmp:
                    prod *= n
                labelList.append(prod)
            elif typeID == 2:
                labelList.append(min(labelListTmp))
            elif typeID == 3:
                labelList.append(max(labelListTmp))
            elif typeID == 5:
                if labelListTmp[0] > labelListTmp[1]:
                    labelList.append(1)
                else:
                    labelList.append(0)
            elif typeID == 6:
                if labelListTmp[0] < labelListTmp[1]:
                    labelList.append(1)
                else:
                    labelList.append(0)
            elif typeID == 7:
                if labelListTmp[0] == labelListTmp[1]:
                    labelList.append(1)
                else:
                    labelList.append(0)

        pkgCount += 1

    if stop > 0:
        i = stop
    return i
#def parseLabel(s, i)
for l in inputVal:
    sumVersion = 0
    l = bin(int('1'+l, 16))[3:]
    labelList = []
    label = parse(l,labelList,0,-1,1)
    print(labelList)
    #print(sumVersion)

