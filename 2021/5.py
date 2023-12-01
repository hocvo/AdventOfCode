numInc = 0
with open('input3.txt') as f:
    lines = f.readlines()
    print(len(lines))
    gamma = ''
    countMap= {}
    length = len(lines[0].strip('\n'))
    total = ''
    for i in range(0,length):
        total += '1'
        count1= 0
        count0= 0
        for j in range(0,len(lines)):
            line = lines[j].strip('\n')
            val = line[i]
            if val  == '1':
                count1 += 1
            else:
                count0 += 1

        if count1 >= count0:
            gamma += '1'
        else:
            gamma += '0'

    total = int(total, 2)
    gamma = int(gamma, 2)
    eps = total - gamma

print('gamma= %i, eps= %i. power= %i' %(gamma, eps, eps*gamma))

