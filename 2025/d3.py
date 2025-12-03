import util
import time
lines = util.parse('test.txt')

def part1():
    num = 50
    count = 0
    for l in lines:
        firstI = 0
        secondI = 0
        max1 = 0
        for i in range(0,len(l)-1):
            num = int(l[i])
            # print(num)
            if num > max1:
                max1 = num
                firstI = i
                # firstI = secondI
                # secondI = i
        max1 = 0
        for i in range(firstI+1,len(l)):
            if i == firstI:
                continue
            num = int(l[i])
            if num > max1:
                max1 = num
                secondI = i
        # print('first:', l[firstI], 'second:', l[secondI])
        # if firstI > secondI:
            # joltage = int(l[secondI])*10 + int(l[firstI])
        # else:
        joltage = int(l[firstI])*10 + int(l[secondI])
        
        count += joltage
    print(count)

#part 2
def dfs(s,i,res, processed):
    if len(res) == 12 or i >= len(s):
        return int(res)
    joltage = 0
    if (i,res) in processed:
        return processed[(i,res)]
    for j in range(i,len(s)):
        joltage = max(joltage, dfs(s,j+1,res+s[i],processed))
    # if i in processed and processed[i] < joltage:
    processed[(i,res)] = joltage
    # print('done processing(',i,',',res,'):', joltage)
    return joltage
    # return max(dfs(s,i+1,res+s[i],processed), dfs(s,i+2,res+s[i],processed))
    
# def bfs(s, i, res):
    

def part2():
    num = 50
    count = 0
    start = time.time()
    for l in lines:
        joltage = 0
        processed = {}
        for i in range(0,len(l)-12):
            joltage = max(joltage, dfs(l,i, '', processed))
            # processed[i]=joltage
        # joltage = max(joltage, dfs(l,3, l[2]))
        print(joltage)
        count += joltage
    stop = time.time()
    print(count)
    print(stop-start)

def part3():
    count = 0
    for l in lines:
        for c in l:
            num=int(c)

# part1()
part2()
#166574147671929
#167997792771560 too low