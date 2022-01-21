N = int(input())
dp = list(map(int, input().split()))
dp.insert(0, 0)
money = [0] * (N + 1)
money[1] = dp[1]
money[2] = max(dp[2], dp[1] * 2)

for i in range(3, N + 1):
    money[i] = dp[i]
    for j in range(1, i // 2 + 1):
        money[i] = max(money[i], money[j] + money[i - j])
print(money[N])

# N = int(input())
# dp = list(map(int, input().split()))
# dp.insert(0, 0)
# money = 0
# for i in range(1, N+1):
#     money = max(money, dp[i]+dp[N-i], dp[i]*(N//i))
# print(money)



