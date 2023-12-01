import util
lines = util.parse("input7.txt")
lines = util.parse("sample7.txt")

def recurse2(i, parent, dirName, curSize):
    if i >= len(lines):
        return (len(lines),0)
    s = lines[i].split(' ')
    path = getPath(parent, dirName)
    print(i, path)
    if s[0] == '$':
        if s[1] == 'cd':
            if s[2] == '..':
                print('returning', curSize)
                return (i, curSize)
            else:
                (i, sizeTmp) = recurse2(i+1, path, s[2], 0)
                print(path, s[2], sizeTmp)
                f[path] = curSize + sizeTmp
                (i, tmp) = recurse2(i+1, parent, dirName, 0)
        elif s[1] == 'ls':
            (i, tmp) = recurse2(i+1, parent, dirName, 0)
    else:
        size = 0
        if s[0] != 'dir':
            size = int(s[0])
        (i, tmp) = recurse2(i+1, parent, dirName, curSize+size)
    return (i, curSize)
def getPath(parent, dirName):
    if parent:
        if parent == '/':
            path = parent+dirName
        else:
            path = parent+"/"+dirName
    else:
        path = dirName
    return path

f = dict()

#for i in range(0, len(lines)):
#    l = lines[i]
#    s = l.split(' ')
#    if s[0] == '$':
#        if s[1] == 'cd':
#            cd(i+1, '', s[2])
recurse2(0,'','', 0)
print(f)
totalAtMost100k=0
for p in f:
    if f[p] <= 100000:
        totalAtMost100k += f[p]
print(totalAtMost100k)
