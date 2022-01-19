T = int(input())

def answer(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return answer(num-1) + answer(num-2) + answer(num-3)

for _ in range(T):
    n = int(input())
    print(answer(n))



