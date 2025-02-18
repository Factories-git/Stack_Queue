from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    copy_impo = sorted(importance.copy())
    new_importance = deque([idx, i] for idx, i in enumerate(importance))
    i = 0
    order = []
    while copy_impo:
        if new_importance[0][1] == copy_impo[-1]:
            copy_impo.pop()
            s = new_importance.popleft()
            order.append(s[0])
        else:
            new_importance.append(new_importance.popleft())
    print(order.index(m)+1)