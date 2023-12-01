import util
inputVal = util.parse('input4.txt')
#inputVal = util.parse('test.input')
numbers = inputVal[0]
games = []
newgame = True
rowCount = 0
for i in range(1,len(inputVal)):
    l = inputVal[i].strip()
    if not l:
        newgame = True
        numInGame = {}
        rowCount = 0
        continue
    nums = l.split(' ')
    col = 0
    for n in nums:
        if not n:
            continue
        pos = (rowCount, col)
        numInGame[int(n)] = pos
        col += 1

    rowCount += 1
    if rowCount == 5:
        emptyScore = {0: set(), 1: set(), 2: set(), 3: set(), 4: set()}
        emptyScore2 = {0: set(), 1: set(), 2: set(), 3: set(), 4: set()}
        games.append((numInGame,emptyScore,emptyScore2))

print('Begin playing')
numbers = numbers.split(',')
numbers = list(map(int, numbers))
end=False
won =[]
for num in numbers:
    for i in range(len(games)):
        if i in won:
            continue
        game = games[i]
        g = game[0]
        sRow = game[1]
        sCol = game[2]
        if num in g:
            #print(num)
            #print(g)
            pos = g[num]
            sRow[pos[0]].add(num) # add to row score
            sCol[pos[1]].add(num) # add to column score
            #print(s)
            # check column
            if len(sRow[pos[0]]) == 5 or len(sCol[pos[1]]) == 5:
                #found winner
                print(g)
                print(sRow)
                print(sCol)
                print('winner = ' + str(sRow[pos[0]]))
                print('winner = ' + str(sCol[pos[1]]))
                sumScore = 0
                for row in sRow:
                    sumScore += sum(sRow[row])
                sumAll = sum(g)
                unmarkSum = sumAll - sumScore
                print('WinNum=%i sumScore=%i unmarkSum=%i score=%i' %(num, sumScore, unmarkSum, unmarkSum*num))
                won.append(i)
                if len(won) == len(games):
                    break

#print(numbers)
#print(games)
#p[1][p[0][num]].append(num)
