import util
lines = util.parse('input1.txt')
maxCal = 0
cal = 0
calList = list()
for l in lines:
    if not l:
        maxCal = max(cal, maxCal)
        calList.append(cal)
        cal = 0
    else:
        cal += int(l)

print(maxCal)
calList.sort()
cal = calList[-1] + calList[-2] + calList[-3]
print(cal)
