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

    circuits = []
    heap = []
    sorted_dist_items = sorted(dist_map.items(), key=lambda item: item[1])

    connections = 0
    idx = 0
    remain = set(range(len(lines)))
    while idx < 1000:
        closest = sorted_dist_items[idx]
        # print(junc_boxes[closest[0][0]], junc_boxes[closest[0][1]])
        it = iter(circuits)
        # c = next((x for x in circuits if closest[0][0] in x or closest[0][1] in x), set())
        cs = [x for x in circuits if closest[0][0] in x or closest[0][1] in x]
        # prev_len = len(c)
        if len(cs) == 0:
            c = set()
            c.add(closest[0][0])
            c.add(closest[0][1])
            circuits.append(c)
            connections += 1
        elif len(cs) == 1:
            c = cs[0]
            # print('adding',closest[0][0],closest[0][1], 'to set',c)
            c.add(closest[0][0])
            c.add(closest[0][1])
            connections += 1
        else:
            # print('found',closest[0][0],closest[0][1], 'in 2 different set',cs)
            cs[0].update(cs[1])
            circuits.remove(cs[1])

        # remain.discard(closest[0][0])
        # remain.discard(closest[0][1])
        # if len(c) > prev_len:
            # connections += 1

        # print('remain:',len(remain))
        idx += 1
    for c in circuits:  
        # print(c)
        heapq.heappush(heap, len(c))
    while len(heap) > 3:
        heapq.heappop(heap)
    cir_size = 1
    while heap:
        cir_size *= heapq.heappop(heap)
    print(cir_size)

start = time.time()
main()
stop = time.time()
print('Finish in:',(stop-start)/1000,'s')

#p1 7106 too low
#p1 9240 not right
#8779, 8360 not right
#using heapq 9702 not right
#13800 not right
#ans = 122430