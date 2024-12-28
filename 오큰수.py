n = int(input())
tower = list(map(int, input().split()))
re = [-1] * n
new = [i for i in tower]
stack = []
for i in range(n-1, -1, -1):
    while stack:
        if stack[-1] <= new[i]:
            stack.pop()
        else:
            re[i] = stack[-1]
            break
    stack.append(new[i])
print(*re)
