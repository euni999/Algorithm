import sys

while True:
    try:
        jump = [int(x) for x in sys.stdin.readline().split()]
        move = max(jump[2] - jump[1], jump[1] - jump[0])
        print(move - 1)
    except:
        break
