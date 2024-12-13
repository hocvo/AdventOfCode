import util
import time
import re
lines = util.parse('d13.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
Xpattern = 'X[\+=](\d*)'
Ypattern = 'Y[\+=](\d*)'
pressNum = 100
def main():
    totalMoney = 0
    machines = util.splitOnElement(lines, "")
    for m in machines:
        a = (int(re.search(Xpattern,m[0]).group(1)), int(re.search(Ypattern,m[0]).group(1)))
        b = (int(re.search(Xpattern,m[1]).group(1)), int(re.search(Ypattern,m[1]).group(1)))
        p = (int(re.search(Xpattern,m[2]).group(1)), int(re.search(Ypattern,m[2]).group(1)))
        print("Running:",a,b,p)
        possible = list()
        recurse(a,b,p,(0,0),0,dict(),possible)
        if possible:
            totalMoney += min(possible)

    print(totalMoney)
def recurse(a,b,p, press, money, seen, possible):
    #print(p,press)
    if press[0] > pressNum and press[1] > pressNum:
        return False
    if p[0] < 0 or p[1] < 0:
        return False
    if p[0] == 0 and p[1] == 0:
        possible.append(money)
        return True
    #press b
    bpress = (press[0],press[1]+1)
    if bpress in seen:
        if seen[bpress]:
            possible.append(money+1)
            return seen[bpress]
    if bpress not in seen and press[1] < pressNum and recurse(a,b, (p[0]-b[0],p[1]-b[1]), bpress, money+1, seen,possible):
        seen[bpress] = True
        return True
    #press a
    apress = (press[0]+1,press[1])
    if apress in seen:
        if seen[apress]:
            possible.append(money+3)
            return seen[apress]
    if apress not in seen and press[0] < pressNum and recurse(a,b, (p[0]-a[0],p[1]-a[1]), apress, money+3, seen,possible):
        seen[apress] = True
        return True
    seen[press] = False
    return False


start = time.time()
main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")
