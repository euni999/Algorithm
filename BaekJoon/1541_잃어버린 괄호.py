import re

Str = input()
Str = re.findall('-?\d+', Str)
Str_num = [int(i) for i in Str]
cnt = 0
idx = len(Str_num)-1

for i in range(idx):
    if (Str_num[i] < 0):
        if (Str_num[i+1] > 0) :
            Str_num[i+1] = -(abs(Str_num[i]) + Str_num[i+1])
        else:
            cnt += Str_num[i]
    else:
        cnt += Str_num[i]

if ((Str_num[idx]>0) & (Str_num[idx-1] < 0)):
    cnt += -(abs(Str_num[idx]) + Str_num[idx-1])
else:
    cnt += Str_num[idx]

print(cnt)