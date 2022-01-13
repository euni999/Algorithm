import sys
n = int(sys.stdin.readline())
for _ in range(n):
    N = int(sys.stdin.readline())
    money = 0
    max = 0
    stock = [int(x) for x in sys.stdin.readline().split()]
    for i in range(N-1, -1, -1):
        if stock[i] > max:
            max = stock[i]
        else:
            money += max - stock[i]
    print(money)

