import sys

input = sys.stdin.readline
print = sys.stdout.write

while True:
    stack = []
    msg = input().rstrip()
    if msg == '.':
        break
    check = True
    for m in msg:
        if m == '(' or m == '[':
            stack.append(m)
        elif m == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                check = False
                break
        elif m == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                check = False
                break
    print(f'{"yes" if check and not stack else "no"}\n')