"""
시간초과
"""

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def my_while(ipts):
    stack = []
    c = {}
    for i, code in enumerate(ipts):
        if code == '[':
            stack.append(i)
        if code == ']':
            if not stack:
                return False
            st = stack.pop()
            c[st] = i
            c[i] = st
    if stack:
        return False

    return c


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
    dic = my_while(ipts)
    if dic is False:
        print('COMPILE ERROR')
        continue
    idx = 0
    while idx < len(ipts):
        j = ipts[idx]
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
            if memory[pointer] == 0:
                idx = dic[idx]
        elif j == ']':
            if memory[pointer] != 0:
                idx = dic[idx]
        idx += 1
    print(''.join(s) if not flag else '')
