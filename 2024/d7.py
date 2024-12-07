import util
lines = util.parse('d7.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
result = 0
count = 0
isDone = False
def part1():
    global result, isDone
    count = 0
    for l in lines:
        isDone = False
        e = l.split(": ")
        result = int(e[0])
        values = e[1].split(" ")
        # print("testing for ", result)
        recurse(int(values[0]), values, 1)
    print(count)

def evaluate(a,b,op):
    if op == "*":
        # print(a,"*",b)
        return int(a)* int(b)
    elif op == "+":
        # print(a,"+",b)
        return int(a) + int(b)
    elif op == "||": # part 2
        return int(str(a)+str(b))
    return 0

def recurse(cur, values, i):
    global count, isDone
    if isDone:
        return 0
    if i == len(values):
        # print("returning ", cur)
        return cur
    # print(result)
    if recurse(evaluate(cur, values[i], "+"), values, i+1) == result or recurse(evaluate(cur, values[i], "*"), values, i+1) == result or recurse(evaluate(cur, values[i], "||"), values, i+1) == result:
        # print("add count ", result)
        count += result
        isDone = True
        return
    # print("returning last", cur)
    return 0
        
#part 2
def part2():
    print(count)

part1()
part2()