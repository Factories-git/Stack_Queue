import sys

input = sys.stdin.readline

stack = []
for i in range(int(input())):
    ipt = input().split()
    if ipt[0] == '1':
        _, num = ipt
        stack.append(int(num))
    elif ipt[0] == '2':
        print(stack.pop() if stack else -1)
    elif ipt[0] == '3':
        print(len(stack))
    elif ipt[0] == '4':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)