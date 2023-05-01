import sys
input = sys.stdin.readline
sys.setrecursionlimit(2600)

T = int(input())
for i in range(0, T):
    M, N, K = map(int, input().split())
    field = [[0 for j in range(M)] for i in range(N)]
    visited = [[0 for j in range(M)] for i in range(N)]
    result = 0
    for j in range(0, K):
        a, b = map(int, input().split())
        field[b][a] = 1

    def dfs(y, x):
        visited[y][x] = 1
        if(y > 0 and field[y - 1][x] == 1 and visited[y - 1][x] == 0):
            dfs(y - 1, x)
        if(x > 0 and field[y][x - 1] == 1 and visited[y][x - 1] == 0):
            dfs(y, x - 1)
        if(y < N - 1 and field[y + 1][x] == 1 and visited[y + 1][x] == 0):
            dfs(y + 1, x)
        if(x < M - 1 and field[y][x + 1] == 1 and visited[y][x + 1] == 0):
            dfs(y, x + 1)

    for y in range(0, N):
        for x in range(0, M):
            if(field[y][x] == 1 and visited[y][x] == 0):
                result += 1
                dfs(y, x)

    print(result)
