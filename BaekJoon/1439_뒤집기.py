S = list(input())
cnt = 1
for i in range(1, len(S)):
    if (S[i] != S[i - 1]):
        cnt += 1

result = int(cnt / 2)
print(result)
