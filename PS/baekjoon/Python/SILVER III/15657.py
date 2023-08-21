N, M = map(int, input().split())
s = list(map(int, input().split()))
s = sorted(s)
k = []


def dfs(start):
    if len(k) == M:
        result = " ".join(map(str, k))
        print(result)
        return

    for i in range(start, N):
        k.append(s[i])
        dfs(i)
        k.pop()


dfs(0)
