from collections import deque

n, m = map(int, input().split())
filed = []

for i in range(n):
    temp = list(map(int, input().split()))
    filed.append(temp)

q = deque([])
for j in range(n):
    for k in range(m):
        if filed[j][k] == 1:
            filed[j][k] = -1
        elif filed[j][k] == 2:
            filed[j][k] = 0
            q.append((j, k))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    y, x = q.popleft()
    for p in range(4):
        cx = x + dx[p]
        cy = y + dy[p]
        if -1 < cx < m and -1 < cy < n and filed[cy][cx] == -1:
            filed[cy][cx] = filed[y][x] + 1
            q.append((cy, cx))
for g in range(n):
    for h in range(m):
        print(filed[g][h], end = " ")
    print()
