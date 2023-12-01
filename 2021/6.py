numInc = 0
with open('input3.txt') as f:
    lines = f.readlines()
    print(len(lines))
    length = len(lines[0].strip('\n'))
    for i in range(0,length):
        count1= 0
        count0= 0
        list1 = set()
        list0 = set()
        if len(lines) == 1:
            print('O2 = %i' %(int(list(lines)[0],2)))
            break
        for line in lines:
            line = line.strip('\n')
            val = line[i]
            if val  == '1':
                count1 += 1
                list1.add(line)
            else:
                count0 += 1
                list0.add(line)

        if count1 < count0:
            lines = list1
        else:
            lines = list0


print('o2 = %s. dec=%i' %(list(lines)[0], int(list(lines)[0],2)))
