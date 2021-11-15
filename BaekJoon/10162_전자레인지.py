n = int(input())

time = [300, 60, 10]
num = []

for i in range(len(time)):
    num.append(n // time[i])
    n = n % time[i]

if n == 0:
    for i in range(len(num)):
        print(num[i])
else:
    print("-1")


