import util
lines = util.parse('d5.txt')
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
    count2 = 0
    notOrdered = list()
    ruleAndPage = util.splitOnElement(lines, "")
    rules = dict()
    for r in ruleAndPage[0]:
        rule = r.split("|")
        if rule[0] not in rules:
            rules[rule[0]] = set()        
        rules[rule[0]].add(rule[1])
    # print(ruleAndPage[1])
    for page in ruleAndPage[1]:
        pages = page.split(",")
        isOrdered = True
        for i in range(1,len(pages)):
            if pages[i] not in rules:
                continue
            curPage = pages[i]
            # print("processing curPage", curPage)
            # print("rules curPage", rules[curPage])
            for j in range(0,i):
                # print("checking page[j]", pages[j])
                if pages[j] in rules[curPage]:
                    isOrdered = False
                    break
            if not isOrdered:
                break
        if isOrdered:
            # print("ordered: ", pages)
            mid = int(len(pages)/2)
            count += int(pages[mid])
        else:
            # print("send ", pages," to part 2")
            count2 += part2(pages, rules)
    print(count)
    print(count2)

#part 2
def part2(pages, rules):
    count = 0
    newPages = list()
    i = len(pages)-1
    while True:
        if i == 0:
            break
        curPage = pages[i]
        for j in range(i):
            # print("checking page[j]", pages[j])
            if curPage in rules and pages[j] in rules[curPage]:
                pages[i], pages[j] = pages[j], pages[i] 
                i = len(pages) # recheck everything
                break
        i -= 1
    mid = int(len(pages)/2)
    return int(pages[mid])

part1()