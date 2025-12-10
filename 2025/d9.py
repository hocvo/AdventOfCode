import util
import time
# import matplotlib.pyplot as plt
# import numpy as np
lines = util.parse('d9.txt')

def area(xy, i, j):
    x1,y1 = xy[i]
    x2,y2 = xy[j]
    return (abs(x1-x2)+1) * (abs(y1-y2)+1)

def part1():
    xy = []
    max_area = 0
    for line in lines:
        x,y = line.split(',')
        x,y = int(x),int(y)
        xy.append((x,y))
    for i in range(len(xy)):
        for j in range(i+1,len(xy)):
            max_area = max(max_area, area(xy,i,j))
    print(max_area)

def is_covered(testx, testy,xy):
    return util.pointInPolygon2D(testx, testy,xy)
        
def check_green(xy, x1,y1,x2,y2):
    if x1 == x2 or y1 == y2:
        return True
    # points to find
    x,y = x1,y2
    xx,yy = x2,y1
    return is_covered(x,y,xy) & is_covered(xx,yy,xy)

def area2(xy, i, j):
    x1,y1 = xy[i]
    x2,y2 = xy[j]
    if check_green(xy,x1,y1,x2,y2):
        return (abs(x1-x2)+1) * (abs(y1-y2)+1)
    return 0

def part2():
    xy = []
    max_area = 0
    for line in lines:
        x,y = line.split(',')
        x,y = int(x),int(y)
        xy.append((x,y))

    # max_x = max(xy, key=lambda x: x[0])
    # max_y = max(xy, key=lambda x: x[1])
    # fig, ax = plt.subplots()
    # ax.scatter([x[0] for x in xy], [x[1] for x in xy], color='blue', label='Initial Points')
    # plt.show()
    prev_max = max_area
    for i in range(len(xy)):
        for j in range(i+1,len(xy)):
            test_area = area2(xy,i,j)
            max_area = max(max_area, test_area)
            # print('area:', xy[i],xy[j], test_area)
            if max_area > prev_max:
                # fig, ax = plt.subplots()
                # ax.scatter([x[0] for x in xy], [x[1] for x in xy], color='blue', label='Initial Points')
                # pt_rm1 = ax.scatter(xy[i][0], xy[i][1], color='red', marker='o', s=100, label='New Point')
                # pt_rm2 = ax.scatter(xy[j][0], xy[j][1], color='red', marker='o', s=100, label='New Point')
                # plt.show()
                # pt_rm1.remove()
                # pt_rm2.remove()
                print('found new max:', xy[i],xy[j], max_area)
                prev_max = max_area
    print(max_area)
start = time.time()
# part1()
part2()
stop = time.time()
print('Finish in:',(stop-start),'s')
#p1 339151449 not even close
#p2 93043 too low, 4620654558 too high
#4575402240