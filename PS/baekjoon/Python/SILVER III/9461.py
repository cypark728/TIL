t = int(input())

a = [1, 1, 1, 2, 2]

for i in range(t):
    temp = int(input())
    length = len(a)
    if temp < length:
        print(a[temp - 1])
    else:
        for j in range(length, temp):
            a.append(a[j - 1] + a[j - 5])
        print(a[temp - 1])