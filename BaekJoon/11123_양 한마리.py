import sys
sys.setrecursionlimit(300000)


def dfs(y, x):
    graph[y][x] = '.'
    for dy, dx in d:
        Y, X = y + dy, x + dx
        if (0 <= Y < H) and (0 <= X < W) and graph[Y][X] == '#':
            dfs(Y, X)


N = int(input())
for _ in range(N):
    H, W = map(int, input().split())
    graph = [list(input()) for _ in range(H)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':
                dfs(i, j)
                result += 1
    print(result)
