"""
시간초과
"""

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def my_while(ptr, stack, idx):
    s_idx = idx
    global memory, s
    stack.append(idx)
    while True:
        if idx == len(ipts):
            if stack:
                return False
        j = ipts[idx]

        if j == '>':
            ptr = (ptr + 1) % 32768
        elif j == '<':
            ptr = (ptr - 1) % 32768
        elif j == '+':
            memory[ptr] = (memory[ptr] + 1) % 255
        elif j == '-':
            memory[ptr] = (memory[ptr] - 1) % 255
        elif j == '.':
            s.append(chr(memory[ptr]))
        elif j == '[':
            if s_idx != idx:
                my_while(ptr, stack, idx)
            else:
                return False
        elif j == ']':
            if memory[ptr] == 1:
                stack.pop()
                return True
            else:
                idx = stack[-1]
                continue
        idx += 1


for _ in range(1, int(input()) + 1):
    pointer = 0
    ipts = ''
    memory = [0] * 32768
    s = []
    flag = False
    re = []
    while True:
        ipt = input().rstrip()
        if ipt == 'end':
            break
        rf = ipt.rfind('%')
        ipt = ipt[:rf if rf != -1 else None]
        ipts += ipt
    for idx, j in enumerate(ipts):
        if j == '>':
            pointer = (pointer + 1) % 32768
        elif j == '<':
            pointer = (pointer - 1) % 32768
        elif j == '+':
            memory[pointer] = (memory[pointer] + 1) % 255
        elif j == '-':
            memory[pointer] = (memory[pointer] - 1) % 255
        elif j == '.':
            s.append(chr(memory[pointer]))
        elif j == '[':
            if idx == len(ipts):
                print('COMPILE ERROR')
                flag = True
                break
            k = my_while(pointer, [], idx + 1)
            re.append(idx + 1)
            if not k:
                print('COMPILE ERROR')
                flag = True
                break
            continue
        elif j == ']':
            if not re:
                print('COMPILE ERROR')
                flag = True

    print(''.join(s) if not flag else '')
