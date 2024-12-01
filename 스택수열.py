import sys

input = sys.stdin.readline

command = ''
now = 0
for i in range(int(input())):
    goal = int(input())
    while goal != now:
        if goal > now:
            now += 1
            command += '+'
        else:
            now -= 1
            command += '-'
print(command)