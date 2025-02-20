import sys

input = sys.stdin.readline

def myWhile(ptr):
    global memory



for _ in range(1, int(input()) + 1):
    pointer = 0
    ipts = ''
    memory = [0] * 32768
    while True:
        ipt = input().rstrip()
        if ipt == 'end':
            break
        rf = ipt.rfind('%')
        ipt = ipt[:rf if rf != -1 else None]
        ipts += ipt
        print(ipt)
    for j in ipts:
        if j == '>':
            pointer = (pointer + 1) % 32768
        elif j == '<':
            pointer = (pointer - 1) % 32768
        elif j == '+':
            memory[pointer] += 1
        elif j == '-':
            memory[pointer] -= 1
        elif j == '.':
            print(memory[pointer])
            print(chr(memory[pointer]), end='', )
        elif j == '[':

    print()
