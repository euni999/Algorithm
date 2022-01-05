test = int(input())
for _ in range(test):
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()
    result = 0
    for i in range(2, n):
        result = max(result, abs(num[i] - num[i-2]))
    print(result)