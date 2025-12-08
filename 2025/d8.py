import util
import time
import math

lines = util.parse('test.txt')

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
    sorted_dist_items = sorted(dist_map.items(), key=lambda item: item[1])

    connections = 0
    idx = 0
    remain = set(range(len(lines)))
    while connections <= 10:
        closest = sorted_dist_items[idx]
        # print(junc_boxes[closest[0][0]], junc_boxes[closest[0][1]])
        found = False
        # c = x for i,x in enumerate(circuits) if (closest[0][0] in x or closest[0][1] in x)
        c = next((x for x in circuits if closest[0][0] in x), set())
        prev_len = len(c)
        if not c:
            circuits.append(c)
        c.add(closest[0][0])
        c.add(closest[0][1])
        if len(c) > prev_len:
            connections += 1
        # for c in circuits:
        #     if closest[0][0] in c and closest[0][1] in c:
        #         found = True
        #         break
        #     elif closest[0][0] in c or closest[0][1] in c:
        #         c.add(closest[0][0])
        #         c.add(closest[0][1])
        #         if closest[0][0] in remain:
        #             remain.remove(closest[0][0])
        #         if closest[0][1] in remain:
        #             remain.remove(closest[0][1])
        #         connections += 1
        #         found = True
        #         break
        # if not found:
        #     cir = set()
        #     cir.add(closest[0][0])
        #     cir.add(closest[0][1])
        #     if closest[0][0] in remain:
        #         remain.remove(closest[0][0])
        #     if closest[0][1] in remain:
        #         remain.remove(closest[0][1])
        #     circuits.append(cir)
        #     connections += 1

        # print('remain:',len(remain))
        idx += 1
    # print('circuits:', len(circuits))
    # print(circuits)
    circuits.sort(key=len,reverse=True)
    cir_size = 1
    for i in range(3):
        cir_size *= len(circuits[i])
    print(cir_size)

start = time.time()
main()
stop = time.time()
print('Finish in:',(stop-start)/1000,'s')

#p1 7106 too low