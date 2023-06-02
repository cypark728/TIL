from collections import deque

m, n, h = map(int, input().split())
filed = []
filed_temp = []
for i in range(h):
    for j in range(n):
        temp = list(map(int, input().split()))
        filed_temp.append(temp)
    filed.append(filed_temp)
    filed_temp = []

q = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if filed[i][j][k] == 1:
                q.append((i, j, k))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

while q:
    xh, y, x = q.popleft()
    for p in range(6):
        cx = x + dx[p]
        cy = y + dy[p]
        ch = xh + dh[p]
        if -1<cx<m and -1<cy<n and -1<ch<h and filed[ch][cy][cx] == 0:
            filed[ch][cy][cx] = filed[xh][y][x] + 1
            q.append((ch, cy, cx))

filed_max = -2
zero_count = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if filed[i][j][k] == 0:
                zero_count += 1
            elif filed[i][j][k] > filed_max:
                filed_max = filed[i][j][k]
if zero_count > 0:
    print(-1)
else:
    print(filed_max - 1)


