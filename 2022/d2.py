import util

lines = util.parse('input2.txt')

score = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2,'Z':3}
game = ['A','B','C','A']
myScore = 0
theirScore = 0
for l in lines:
    g = l.split(' ')
    if g[0] == 'A':
        if g[1] == 'X':
            myScore += score['C'] + 0
        elif g[1] == 'Z':
            myScore += score['B'] + 6
        else:
            myScore += score[g[0]] + 3
    elif g[0] == 'B':
        if g[1] == 'X':
            myScore += score['A']
        elif g[1] == 'Z':
            myScore += score['C'] + 6
        else:
            myScore += score[g[0]] + 3
    elif g[0] == 'C':
        if g[1] == 'X':
            myScore += score['B']
        elif g[1] == 'Z':
            myScore += score['A'] + 6
        else:
            myScore += score[g[0]] + 3
print(myScore)
