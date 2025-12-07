
import util
import time
import numpy as np
from collections import deque
np.seterr(divide='ignore', invalid='ignore')
np.set_printoptions(linewidth=100, formatter={'all': lambda x: f'{x:<1.5}'})

lines = util.parse('d5.txt')

def main():
    count = 0
    foundBreak = False
    ingredients = []
    freshIng = []
    for line in lines:
        # line = lines[i]
        if line == '':
            foundBreak = True
            continue
        if foundBreak:
            ingredients.append(int(line))
        else:
            low,high = line.split('-')
            freshIng.append((int(low),int(high)))
    # print(ingredients)
    # print(freshIng)
    for ing in ingredients:
        for fresh in freshIng:
            if ing >= fresh[0] and ing <= fresh[1]:
                count += 1
                break
    print(count)
    count=0
    freshIng = sorted(freshIng)
    print(freshIng)
    new_fresh = []
    new_fresh.append(freshIng[0])
    idx = 0
    for i in range(1,len(freshIng)):
        l,h = new_fresh[idx]
        l1,h1 = freshIng[i]
        if l <= l1 <= h:
            #inclusive
            if h1 <= h:
                continue
            # longer case:
            new_fresh[idx] = (l,l1-1)
            new_fresh.append((l1,h1))
        else:
            new_fresh.append((l1,h1))
        idx += 1
    print(new_fresh)
    for l,h in new_fresh:
        count += h-l+1
    print(count)
start = time.time()
main()
stop = time.time()
print('Finish in:',(stop-start)/1000,'s')
