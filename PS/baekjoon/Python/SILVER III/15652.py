N, M = map(int, input().split())
s = []

def dfs(start):
    if len(s) == M:
        result = " ".join(map(str, s))
        print(result)
        return
    
    for i in range(start, N + 1):
        s.append(i)
        dfs(i)
        s.pop()
        
dfs(1)

