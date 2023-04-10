n = int(input())
a = list(map(int, input().split()))
result = 0

a.sort()

for j in range(0, n):
    for k in range(0, j + 1):
        result = result + a[k]
        
print(result)