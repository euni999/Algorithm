S = int(input())
cnt = 0
result = 0

for i in range(1, S+1): # 1부터 자연수 S까지
    cnt += i 
    result += 1
    if (cnt == S): break
    if ((S - cnt) <= i): # 남은 값이 자연수보다 작거나 같으면
        break

print(result)