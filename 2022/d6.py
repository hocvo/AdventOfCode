import util
lines = util.parse('input6.txt')
l = lines[0]

for i in range(0,len(l)-4):
    s = set()
    for j in range(14):
        s.add(l[i+j])
    #print(s)
    if len(s) == 14:
        print(i+j)
        break
