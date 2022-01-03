import sys

n = int(sys.stdin.readline().rstrip())
work = []
scores = [0]*1000

for i in range(n):
    day, score = map(int, sys.stdin.readline().split())
    work.append([day, score])

work.sort(reverse=True, key=lambda x: (x[1]))

for i in range(n):
    for j in range(work[i][0]-1, -1, -1):
        if scores[j] == 0:
            scores[j] = work[i][1]
            break

print(sum(scores))


'''
1. 점수가 큰 것
2. 마감에 가까운 것
'''