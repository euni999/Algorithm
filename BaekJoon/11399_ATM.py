n = int(input())

num = list(map(int, input().split()))
num.sort()

for i in range(1, n):
    num[i]  += num[i-1]

print(sum(num))



'''
배열을 오름차순으로 정렬
누적 시간 더하기
'''