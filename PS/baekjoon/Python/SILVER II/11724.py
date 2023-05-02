import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[]for i in range(N + 1)]
visited = [0] * (N + 1)
result = 0

def bfs(j):
    Q = deque([j])
    visited[j] = 1
    while Q:
        temp = Q.popleft()
        visited[temp] = 1
        for i in graph[temp]:
            if visited[i] == 0:
                visited[i] = 1;
                Q.append(i)

for i in range(0, M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for j in range(1, N + 1):
    if(visited[j] == 0):
        result += 1
        bfs(j)

print(result)
