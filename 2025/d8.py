import util
import time
import math
import heapq

lines = util.parse('d8.txt')

def calc_dist(p, q):
    d = (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2 + (q[2] - p[2]) ** 2
    return d

def main():
    junc_boxes = []
    dist_map = {}
    for line in lines:
        junc_boxes.append([int(x) for x in line.split(',')])
    for i in range(len(junc_boxes)):
        for j in range(i+1,len(junc_boxes)):
            dist = calc_dist(junc_boxes[j], junc_boxes[i])
            dist_map[(i,j)] = dist

    circuits = [set([i]) for i in range(len(lines))]
    heap = []
    sorted_dist_items = sorted(dist_map.items(), key=lambda item: item[1])

    idx = 0
    remain = set(range(len(lines)))
    last_junction =  sorted_dist_items[idx]
    while idx < 1000: #part1
        closest = sorted_dist_items[idx]
        # print(junc_boxes[closest[0][0]], junc_boxes[closest[0][1]])
        cs = [x for x in circuits if closest[0][0] in x or closest[0][1] in x]
        # print(cs)
        if len(cs) < 2:
            idx += 1
            continue
        cs[0].update(cs[1])
        circuits.remove(cs[1])
        # print(circuits)
        last_junction =  sorted_dist_items[idx]
        idx += 1
    # use heapq or sort list both work
    # for c in circuits:  
        # print(c)
        # heapq.heappush(heap, len(c))
    # while len(heap) > 3:
        # heapq.heappop(heap)
    circuits.sort(key=len, reverse=True)
    cir_size = 1
    for i in range(3):
        cir_size *= len(circuits[i])
    print(cir_size)

def part2():
    junc_boxes = []
    dist_map = {}
    for line in lines:
        junc_boxes.append([int(x) for x in line.split(',')])
    for i in range(len(junc_boxes)):
        for j in range(i+1,len(junc_boxes)):
            dist = calc_dist(junc_boxes[j], junc_boxes[i])
            dist_map[(i,j)] = dist

    circuits = [set([i]) for i in range(len(lines))]
    heap = []
    sorted_dist_items = sorted(dist_map.items(), key=lambda item: item[1])

    idx = 0
    remain = set(range(len(lines)))
    last_junction =  sorted_dist_items[idx]
    while len(circuits) > 1 and idx < len(sorted_dist_items): #part2
    # while idx < 10: #part1
        closest = sorted_dist_items[idx]
        # print(junc_boxes[closest[0][0]], junc_boxes[closest[0][1]])
        cs = [x for x in circuits if closest[0][0] in x or closest[0][1] in x]
        # print(cs)
        if len(cs) < 2:
            idx += 1
            continue
        cs[0].update(cs[1])
        circuits.remove(cs[1])
        # print(circuits)
        last_junction =  sorted_dist_items[idx]
        idx += 1
    print(junc_boxes[last_junction[0][0]],junc_boxes[last_junction[0][1]])
    x1 = junc_boxes[last_junction[0][0]][0]
    x2 = junc_boxes[last_junction[0][1]][0]
    print(x1*x2)
start = time.time()
main()
part2()
stop = time.time()
print('Finish in:',(stop-start)/1000,'s')

#p1 7106 too low
#p1 9240 not right
#8779, 8360 not right
#using heapq 9702 not right
#13800 not right
#ans = 122430