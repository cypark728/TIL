from collections import deque

n, m = map(int, input().split())

filed = []
for i in range(n):
    temp = input()
    filed.append([])
    for b in range(m):
        filed[i].append(temp[b])

q = deque([])
for j in range(n):
    for k in range(m):
        if filed[j][k] == 'I':
            q.append((j, k)) # y, x

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

while q:
    y, x = q.popleft()
    for p in range(4):
        cx = x + dx[p]
        cy = y + dy[p]
        if -1 < cx < m and -1 < cy < n:
            if filed[cy][cx] == 'O':
                filed[cy][cx] = 'I'
                q.append((cy, cx))
            elif filed[cy][cx] == 'P':
                filed[cy][cx] = 'I'
                result += 1
                q.append((cy, cx))

if result == 0:
    print("TT")
else:
    print(result)
