import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))
s = [0]
for x in range(n):
    s.append(s[x] + a[x])

for i in range(m):
    j, k = map(int, input().split())
    print(s[k] - s[j - 1])