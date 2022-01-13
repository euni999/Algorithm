import sys

cnt = 0
end = [0, 0, 0]
while True:
    camp = [int(x) for x in sys.stdin.readline().split()]
    if camp != end:
        day = camp[0] * (camp[2] // camp[1])
        cnt += 1
        if camp[0] <= (camp[2] % camp[1]):
            day += camp[0]
        else:
            day += (camp[2] % camp[1])
        s = "Case {}: {}".format(cnt, day)
        print(s)
    else:
        break
