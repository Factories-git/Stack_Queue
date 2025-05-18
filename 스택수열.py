import sys

input = sys.stdin.readline

command = ''
stack = []
k = int(input())
arr = [int(input()) for _ in range(k)]
n = 1
for i in range(k):
    goal = arr[i]
    if goal >= n:
        while goal >= n: #goal 이상이여야지 pop해서 수열에 저장됨
            stack.append(n)
            command += '+'
            n += 1
        stack.pop() #그래서 pop
        command += '-'
    else:
        s = stack.pop()
        if s > goal: #예제 2번 처럼 goal이 더 작은경우(현재 수보다)
            print('NO')
            exit(0)
        else: command += '-'
print('\n'.join(command))