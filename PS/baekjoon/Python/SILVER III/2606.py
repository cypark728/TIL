from collections import deque
n = int(input())
m = int(input())

visited = [0] * (n + 1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited[1] = 1
Q = deque([1])
while Q:
    c = Q.popleft()
    for i in graph[c]:
        if visited[i] == 0:
            visited[i] = 1
            Q.append(i)

print(sum(visited) - 1)
