n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
t = []

def dfs(start):
    if len(t) == m:
        result = " ".join(map(str, t))
        print(result)
        return

    before_number = 0
    for i in range(start, n):
        if s[i] != before_number:
            t.append(s[i])
            before_number = s[i]
            dfs(i)
            t.pop()

dfs(0)
