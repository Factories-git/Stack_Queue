import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
isQueue = list(map(int, input().split()))
ex_elements = list(map(int, input().split()))
m = int(input())
new_elements = list(map(int, input().split()))

queueStack = deque()
for i in range(n):
    if isQueue[i] == 0:
        queueStack.append(ex_elements[i])

for i in range(m):
    queueStack.appendleft(new_elements[i])
    print(queueStack[-1], end=' ')
    queueStack.pop()