n = int(input())

a = [1, 3]

if n < 3:
    print(a[n - 1])
else:
    for i in range(len(a), n):
        a.append(a[i - 1] + (a[i - 2] * 2))
    print(a[n - 1] % 10007)