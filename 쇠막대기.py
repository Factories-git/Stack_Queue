import sys
s = sys.stdin.readline().strip()

remain = 0
result = 0
stack = []

for idx, i in enumerate(s):
    if stack:
        if stack[-1][0] == '(' and i == ')':
            k = stack.pop()
            remain -= 1
            if idx - k[1] == 1:
                result -= 1
                result += remain
        else:
            stack.append((i, idx))
            remain += 1
            result += 1
    else:
        remain += 1
        result += 1
        stack.append((i, idx))
print(result)