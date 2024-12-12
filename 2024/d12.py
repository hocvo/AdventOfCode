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
            q = list()
            #region = set()
            q.append((r,c))
            area = 0
            peri = 0
            while q:
                #print(q)
                (i,j) = q.pop(0)
                if (i,j) in seen:
                    continue
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
            fence += area * peri
            #print(area,peri,fence)
    print(fence)
start = time.time()
main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")
