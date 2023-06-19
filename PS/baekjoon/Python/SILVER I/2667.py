from collections import deque
n = int(input())
field = []
for i in range(n):
    field.append(list(map(int, input())))

result = 0
result_list = []
temp = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([])

for a in range(n):
    for b in range(n):
        if field[a][b] == 1:
            field[a][b] = -1
            temp = 1
            result += 1
            q.append((a, b))
            while q:
                y, x = q.popleft()
                for k in range(4):
                    cx = x + dx[k]
                    cy = y + dy[k]
                    if -1 < cx < n and -1 < cy < n and field[cy][cx] == 1:
                        temp += 1
                        field[cy][cx] = -1
                        q.append((cy, cx))
            result_list.append(temp)

print(result)
result_list = sorted(result_list)
for _ in result_list:
    print(_)
