import util
import time
lines = util.parse('d3.txt')

def dfs(jolts, toggles):
    if len(jolts) == toggles:
        return sum(10 ** (toggles - i - 1) * x for i, x in enumerate(jolts))
    if toggles == 1:
        return max(jolts)
    (n,idx) = (-1,0)
    
    # find highest number in jolts but exclude some at the end for the rest of the toggles
    # this is equivalent to the for loop below but have to switch idx to (-) in the return
    # n, idx = max((x , -i) for (i, x) in enumerate(jolts[:-(toggles-1)]))
    for i, x in enumerate(jolts[:-toggles+1]):
        if x > n:
            n = x
            idx = i
    return n * 10**(toggles-1) + dfs(jolts[idx+1:],toggles-1)

def part1():
    count = 0
    start = time.time()
    for l in lines:
        jolts = [int(i) for i in l.strip()]
        count += dfs(jolts,2)
    stop = time.time()
    print(count)
    print(stop-start)

def part2():
    count = 0
    start = time.time()
    for l in lines:
        jolts = [int(i) for i in l.strip()]
        count += dfs(jolts,12)
    stop = time.time()
    print(count)
    print(stop-start)

part1()
part2()
#166574147671929
#167997792771560 too low