import util
lines = util.parse('d8.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))

def part1():
    count = 0
    map = dict()
    R = len(lines)
    C = len(lines[0])
    antinode = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] != ".":
                if lines[r][c] not in map:
                    map[lines[r][c]] = list()
                map[lines[r][c]].append((r,c))
    for k,v in map.items():
        # print("Processing ", k, ", ", v)
        for i in range(len(v)):
            for j in range(len(v)):
                if i == j:
                    continue
                d = (v[i][0]-v[j][0], v[i][1]-v[j][1])
                # print("distance bwt ", v[i], " and ", v[j], " = ", d)
                aLoc =  (v[i][0]+d[0], v[i][1]+d[1])
                if aLoc[0] >=0 and aLoc[0] < R and aLoc[1] >=0 and aLoc[1] < C:
                    antinode.add(aLoc)
                    # print(aLoc)
    # print(antinode)
    print(len(antinode))

#part 2
def part2():
    count = 0
    map = dict()
    R = len(lines)
    C = len(lines[0])
    antinode = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] != ".":
                if lines[r][c] not in map:
                    map[lines[r][c]] = list()
                map[lines[r][c]].append((r,c))
    for k,v in map.items():
        # print("Processing ", k, ", ", v)
        for i in range(len(v)):
            for j in range(len(v)):
                if i == j:
                    continue
                d = (v[i][0]-v[j][0], v[i][1]-v[j][1])
                # print("distance bwt ", v[i], " and ", v[j], " = ", d)
                cur = v[i]
                while cur[0] >=0 and cur[0] < R and cur[1] >=0 and cur[1] < C:
                    antinode.add(cur)
                    cur =  (cur[0]+d[0], cur[1]+d[1])
                    # print(aLoc)
    # print(antinode)
    print(len(antinode))

part1()
part2()