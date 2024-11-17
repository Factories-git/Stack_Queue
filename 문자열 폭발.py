stack = []
s = input()
bomb = input()
b = len(bomb)
for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-b:]) == bomb:
        for _ in range(b):
            stack.pop()
print(''.join(stack) if stack else 'FRULA')