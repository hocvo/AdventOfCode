import util
lines = util.parse('d2.txt')
# convert to int: int(str)
# convert to str: str(any)
# list(): [any,any,...]
# set(): {any,any,...}
# frozenset(): immutable set
# dict(): {k:v, k:v, ...}
# tuple():  An ordered, immutable collection of items (e.g., (1, 2, "apple"))
# range: Represents a sequence of numbers (e.g., range(5), range(1, 5), range(1,5,2))

 # removable not working. Using brute force get 430 while using removable would only get 426
def testReport(nums, removable):
    #print (nums)
    shouldCount = True
    isIncreasing = nums[1] > nums[0]
    shouldCount = True
    i = 1
    j = 0
    while i < len(nums) and j < len(nums):
        if nums[i] >= nums[j]:
            if not isIncreasing or nums[i]-nums[j] > 3 or nums[i]-nums[j] < 1:
                if removable > 0:
                    removable -= 1
                    nums1 = list(nums)
                    nums1.pop(i)
                    nums2 = list(nums)
                    nums2.pop(j)
                    return testReport(nums1,0) or testReport(nums2,0)
                shouldCount = False
                break
        elif nums[i] < nums[j]:
            if isIncreasing or nums[j]-nums[i] > 3 or nums[j]-nums[i] < 1:
                if removable > 0:
                    removable -= 1
                    nums1 = list(nums)
                    nums1.pop(i)
                    nums2 = list(nums)
                    nums2.pop(j)
                    return testReport(nums1,0) or testReport(nums2,0)
                shouldCount = False
                break
        i = i + 1
        j = j + 1
    return shouldCount

def part1():
    count = 0
    for l in lines:
        nums = l.split()
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        if testReport(nums,0):
            count += 1
    print(count)

def part2():
    count = 0
    for l in lines:
        nums = l.split()
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        if testReport(nums,1):
            count += 1
        else:
            for i in range(len(nums)):
                newNums = list(nums)
                newNums.pop(i)
                if testReport(newNums,0):
                    count += 1
                    break
    print(count)

part1()
part2()