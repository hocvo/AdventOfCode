import util
import time
lines = util.parse('d11.txt')


def find_path(rack, res, from_, to, track):
    if to in rack[from_]:
        res.add(track)
        return
    for out in rack[from_]:
        if out in track:
            continue
        copy_track = tuple(track) + tuple([out])
        find_path(rack, res, out, to, copy_track)

def part1():
    rack = {}
    for line in lines:
        key, out = line.split(':')
        outs = out.strip().split()
        rack[key] = set(outs)
        res = set()
    find_path(rack, res, 'you', 'out', [])
    print(len(res))
start = time.time()
part1()
# part2()
stop = time.time()
print('Finish in:',(stop-start),'s')