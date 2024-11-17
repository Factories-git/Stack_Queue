import sys

input = sys.stdin.readline

stack = []
num = 0
for i in range(int(input())):
    command = input().split()
    if len(command) == 2:
        num = int(command[1])
    commands = command[0]
    if commands == 'push':
        stack.append(num)
    elif commands == 'pop':
        if  stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)
    elif commands == 'size':
        print(len(stack))
    elif commands == 'empty':
        print(0 if stack else 1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)