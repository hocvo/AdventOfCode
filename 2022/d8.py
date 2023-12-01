import util
lines = util.parse('input8.txt')
m = []
for i in range(len(lines)):
    m.append([])
    for c in lines[i]:
        m[i].append(int(c))

#print(m)
rowNum = len(m)
colNum = len(m[1])
neighborIndex = [1,-1]
neighborIndex = [[1,0],[-1,0],[0,-1],[0,1]]
maxView = []
def visible(treeVal, r, c):
    #print("Processing ", treeVal, "Row: ", r, "Col: ", c)
    #if r == 0 or r == len(m)-1:
        #print("Edge row ", r)
        #return True
    #if c == 0 or c == len(m[0])-1:
        #print("Edge col ", r)
        #return True
    visible = False
    viewD = 0
    viewU = 0
    viewR = 0
    viewL = 0
    for index in neighborIndex:
        neighborR = r + index[0]
        neighborC = c + index[1]
        #if m[neighborR][neighborC] < treeVal:
        visible = True
        #down
        if index[0] == 1:
            i = neighborR
            while i < rowNum:
                #print("Checking down ", m[i][neighborC])
                viewD += 1
                if m[i][neighborC] >= treeVal:
                    visible = False
                    break
                i += 1
            #if visible:
                #return visible
        #up
        elif index[0] == -1:
            i = neighborR
            while i >= 0:
                #print("Checking up", m[i][neighborC])
                viewU += 1
                if m[i][neighborC] >= treeVal:
                    visible = False
                    break
                i -= 1
            #if visible:
                #return visible
        #right
        elif index[1] == 1:
            i = neighborC
            while i < colNum:
                #print("Checking right", m[neighborR][i])
                viewR += 1
                if m[neighborR][i] >= treeVal:
                    visible = False
                    break
                i += 1
            #if visible:
                #return visible
        #left
        elif index[1] == -1:
            i = neighborC
            while i >= 0:
                #print("Checking right", m[neighborR][i])
                viewL += 1
                if m[neighborR][i] >= treeVal:
                    visible = False
                    break
                i -= 1
            #if visible:
                #return visible
    #print("returning ", visible)
    #print("views: ",viewD,viewU, viewR,viewL)
    maxView.append(viewD*viewU*viewR*viewL)
    return visible

visibleTree = 0
for i in range(len(m)):
    row = m[i]
    for j in range(len(row)):
        tree = row[j]
        if visible(tree, i, j):
            visibleTree += 1
print(visibleTree)
maxView.sort()
print(maxView)
print(maxView[-1])
