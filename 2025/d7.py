
import numpy as np
import util
import time
from collections import deque
np.seterr(divide='ignore', invalid='ignore')
np.set_printoptions(linewidth=100, formatter={'all': lambda x: f'{x:<1.5}'})


lines2 = util.parse('d7.txt')
C = len(lines2[0])
seen = dict()
def max_timeline(l, row, beam_idx):
    if (row, beam_idx) in seen:
        return seen[(row,beam_idx)]
    if row >= len(l):
        return 1
    split_idx = set([i for i, x in enumerate(list(l[row])) if x == "^"])

    timeline = 0
    if beam_idx in split_idx:
        if 0 <= beam_idx-1 < C:
            timeline += max_timeline(l, row+1, beam_idx-1)
        if 0 <= beam_idx+1 < C:
            timeline += max_timeline(l, row+1, beam_idx+1)
    else:
        timeline += max_timeline(l, row+1, beam_idx)

    seen[(row, beam_idx)] = timeline
    return timeline

def part1():
    lines = [list(x) for x in lines2]
    start_col = lines[0].index('S')
    split_count = 0
    row = 1
    lines[row][start_col] = '|'
    beam_idxs = [i for i, x in enumerate(list(lines[row])) if x == "|"]
    while row < len(lines):
        split_idx = set([i for i, x in enumerate(list(lines[row])) if x == "^"])
        for beam in beam_idxs:
            if beam in split_idx:
                split_count += 1
                if 0 <= beam-1 < C:
                    lines[row][beam-1] = '|'
                if 0 <= beam+1 < C:
                    lines[row][beam+1] = '|'
            else:
                lines[row][beam] = '|' #bring it down
        beam_idxs = [i for i, x in enumerate(list(lines[row])) if x == "|"]
        row += 1
    print(split_count)

def main():
    lines = [list(x) for x in lines2]
    start_col = lines[0].index('S')
    split_count = 0
    row = 1
    lines[row][start_col] = '|'
    beam_idx = lines[row].index("|")
    timeline = max_timeline(lines,row,beam_idx)
    print(timeline)


start = time.time()
main()
stop = time.time()
print('Finish in:',(stop-start)/1000,'s')