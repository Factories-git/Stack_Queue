n = int(input())
Lines = list(map(int, input().split()))
stack = []
now = 1

for i in Lines:
    while stack and stack[-1] == now:
        stack.pop()
        now += 1
    if i == now:
        now += 1
    else:
        stack.append(i)

while stack and now == stack[-1]:
    stack.pop()
    now += 1

if stack:
    print('Sad')
else:
    print('Nice')