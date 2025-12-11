from twisted.python.context import setDefault

import util
import time
lines = util.parse('d11.txt')
def find_path(rack, res, from_, to, track, seen):
    if to in rack[from_]:
        res.add(track)
        return True
    if from_ in seen:
        for path in seen[from_]:
            res.add(track+tuple(path))
        return True
    found = False
    for out in rack[from_]:
        if out in track:
            continue
        copy_track = tuple(track) + tuple([out])
        if find_path(rack, res, out, to, copy_track,seen):
            tmp = list(copy_track)
            idx = tmp.index(from_)
            if from_ in seen:
                seen[from_].append(tmp[idx+1:])
            else:
                seen[from_] = [tmp[idx+1:]]
            found = True
    return found

def find_path3(rack, res, from_, to, track, seen):
    if from_ == 'out':
        return 0
    if to in rack[from_]:
        return 1
    if from_ in seen:
        return seen[from_]
    count = 0
    for des in rack[from_]:
        if des in track:
            continue
        copy_track = tuple(track) + tuple([des])
        count += find_path3(rack, res, des, to, copy_track,seen)
    return count
def find_path2(rack, res, from_, to, track, seen):
    if from_ == 'out':
        return []
    if to in rack[from_]:
        res.add(track)
        return [to]
    paths = []
    if from_ in seen:
        for l in seen[from_]:
            res.add(track+tuple(l))
        return seen[from_]
    for out in rack[from_]:
        if out in track:
            continue
        p = [out]
        copy_track = tuple(track) + tuple([out])
        ret = find_path2(rack, res, out, to, copy_track,seen)
        if any(isinstance(el, list) for el in ret): #return from main method
            for l in ret:
                paths.append(p+l)
        else: # return from found destination
            p += ret
        if to in p:
            paths.append(p)
    if paths:
        seen[from_] = paths
    return paths


def part1():
    rack = {}
    for line in lines:
        key, out = line.split(':')
        outs = out.strip().split()
        rack[key] = set(outs)
    res = set()
    # find_path2(rack, res, 'svr', 'fft', ['svr'], {})
    # count_svr_fft = len(res)
    # res = set()
    # find_path2(rack, res, 'fft', 'dac', ['fft'], {}) #3408588, 3408582
    # count_fft_dac = len(res)
    # res = set()
    # find_path2(rack, res, 'dac', 'out', ['dac'], {}) #9055
    # count_dac_out = len(res)
    # print(count_svr_fft*count_fft_dac*count_dac_out)

    print(find_path3(rack, res, 'fft', 'dac',['fft'],{}))


    print(len(res))
    dac_ftf_count = 0
    for result in res:
        path = set(result)
        if 'dac' in path and 'fft' in path:
            dac_ftf_count += 1
    print(dac_ftf_count)
start = time.time()
part1()
# part2()
stop = time.time()
print('Finish in:',(stop-start),'s')