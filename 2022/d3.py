import util
lines = util.parse('input3.txt')
char_a = 1
char_A = 27
total=0
for l in lines:
    mid = int(len(l)/2)
    firstHalf = l[:mid]
    secondHalf = l[mid:]
    seen = set()
    for c in secondHalf:
        if c in firstHalf and c not in seen:
            seen.add(c)
            if c.isupper():
                total += ord(c) - ord('A') + char_A
            else:
                total += ord(c) - ord('a') + char_a
print(total)
#part 2
total = 0
for i in range(0,len(lines),3):
    group = lines[i:i+3]
    longest = 0
    for j in range(3):
        if len(group[j]) > longest:
            longest = len(group[j])
            startGroup = j
    #print('longest index = %i' % startGroup)
    for item in group[startGroup]:
        if item in group[(startGroup-1)%3] and item in group[(startGroup+1)%3]:
            if item.isupper():
                total += ord(item) - ord('A') + char_A
            else:
                total += ord(item) - ord('a') + char_a
            break

print(total)
