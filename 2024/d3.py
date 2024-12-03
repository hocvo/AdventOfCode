import util
import re
lines = util.parse('d3.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))

test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
pattern = "mul\(([0-9]{1,3}),([0-9]{1,3})\)"
def part1():
    count = 0
    
    # x = re.findall(pattern,test)
    # print(x[0][0])
    # x2 = re.search(pattern, x[0])
    # print(x2)
    # print(x2.group(0))
    # print(x2.group(1))
    for l in lines:
        multList = re.findall(pattern,l)
        # print(multList)
        for mult in multList:
            count += int(mult[0]) * int(mult[1])
    print(count)

#part 2
def part2():
    count = 0
     # need to joins all instructions since don't from prev line would not process the first part of current line
    l = ''.join(lines)
    doSplit = l.split("do()")
    for do in doSplit:
        dodont = do.split("don't()")
        multList = re.findall(pattern, dodont[0])
        for mult in multList:
            count += int(mult[0]) * int(mult[1])
    print(count)

part1()
part2()
