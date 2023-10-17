n = int(input())
field = []
for i in range(n):
    field.append(list(map(int, input().split())))

for j in range(1, n):
    for k in range(0, j + 1):
        if k == 0:
            field[j][k] += field[j - 1][0]
        elif k == j:
            field[j][k] += field[j - 1][j - 1]
        else:
            field[j][k] += max(field[j - 1][k - 1], field[j - 1][k])
            
print(max(field[n - 1]))
