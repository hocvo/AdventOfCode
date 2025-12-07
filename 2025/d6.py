import util
import numpy as np
import time
lines = util.parse('d6.txt')

def main():
    sum = 0
    nums1 = [int(x) for x in lines[0].split(' ')]
    nums2 = [int(x) for x in lines[1].split(' ')]
    nums3 = [int(x) for x in lines[2].split(' ')]
    nums4 = [int(x) for x in lines[3].split(' ')]
    ops = lines[4].split()

    print ('size:', len(nums1),len(nums2),len(nums3),len(ops))
    print (nums1)
    print (nums2)
    print (nums3)

    for i in range(len(nums1)):
        if ops[i] == '*':
            res = nums1[i] * nums2[i] * nums3[i] * nums4[i]
            sum += res
            print(nums1[i], '*', nums2[i], '*', nums3[i], '=', res)
        else:
            res = nums1[i] + nums2[i] + nums3[i] + nums4[i]
            sum += res
            print(nums1[i], '+', nums2[i], '+', nums3[i], '=', res)
    print(sum)

def part2():
    sum = 0
    nums1 = [x for x in lines[0].split(' ')]
    nums1 = [' ' if x == '' else x for x in nums1]
    nums2 = [x for x in lines[1].split(' ')]
    nums2 = [' ' if x == '' else x for x in nums2]
    nums3 = [x for x in lines[2].split(' ')]
    nums3 = [' ' if x == '' else x for x in nums3]
    nums4 = [x for x in lines[3].split(' ')]
    nums4 = [' ' if x == '' else x for x in nums4]
    ops = lines[4].split()

    idx = (0,0,0,0)
    for op in ops:
        i1,i2,i3,i4 = idx
        max_len = max(len(nums1[i1]),len(nums2[i2]),len(nums3[i3]),len(nums4[i4]))

        # print("max_len", max_len)
        num1, num2, num3 = nums1[i1], nums2[i2], nums3[i3]
        num4 = nums4[i4]
        #first row
        while len(num1) < max_len:
            i1 += 1
            if (i1 >= len(nums1)):
                num1 = num1 + ' '
            else:
                num1 = num1 + nums1[i1]
        #2nd row
        while len(num2) < max_len:
            i2 += 1
            if (i2 >= len(nums2)):
                num2 = num2 + ' '
            else:
                num2 = num2 + nums2[i2]
        #3rd row
        while len(num3) < max_len:
            i3 += 1
            if (i3 >= len(nums3)):
                num3 = num3 + ' '
            else:
                num3 = num3 + nums3[i3]
        #4th row
        while len(num4) < max_len:
            i4 += 1
            if (i4 >= len(nums4)):
                num4 = num4 + ' '
            else:
                num4 = num4 + nums4[i4]
        idx = (i1+1,i2+1,i3+1,i4+1)
        m = [list(x) for x in [num1,num2,num3,num4]]
        print(m)
        m = np.matrix(m)
        new_nums = [''.join(x) for x in m.T.tolist()]
        res = 1 if op == '*' else 0
        for num in new_nums:
            if op == '*':
                res *= int(num)
            else:
                res += int(num)
        # num1 = int(new_nums[0])
        # num2 = int(new_nums[1])
        # num3 = int(new_nums[2])
        # num4 = int(new_nums[3])
        sum += res

    print(sum)

start = time.time()
part2()
stop = time.time()
print('Finish in:',(stop-start)/1000,'s')

#p1 2462060 too low
#p1 3381180 too low