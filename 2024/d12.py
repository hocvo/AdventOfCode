import util
import time
lines = util.parse('d12.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
regions = list()
def main():
    fence = 0
    R = len(lines)
    C = len(lines[0])
    seen = set()
    for r in range(R):
        for c in range(C):
            if (r,c) in seen:
                continue
            #print("First time seeing:", lines[r][c], "at", r,c)
            reg = list()
            q = list()
            q.append((r,c))
            area = 0
            peri = 0
            while q:
                #print(q)
                (i,j) = q.pop(0)
                if (i,j) in seen:
                    continue
                reg.append((i,j))
                area += 1
                adj = 0
                for (x,y) in util.neighborsCrossIndex(lines,i,j):
                    if lines[i][j] == lines[x][y]:
                        if (x,y) in seen:
                            adj += 1
                        else:
                            q.append((x,y))
                peri = peri + 4 - (2*adj)
                #print(adj,peri)
                seen.add((i,j))
            seen.add((r,c))
            regions.append(reg)
            fence += area * peri
            #print(area,peri,fence)
    print(fence)

def getMinMaxList(colList):
    colSepList = list()
    colList.sort()
    start = 0
    i = 0
    for i in range(1,len(colList)):
        if colList[i] - colList[i-1] > 1:
            colSepList.append(colList[start:i])
            start = i
    colSepList.append(colList[start:i+1])
    minMaxList = list()
    for cols in colSepList:
        minC = min(cols)
        maxC = max(cols)
        minMaxList.append((minC,maxC))
    return minMaxList
def part2():
    fence = 0
    for reg in regions:
        area = len(reg)
        peri = 0
        reg.sort(key = lambda t: t[0])
        # print(reg)
        regByRow = list()
        start = 0
        i = 0
        for i in range(1,len(reg)):        
            #min = min(min, int(reg[i][1]))
            #max = max(max, int(reg[i][1]))
            if reg[i-1][0] != reg[i][0]:
                subR = reg[start:i]
                # print("SubR:",subR)
                colList= [x[1] for x in subR]
                # print("ColList:",subR)
                regByRow.append(getMinMaxList(colList))
                start = i
        #process last portion
        subR = reg[start:i+1]
        # print("SubR:",subR)
        colList= [x[1] for x in subR]
        # print("ColList:",subR)
        regByRow.append(getMinMaxList(colList))
        # print("regByRow:", regByRow)

        prevMin = set()
        prevMax = set()
        for mmList in regByRow:
            newPrevMin = set()
            newPrevMax = set()
            for (minC,maxC) in mmList:
                # print("minC, maxC, prevMin, prevMax", minC, maxC, prevMin, prevMax)
                if minC not in prevMin:
                    peri += 2
                if maxC not in prevMax:
                    peri += 2
                newPrevMin.add(minC)
                newPrevMax.add(maxC)
            prevMin = newPrevMin
            prevMax = newPrevMax

        fence += area * peri
        # print ("area, peri, fence:", area, peri, area * peri)
    print(fence)    
    
start = time.time()
main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")
    
part2()
