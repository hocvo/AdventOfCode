import util
lines = util.parse('d9.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))
# lines = ["12345"]
def main():
    checksum = 0
    l = lines[0]
    disk = list()
    id = 0
    for i in range(0,len(l),2):
        numFile = int(l[i])
        while numFile > 0:
            disk.append(str(id))
            numFile -= 1
        if (i+1 < len(l)):
            numFree = int(l[i+1])
            while numFree > 0:
                disk.append('.')
                numFree -= 1
        # print("files: ", numFile, " free: ", numFree)
        id += 1
    disk = part2(disk)
    i = 0
    while i < len(disk):
        # print("checksum ", disk[i])   
        if disk[i] == ".":
            i += 1
            continue
        checksum += i * int(disk[i])
        i += 1
    print(checksum)

def part1(disk):
    j = len(disk)-1
    for i in range(len(disk)):
        if i > j:
            break
        if disk[i] == ".":
            while j > i:
                if disk[j] != ".":
                    # print("swapping ", disk[i], " and ", disk[j])
                    disk[i], disk[j] = disk[j], disk[i]
                    break
                j -= 1
    return disk
#part 2
def part2(disk):
    i = len(disk) - 1
    diskMap = dict()
    while i >= 0:
        if disk[i] == ".":
            i -= 1
            continue
        if disk[i] not in diskMap:
            diskMap[disk[i]] = (i, 1)
        else:
            diskMap[disk[i]] = (i, diskMap[disk[i]][1] + 1)
        i -= 1
    print(diskMap)
    for k in diskMap:
        i = 0
        size = diskMap[k][1]
        print("Checking to move ", k, " with size", size)
        while i < diskMap[k][0]:
            if disk[i] == ".":
                potentialI = i
                count = size
                while disk[i] == "." and count > 0:
                    i += 1
                    count -= 1
                if count <= 0:
                    print("Swapping from index ", potentialI, " to ", potentialI + size-1)
                    for z in range(potentialI, potentialI + size):
                        disk[z] = k
                    for z in range(diskMap[k][0], diskMap[k][0]+diskMap[k][1]):
                        disk[z] = '.'
                    break
            i += 1
    return disk
