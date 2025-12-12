import util
import time
import numpy as np
lines = util.parse('test.txt')

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
        found = press_button(btns, i, copy_cur_press, expect_ind, copy_cur_ind, copy_seen_ind, res)
        if found:
            res.add(len(copy_cur_press))
        seen_ind.add(tuple(cur_ind))
    return False

def press_button_jolt(btns, press_idx, cur_press, cur_jol, seen, res):
    if res:
        min_press = min(res)
        if len(cur_press) >= min_press:
            return False
    if tuple(cur_jol) in seen:
        res.add(len(cur_press) + seen[tuple(cur_jol)])
        return True
    if any(x < 0 for x in cur_jol):
        return False

    found = False
    for i in range(len(btns)):
        copy_cur_press = list(cur_press)
        copy_cur_jol = list(cur_jol)
        for jol_idx in btns[i]:
            copy_cur_jol[jol_idx] -= 1
        copy_cur_press.append(btns[i])
        found1 = press_button_jolt(btns, press_idx, copy_cur_press, copy_cur_jol, seen, res)
        if found1:
            found = True
            seen[tuple(cur_jol)] = 1 + seen[tuple(copy_cur_jol)]
    return found

def press_button_jolt2(btns, cur_jol, seen, cur_press):
    if all(0==x for x in cur_jol):
        return cur_press
    if tuple(cur_jol) in seen:
        return seen[tuple(cur_jol)]
    if any(x < 0 for x in cur_jol):
        return 9999999999
    press_count = 9999999999
    for i in range(len(btns)):
        copy_cur_jol = list(cur_jol)
        for jol_idx in btns[i]:
            copy_cur_jol[jol_idx] -= 1
        press_count = min(press_count, press_button_jolt2(btns, copy_cur_jol, seen, cur_press+1))
    if tuple(cur_jol) in seen:
        seen[tuple(cur_jol)] = min(seen[tuple(cur_jol)],press_count)
        press_count = seen[tuple(cur_jol)]
    else:
        seen[tuple(cur_jol)] = press_count
    return press_count

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
    count_ind = 0
    for i in range(len(indicators)):
        cur_ind = [-1 for i in indicators[i]]
        seen_ind = set()
        seen_ind.add(tuple(cur_ind))
        res = set()
        press_button(buttons[i],-1,list(),indicators[i],cur_ind, seen_ind,res)
        count_ind += min(res)
    print(count_ind)
    count_jol = 0
    for i in range(len(joltages)):
        seen = {tuple([0 for x in joltages[i]]): 1}
        buttons[i].sort(key=len,reverse=True)
        count_jol += press_button_jolt2(buttons[i],joltages[i],seen, 0)
        print(count_jol)
    print(count_jol)

start = time.time()
part1()
#part2()
stop = time.time()
