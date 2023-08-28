import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
t = [[] for i in range(n + 1)]
s = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    t[a].append(b)
    t[b].append(a)


def dfs(start):
    for i in t[start]:
        if (s[i] == 0):
            s[i] = start
            dfs(i)


dfs(1)
for k in range(2, n + 1):
    print(s[k])
