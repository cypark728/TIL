import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = {}

for i in range(1, n + 1):
    temp = input().rstrip()
    a[i] = temp
    a[temp] = i
    
for j in range(0, m):
    b = input().rstrip()
    if b.isdigit():
        print(a[int(b)])
    else:
        print(a[b])
print(m)
print(n)