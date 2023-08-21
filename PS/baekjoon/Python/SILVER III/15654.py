N, M = map(int, input().split())
s = list(map(int, input().split()))
s = sorted(s)
k = []


def dfs():
    if len(k) == M:
        result = " ".join(map(str, k))
        print(result)
        return
    
    for i in s:
        if i not in k:
            k.append(i)
            dfs()
            k.pop()

dfs()
