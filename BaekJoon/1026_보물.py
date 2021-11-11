n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

s = 0

for i in range(n):
    s += A[i] * B.pop(B.index(max(B)))

print(s)