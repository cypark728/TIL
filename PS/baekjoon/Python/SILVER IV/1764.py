import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = {}
b = []

for i in range(0, n):
    temp = input().rstrip()
    a[temp] = i
    
    
for j in range(0, m):
    temp = input().rstrip()
    if temp in a:
        b.append(temp)
        
b.sort()
print(len(b))
for k in range(0, len(b)):
    print(b[k])