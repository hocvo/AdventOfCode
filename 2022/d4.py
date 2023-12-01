import util
lines = util.parse('input4.txt')
total = 0
for l in lines:
    pair = l.split(',')
    firstElf = pair[0].split('-')
    secondElf = pair[1].split('-')
    firstElf[0]= int(firstElf[0])
    firstElf[1]= int(firstElf[1])
    secondElf[0]= int(secondElf[0])
    secondElf[1]= int(secondElf[1])
    #print (firstElf, secondElf)
    if firstElf[0] >= secondElf[0] and firstElf[1] <= secondElf[1]:
        total += 1
        continue
    if secondElf[0] >= firstElf[0] and secondElf[1] <= firstElf[1]:
        total += 1
        continue
print(total)
total = 0
#Part 2
for l in lines:
    pair = l.split(',')
    firstElf = pair[0].split('-')
    secondElf = pair[1].split('-')
    firstElf[0]= int(firstElf[0])
    firstElf[1]= int(firstElf[1])
    secondElf[0]= int(secondElf[0])
    secondElf[1]= int(secondElf[1])
    #print (firstElf, secondElf)
    if firstElf[0] >= secondElf[0] and firstElf[0] <= secondElf[1]:
        total += 1
        continue
    if firstElf[1] >= secondElf[0] and firstElf[1] <= secondElf[1]:
        total += 1
        continue
    if secondElf[0] >= firstElf[0] and secondElf[0] <= firstElf[1]:
        total += 1
        continue
    if secondElf[1] >= firstElf[0] and secondElf[1] <= firstElf[1]:
        continue
print(total)
