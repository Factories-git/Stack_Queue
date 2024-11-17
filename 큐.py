import sys
from collections import deque

input = sys.stdin.readline

dq = deque()
t = int(input())
for i in range(t):
    cmd = input().strip()
    if cmd[:5] == 'push ':
        dq.append(int(cmd[4:]))
    elif cmd == 'pop':
        if dq:
            j = dq.popleft()
        else:
            j = -1
        print(j)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        print(dq[0])
    else:
        print(dq[-1])