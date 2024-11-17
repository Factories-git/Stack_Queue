from collections import deque

cards = deque(i for i in range(1,int(input())+1))
forsake = []
while len(cards) != 1:
    forsake.append(cards.popleft())
    cards.append(cards.popleft())
print(*forsake, cards[0])