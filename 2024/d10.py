import util
lines = util.parse('d10.txt')
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
    score = 0 # part 1
    rating = 0 # part 2
    R = len(lines)
    C = len(lines[0])
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "0":
                q = list()
                seen = set()
                q.append((r,c))
                while q:
                    (i,j) = q.pop(0)
                    #print("checking", i,j)
                    if lines[i][j] == '9':
                        if (i,j) not in seen:
                            seen.add((i,j))
                        rating += 1
                    for n in util.neighborsCrossIndex(lines, i,j):
                        #print("processing neighbor", n, "curHeight:",lines[i][j], "neighbor height:",lines[n[0]][n[1]])
                        if int(lines[n[0]][n[1]]) - int(lines[i][j]) == 1:
                            # print("found increment, adding",n)
                            q.append(n)
                score += len(seen)
    print(score, rating)

main()
