numInc = 0
with open('input2.txt') as f:
    lines = f.readlines()
    print(len(lines))
    forward=0
    depth=0
    aim=0
    for i in range(0,len(lines)):
        line = lines[i].split()
        val = int(line[1].strip('\n'))
        if line[0] == 'down':
            aim += val
        elif line[0] == 'up':
            aim -= val
        else:
            forward += val
            depth += aim * val

print('x= %i, y= %i. position= %i' %(forward, depth, forward*depth))

