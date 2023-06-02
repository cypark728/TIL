n = int(input())
filed = []

for _ in range(n):
    temp = list(map(int, input()))
    filed.append(temp)


def dfs(x, y, size):
    size = int(size)
    x = int(x)
    y = int(y)
    if size == 1:
        print(filed[y][x], end="")
    else:
        check = filed[y][x]
        for i in range(size):
            for j in range(size):
                if check != filed[y + i][x + j]:
                    check = -1
                    break
        if check == -1:
            print("(", end="")
            size = size / 2
            dfs(x, y, size)
            dfs(x + size, y, size)
            dfs(x, y + size, size)
            dfs(x + size, y + size, size)
            print(")", end="")
        else:
            print(check, end="")

dfs(0, 0, n)
