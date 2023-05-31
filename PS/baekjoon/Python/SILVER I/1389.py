from collections import deque

n, m = map(int, input().split())
graph = [[]for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque([start])
    visited = [0] * (n + 1)
    result = 0
    while q:
        temp = q.popleft()
        for i in graph[temp]:
            if visited[i] == 0:
                visited[i] = visited[temp] + 1
                q.append(i)
    for j in range(1, n + 1):
        result = result + visited[j]
    result -= visited[start]
    return result


max_result = bfs(1)
answer = 1
for k in range(2, n + 1):
    temp = bfs(k)
    if max_result > temp:
        max_result = temp
        answer = k
print(answer)
