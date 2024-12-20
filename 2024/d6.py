import util
lines = util.parse('d6.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
guardPos = ["^",">","v","<"]
moves = [(-1,0),(0,1),(1,0),(0,-1)]
R = len(lines)
C = len(lines[0])
def part1():
    count = 0
    start = tuple()
    found = False
    steps = set()
    for r in range(R):
        for c in range(C):
            if lines[r][c] in guardPos:
                start = (r,c)
                found = True
                break
        if found:
            break
    cur = start
    face = lines[start[0]][start[1]]
    # nextMove = tuple(map(sum, zip(start, moves[guardPos.index(face)])))
    # print(cur)
    # print(nextMove)
    while cur[0] >= 0 and cur[0] < R and cur[1] >= 0 and cur[1] < C:
    # for i in range(5):
        # print(cur)
        # print("adding ", cur)
        steps.add(cur)
        m = moves[guardPos.index(face)]
        nextMove = (cur[0]+m[0],cur[1]+m[1])
        if nextMove[0] >= 0 and nextMove[0] < R and nextMove[1] >= 0 and nextMove[1] < C and lines[nextMove[0]][nextMove[1]] == "#": #need to turn
            face = guardPos[(guardPos.index(face) + 1) % 4]
            # print ("hit wall :", nextMove, " turn to ", face)
        else:
            # print(nextMove)
            cur = nextMove
    print(len(steps))

def part2():
    count = 0
    start = tuple()
    found = False
    for r in range(R):
        for c in range(C):
            if lines[r][c] in guardPos:
                start = (r,c,lines[r][c])
                found = True
                break
        if found:
            break
    for r in range(R):
        for c in range(C):            
            cur = start
            face = lines[start[0]][start[1]]
            steps = set()
            while cur[0] >= 0 and cur[0] < R and cur[1] >= 0 and cur[1] < C:
                if cur in steps:
                    count += 1
                    print("found loop at: ", cur, "count=",count)
                    break
                # print("adding ", cur)
                steps.add(cur)
                m = moves[guardPos.index(face)]
                nextMove = (cur[0]+m[0],cur[1]+m[1],face)
                nm = (cur[0]+m[0],cur[1]+m[1])
                if nextMove[0] >= 0 and nextMove[0] < R and nextMove[1] >= 0 and nextMove[1] < C and (lines[nextMove[0]][nextMove[1]] == "#" or nm == (r,c)): #need to turn
                    # print("hit wall :", nextMove)
                    face = guardPos[(guardPos.index(face) + 1) % 4]
                    # steps.add((cur[0],cur[1],face))
                    # print("adding ", (cur[0],cur[1],face))
                    cur = (cur[0],cur[1],face)
                    # print ("hit wall :", nextMove, " turn to ", face)
                    # print ("turn to ", face)
                else:
                    # print(nextMove)
                    cur = nextMove
    print(count)

part1()
part2()