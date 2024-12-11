import util
import time
lines = util.parse('d11.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
seen = dict()
blinks = 75
def main2(): # too long to do insert. even longer than main()
    stones = lines[0].split(' ')
    stones = [int(x) for x in stones]
    for blink in range(25):
        i = 0
        while i < len(stones):
            s = stones[i]
            if s == 0:
                stones[i] = 1
            elif len(str(s)) % 2 == 0:
                ss = str(s)
                mid = int(len(ss) / 2)
                stones[i] = int(ss[:mid])
                stones.insert(i+1,int(ss[mid:]))
                i += 1
                #print("ss: ",ss, "s: ", s, "mid: ", mid)
                #print("ss[:mid]: ",ss[:mid], "ss[mid:]: ", ss[mid:])
            else:
                stones[i] = stones[i] * 2024
            i += 1
    #print(stones)
    print(len(stones))
def main3():
    count = 0
    stones = lines[0].split(' ')
    stones = [int(x) for x in stones]
    for s in stones:
        count += recurse(s,blinks)
    print(count)
def recurse(s, blink):
    if blink == 0:
        return 1
    count = 0
    if (s,blink) in seen:
        return seen[(s,blink)]
    if s == 0:
        count += recurse(1,blink-1)
    elif len(str(s)) % 2 == 0:
        ss = str(s)
        mid = int(len(ss) / 2)
        count += recurse(int(ss[:mid]), blink-1)
        count += recurse(int(ss[mid:]), blink-1)
    else:
        count += recurse(s*2024,blink-1)
    seen[(s,blink)] = count
    return count
def main(): #does not work for part 2. take too long
    stones = lines[0].split(' ')
    stones = [int(x) for x in stones]
    seen = dict()
    for blink in range(blinks):
        tmp = list()
        for s in stones:
            if s == 0:
                tmp.append(1)
            elif len(str(s)) % 2 == 0:
                ss = str(s)
                mid = int(len(ss) / 2)
                #print("ss: ",ss, "s: ", s, "mid: ", mid)
                #print("ss[:mid]: ",ss[:mid], "ss[mid:]: ", ss[mid:])
                tmp.append(int(ss[:mid]))
                tmp.append(int(ss[mid:]))
            else:
                if s in seen:
                    tmp.append(seen[s])
                else:
                    val = s*2024
                    tmp.append(val)
                    seen[s] = val
        stones = tmp

    #print(stones)
    print(len(stones))

start = time.time()
#main()
stop = time.time()
print("Main run in: ", stop-start, "seconds")
start = time.time()
main3()
stop = time.time()
print("Main2 run in: ", stop-start, "seconds")
