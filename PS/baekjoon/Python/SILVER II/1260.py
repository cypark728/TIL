from collections import deque
n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
for j in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for k in range(0, n + 1):
    graph[k] = sorted(graph[k])


def dfs(v):  # dfs
    visited[v] = 1
    print(v, end=" ")
    for i in graph[v]:
        if(visited[i] == 0):
            dfs(i)


dfs(v)
print()

# bfs
visited = [0] * (n + 1)
Q = deque([v])
while Q:
    now = Q.popleft()
    visited[now] = 1
    print(now, end=" ")
    for i in graph[now]:
        if(visited[i] == 0):
            Q.append(i)
            visited[i] = 1

