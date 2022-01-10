num = int(input())
seat = input()
holder = 0
if (seat.find('LL') != -1):
    holder = 1
seat = seat.replace('LL', 'S')

holder += seat.count('S')
print(holder)

