from collections import deque

m, n = map(int, input().split())
filed = []
for i in range(n):
    filed.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    q = deque([])
    for i in range(n):
        for j in range(m):
            if filed[i][j] == 1:
                q.append((j, i))

    while q:
        x, y = q.popleft()
        for k in range(4):
            cx = x + dx[k]
            cy = y + dy[k]
            if -1 < cx < m and -1 < cy < n and filed[cy][cx] == 0:
                filed[cy][cx] = filed[y][x] + 1
                q.append((cx, cy))


bfs()
zero_count = 0
t_max = 0
for i in range(n):
    for j in range(m):
        if filed[i][j] == 0:
            zero_count += 1
            break
        elif filed[i][j] > t_max:
            t_max = filed[i][j]

if zero_count > 0:
    print(-1)
else:
    print(t_max - 1)