import util

inputVal = util.parse('input7.txt')
#inputVal = util.parse('test.input')
#inputVal = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
# inputVal = ['cfadeg ca bacg dfabe dgcbf dbegafc dac afbdgc gcbedf bfcda | fbdac adbef bgcdfae dcagfe']

total = 0
digits = {}
s = {}


# Python3 program to Split string into characters
def split(word):
    return [char for char in word]


def sort(word):
    chars = split(word)
    chars.sort()
    out = ''
    for c in chars:
        out += c
    return out


def decode(code):
    cd = sort(code)
    for i in digits:
        # print('%s == %s?' %(digits[i],cd))
        if digits[i] == cd:
            return i


def findCommon(l):
    m = {}
    for j in l:
        for i in j:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
    common = ('z', 0)
    for i in m:
        if m[i] > common[1]:
            common = (i, m[i])
    return common[0]


def diff(s1, s2):
    diff = set()
    for c in s1:
        if c not in s2:
            diff.add(c)
    for c in s2:
        if c not in s1:
            diff.add(c)
    return list(diff)


def sub(s1, s2):
    sb = set()
    for c in s1:
        if c not in s2:
            sb.add(c)
    return list(sb)


count = 1
for line in inputVal:
    right = line.split('|')[1]
    left = line.split('|')[0]
    both = right + ' ' + left
    digit = both.split()
    # print(digit)
    fives = set()
    sixs = set()
    for d in digit:
        if len(d) == 2:
            digits['1'] = d
        elif len(d) == 3:
            digits['7'] = d
        elif len(d) == 4:
            digits['4'] = d
        elif len(d) == 5:
            fives.add(sort(d))
        elif len(d) == 6:
            sixs.add(sort(d))
        elif len(d) == 7:
            digits['8'] = d
    # print('1:%s 4:%s 7:%s 8:%s' %(one,4,7,8))
    s[1] = diff(digits['1'], digits['7'])[0]
    # print('seg1: %s' %s[1])
    tmp = digits['4'] + s[1]
    tList = []
    fives = list(fives)
    tList.append(diff(tmp, fives[0]))
    tList.append(diff(tmp, fives[1]))
    tList.append(diff(tmp, fives[2]))
    s[7] = findCommon(tList)
    # print('seg7: %s' %s[7])
    tList = list(fives)
    tList.append(digits['4'])
    s[4] = findCommon(tList)
    # print('seg4: %s' %s[4])
    s[2] = sub(digits['4'], digits['1'] + s[4])[0]
    # print('seg2: %s' %s[2])
    tList = list(sixs)
    tList.append(digits['1'])
    s[6] = findCommon(tList)
    # print('seg6: %s' %s[6])
    s[3] = sub(digits['1'], s[6])[0]
    # print('seg3: %s' %s[3])
    s[5] = sub(digits['8'], digits['4'] + s[1] + s[7])[0]
    # print('seg5: %s' %s[5])

    digits['2'] = s[1] + s[3] + s[4] + s[5] + s[7]
    digits['3'] = s[1] + s[3] + s[4] + s[6] + s[7]
    digits['5'] = s[1] + s[2] + s[4] + s[6] + s[7]
    digits['0'] = s[1] + s[2] + s[3] + s[5] + s[6] + s[7]
    digits['6'] = s[1] + s[2] + s[4] + s[5] + s[6] + s[7]
    digits['9'] = s[1] + s[2] + s[3] + s[4] + s[6] + s[7]
    # print(digits)
    # print(right.split())
    for i in digits:
        digits[i] = sort(digits[i])
    output = ''
    for i in right.split():
        output += decode(i)
    print('line %i: %s' % (count, output))
    total += int(output)
    count += 1

print(total)
