n = int(input())
temp = list(map(int, input().split()))
sor_temp = sorted(temp)
idx = 0
check_dict = {}
for i in sor_temp:
    if idx == 0:
        last = i
        check_dict[i] = idx
        idx += 1
    else:
        if last != i:
            check_dict[i] = idx
            idx += 1
            last = i

for j in temp:
    print(check_dict[j], end = " ")