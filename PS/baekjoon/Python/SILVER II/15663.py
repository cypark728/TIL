n, m = map(int, input().split())
s = list(map(int, input().split()))
s = sorted(s)
visited = [0] * n
temp = []


def dfs():
    if len(temp) == m:
        result = " ".join(map(str, temp))
        print(result)
        return

    before_number = 0
    for i in range(n):
        if visited[i] == 0 and before_number != s[i]:
            before_number = s[i]
            visited[i] = 1
            temp.append(s[i])
            dfs()
            temp.pop()
            visited[i] = 0


dfs()
