import sys
sys.setrecursionlimit(10 ** 7)

A, B = map(int, input().split())
cnt = 1
while B != A:
    if (B > A):
        if (B % 2 == 0):
            B //= 2
        elif (B % 10 == 1):
            B //= 10
        else:
            cnt = -1
            break
        cnt += 1
    if (B < A):
        cnt = -1
        break

print(cnt)
