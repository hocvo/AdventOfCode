
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
    freshIng = set()
    for line in lines:
        # line = lines[i]
        if line == '':
            foundBreak = True
            continue
        if foundBreak:
            ingredients.append(int(line))
        else:
            low,high = line.split('-')
            freshIng.add((int(low),int(high)))
    # print(ingredients)
    # print(freshIng)
    for ing in ingredients:
        for fresh in freshIng:
            if ing >= fresh[0] and ing <= fresh[1]:
                count += 1
                break
    print(count)
start = time.time()
main()
stop = time.time()
print('Finish in:',(stop-start)/1000,'s')
