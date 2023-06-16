from collections import deque

n, m = map(int, input().split())
field = []

for i in range(n):
    field.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([])
q.append((0, 0))  # y, x

while q:
    y, x = q.popleft()
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if -1 < cx < m and -1 < cy < n and field[cy][cx] == 1:
            field[cy][cx] = field[y][x] + 1
            q.append((cy, cx))

print(field[n - 1][m - 1])

