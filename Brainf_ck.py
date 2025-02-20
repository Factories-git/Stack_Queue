import sys

input = sys.stdin.readline

for _ in range(1, int(input())+1):
    pointer = 0
    ipts = ''
    memory = [0] * 32768
    while True:
        ipt = input().rstrip()
        if ipt == 'end':
            break
        ipt = ipt[:ipt.find('%')]
        ipts = ''.join(ipt)
        print(ipt, ipts)
    for i in ipts:
        for j in i:
            if j == '%':
                continue
            if j == '>':
                pointer = (pointer + 1) % 32768
            elif j == '<':
                pointer = (pointer - 1) % 32768
            elif j == '+':
                memory[pointer] += 1
            elif j == '-':
                memory[pointer] -= 1
            print(memory[:5], pointer, ipts)