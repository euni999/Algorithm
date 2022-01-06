test = int(input())

for _ in range(test):
    n = int(input())
    goal = list(input())
    robot = list(input())
    result = 0
    dif = []
    for i in range(n):
        if (goal[i] != robot[i]):
            dif.append(robot[i])
            
    result = max(dif.count('W'), dif.count('B'))
    print(result)
