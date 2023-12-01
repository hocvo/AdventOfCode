numInc = 0
with open('input1.txt') as f:
    lines = f.readlines()
    print(len(lines))
    for i in range(1,len(lines)):
        prev = int(lines[i-1].strip('\n'))
        cur = int(lines[i].strip('\n'))
        if cur > prev:
            numInc += 1

print(numInc)

