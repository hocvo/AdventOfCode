import util
lines = util.parse('d1.txt')
def part1():
    count = 0
    l1 = list()
    l2 = list()
    for l in lines:
        p = l.split()
        l1.append(int(p[0].strip()))
        l2.append(int(p[1].strip()))
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        diff = abs(l1[i] - l2[i])
        count = count + diff
    print(count)

#part 2
def part2():
    count = 0
    l1 = list()
    map = dict()
    for l in lines:
        p = l.split()
        l1.append(int(p[0].strip()))
        r = int(p[1].strip())
        if r in map:
            map[r] = map[r] + 1
        else:
            map[r] = 1
    #print(map)
    #print(list)
    for i in range(len(l1)):
        if l1[i] in map:
            similarity = l1[i] * map[l1[i]]
            count = count + similarity
    print(count)

part1()
part2()