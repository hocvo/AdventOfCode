import util
import time
lines = util.parse('d11.txt')

# work great for part 1 but not 2
# def find_path(rack, res, from_, to, track, seen):
#     if to in rack[from_]:
#         res.add(track)
#         return True
#     if from_ in seen:
#         for path in seen[from_]:
#             res.add(track+tuple(path))
#         return True
#     found = False
#     for out in rack[from_]:
#         if out in track:
#             continue
#         copy_track = tuple(track) + tuple([out])
#         if find_path(rack, res, out, to, copy_track,seen):
#             tmp = list(copy_track)
#             idx = tmp.index(from_)
#             if from_ in seen:
#                 seen[from_].append(tmp[idx+1:])
#             else:
#                 seen[from_] = [tmp[idx+1:]]
#             found = True
#     return found

def find_path3(rack, from_, to, track, seen):
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
        count += find_path3(rack, des, to, copy_track,seen)
    seen[from_] = count
    return count

#semi working. not for huge network
# def find_path2(rack, res, from_, to, track, seen):
#     if from_ == 'out':
#         return []
#     if to in rack[from_]:
#         res.add(track + tuple([to]))
#         return [to]
#     paths = []
#     if from_ in seen:
#         for l in seen[from_]:
#             if to in l:
#                 res.add(track+tuple(l))
#         return seen[from_]
#     for out in rack[from_]:
#         if out in track:
#             continue
#         p = [out]
#         copy_track = tuple(track) + tuple([out])
#         ret = find_path2(rack, res, out, to, copy_track,seen)
#         if any(isinstance(el, list) for el in ret): #return from main method
#             for l in ret:
#                 paths.append(p+l)
#         else: # return from found destination
#             p += ret
#         if to in p:
#             paths.append(p)
#
#     seen[from_] = paths
#     return paths


def main():
    rack = {}
    for line in lines:
        key, out = line.split(':')
        outs = out.strip().split()
        rack[key] = set(outs)
    res = set()
    count = find_path3(rack, 'you', 'out',['you'],{})
    print("part1: ", count)

    #part2
    svr_fft = find_path3(rack, 'svr', 'fft',['svr'],{})
    # print(svr_fft)
    fft_dac = find_path3(rack, 'fft', 'dac',['fft'],{})
    # print(fft_dac)
    dac_out = find_path3(rack, 'dac', 'out',['dac'],{})
    # print(dac_out)
    svr_dac = find_path3(rack, 'svr', 'dac',['svr'],{})
    # print(svr_dac)
    dac_fft = find_path3(rack, 'dac', 'fft',['dac'],{})
    # print(dac_fft)
    fft_out = find_path3(rack, 'fft', 'out',['fft'],{})
    # print(fft_out)
    count = (svr_fft * fft_dac * dac_out) + (svr_dac * dac_fft * fft_out)
    print('part2:', count)

start = time.time()
main()
stop = time.time()
print('Finish in:',(stop-start),'s')