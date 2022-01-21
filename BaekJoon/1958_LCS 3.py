import sys

s1 = sys.stdin.readline()
s2 = sys.stdin.readline()
s3 = sys.stdin.readline()

x = len(s1) + 1
y = len(s2) + 1
z = len(s3) + 1

dp = [[[0] * z for _ in range(y)] for _ in range(x)]

for i in range(1, x):
    for j in range(1, y):
        for k in range(1, z):
            if s1[i-1] == s2[j-1] and s2[j-1] == s3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

result = -1

for i in range(x):
    for j in range(y):
        result = max(max(dp[i][j]), result)

print(result-1)


