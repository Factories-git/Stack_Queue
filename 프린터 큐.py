from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    importance = deque(map(int, input().split()))
    i = -1
    print(n,m)
    while importance:
        print(i)
        if importance[i] == max(importance):
            importance.popleft()
            if i == m:
                print(i+1)
        else:
            importance.append(importance.popleft())
