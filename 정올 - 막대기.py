import sys

n = int(input())
nums = [int(sys.stdin.readline()) for i in range(n)]
count = 1
curr = nums[-1]
for i in range(n-2, -1, -1):
    if nums[i] > curr:
        curr = nums[i]
        count += 1

print(count)