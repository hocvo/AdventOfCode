import util
import time
import matplotlib.pyplot as plt
import numpy as np
lines = util.parse('d10.txt')

def press_button(btns, last_press_idx, cur_press, expect_ind, cur_ind, seen_ind, res):
    # if len(cur_press) > 5:
    #     return False
    if expect_ind == cur_ind:
        return True
    if tuple(cur_ind) in seen_ind and len(cur_press) > 0: #prevent loop
        return False

    for i in range(last_press_idx+1,len(btns)):
        copy_seen_ind = set(seen_ind)
        copy_cur_press = list(cur_press)
        copy_cur_ind = list(cur_ind)
        for ind_idx in btns[i]:
            copy_cur_ind[ind_idx] = copy_cur_ind[ind_idx] * -1
        copy_cur_press.append(btns[i])
        if press_button(btns, i, copy_cur_press, expect_ind, copy_cur_ind, copy_seen_ind, res):
            res.add(len(copy_cur_press))
        seen_ind.add(tuple(cur_ind))
    return False

def part1():
    indicators = []
    buttons = []
    joltages = []
    for line in lines:
        i_open = line.index('[')
        i_close = line.index(']')
        ind = list(line[i_open+1:i_close])
        ind = [-1 if x == '.' else 1 for x in ind]
        indicators.append(ind)
        j_open = line.index('{')
        line = line[i_close+1:]
        button = []
        while line.index('{') > 0:
            b_open = line.find('(')
            if b_open < 0:
                break
            b_close = line.index(')')
            if ',' in line[b_open+1:b_close]:
                button.append(list(map(int,line[b_open+1:b_close].split(','))))
            else:
                button.append(list(map(int,line[b_open+1:b_close])))
            line = line[b_close+1:]
        buttons.append(button)
        j_open = line.index('{')
        j_close = line.index('}')
        joltages.append(list(map(int,line[j_open+1:j_close].split(','))))
    # print(indicators)
    # print(buttons)
    # print(joltages)
    count = 0
    for i in range(len(indicators)):
        cur_ind = [-1 for i in indicators[i]]
        seen_ind = set()
        seen_ind.add(tuple(cur_ind))
        res = set()
        press_button(buttons[i],-1,list(),indicators[i],cur_ind, seen_ind,res)
        count += min(res)
        #print(press_button(buttons[i],-1,5,0,indicators[i],cur_ind, seen_ind))
    print(count)
start = time.time()
part1()
#part2()
stop = time.time()

def press_button2(btns, last_press_idx, min_press, cur_press, expect_ind, cur_ind, seen_ind):
    if cur_press >= min_press:
        return min_press
    if expect_ind == cur_ind:
        return min(min_press,cur_press)
    if tuple(cur_ind) in seen_ind and cur_press > 0: #prevent loop
        return cur_press

    # min_count = 999999
    count_press = cur_press
    for i in range(len(btns)):
        if i != last_press_idx:
            for ind_idx in btns[i]:
                cur_ind[ind_idx] = cur_ind[ind_idx] * -1
            count_press = press_button(btns, i, min_press, cur_press+1, expect_ind, cur_ind, seen_ind)
            if cur_ind == expect_ind:
                min_press = count_press
            seen_ind.add(tuple(cur_ind))
            # if count_press <= min_press:
            #     return count_press
            # count_press = min(min_press,count_press)
    return min_press