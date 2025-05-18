import sys

input = sys.stdin.readline

left_stack = list(input().strip())
right_stack = []
m = int(input())
for i in range(m):
    command = str(input().strip())
    if command == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    if command == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    if command == 'B':
        if left_stack:
            left_stack.pop()
    if command.startswith('P '):
        _, char = command.split()
        left_stack.append(char)
print(''.join(left_stack + right_stack[::-1]))