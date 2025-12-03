import util
lines = util.parse('d2.txt')

def countInvalid(start,end):
    sum = 0
    for i in range(start,end+1):
        s = str(i)
        if len(s) % 2 > 0:
            continue
        mid = int(len(s)/2)
        firstHalf = s[:mid]
        secondHalf = s[mid:]
        if firstHalf == secondHalf:
            sum += i
    return sum

def part1():
    count = 0
    for l in lines:
        ranges = l.split(',')
        for r in ranges:
            (start,end) = r.split('-')
            count += countInvalid(int(start),int(end))

    print(count)

#part 2

# split from 2->n where n is size of array
def countInvalid2(start,end):
    sum = 0
    for i in range(start,end+1):
        s = str(i)
        size = len(s)
        splitIndex = size/2
        # print('processing',i, 'num len', size, 'with init index', splitIndex)
        while splitIndex >= 1:
            splitIndex = int(splitIndex)
            while size % splitIndex != 0:
                splitIndex -= 1
            checkDup = set()
            prevIndex = 0
            # print('  checking partial size', splitIndex)
            for j in range(splitIndex,size+1,splitIndex):
                # print('    checking', s[prevIndex:j])
                checkDup.add(s[prevIndex:j])
                prevIndex = j
            if len(checkDup) == 1:
                # print('invalid ID:',i)
                sum += i
                break
            splitIndex -= 1
    return sum

def part2():
    count = 0
    for l in lines:
        ranges = l.split(',')
        for r in ranges:
            (start,end) = r.split('-')
            count += countInvalid2(int(start),int(end))

    print(count)

#part1()
part2()
#2548308401678360 too high