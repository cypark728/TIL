import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a = []
result = 0
count = 1
check = k

for i in range(0, n):
    a.append(int(input().rstrip()))
    
for j in range(n - 1, -1, -1):
    if (check // a[j]) > 0:
        result = (check // a[j]) + result
        check = check % a[j]

print(result)