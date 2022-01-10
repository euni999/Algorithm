N, M = map(int, input().split())
m = [1, M]
J = int(input())
move = 0
for _ in range(J):
    apple = int(input())
    if (m[0] <= apple <= m[1]):
        pass
    else:
        if (m[1] < apple):
            move += apple - m[1]
            m[0] += apple - m[1]
            m[1] = apple

        else:
            move += m[0] - apple
            m[1] -= m[0] - apple
            m[0] = apple

print(move)