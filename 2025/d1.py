import util
lines = util.parse('d1.txt')


def rotate(start, direction, turns):
    end = start
    count = 0
    if direction == 'L':
        end = start - turns
        if start != 0 and turns >= start: #second condition already count 0. so exclude if starting at 0
            count += 1
    else:
        end = start + turns
        if start != 0 and turns >= (100-start):
            count += 1
    while end < 0:
        end += 100
    while end > 99:
        end -= 100
    return (end, count)

def part1():
    num = 50
    count = 0
    for l in lines:
        direction = l[0]
        turns = int(l[1:])
        res = rotate(num, direction, turns)
        num = res[0]
        if num == 0:
            count += 1
    print(count)

#part 2
def part2():
    num = 50
    count = 0
    for l in lines:
        direction = l[0]
        turns = int(l[1:])
        loop = int(turns / 100)
        count += loop
        turns = turns % 100
        prev = num
        res = rotate(num, direction, turns)
        num = res[0]
        count += res[1]
        # print('Rotating from', prev, '# turn:', direction, turns, 'to', res[0], 'count:', count)
    print(count)

part1()
part2()
#5789 too lower
#5984 too high