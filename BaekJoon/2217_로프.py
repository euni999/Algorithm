import sys
n = int(sys.stdin.readline().strip())

rope = []
weight = 0
for _ in range(n):
    rope.append(int(sys.stdin.readline().strip()))
rope.sort()

for i in range(n):
    weight = max(weight, rope[i] * (n - i))
print(weight)
