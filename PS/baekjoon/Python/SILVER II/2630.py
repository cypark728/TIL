n = int(input())
paper = []

for i in range(n):
    temp = list(map(int, input().split()))
    paper.append(temp)

blue = 0
white = 0
def cut(x, y, size):
    global blue
    global white
    temp = paper[y][x]
    if size == 1:
        if temp == 1:
            blue += 1
        else:
            white += 1
    else:
        for i in range(y, y + size):
            for j in range(x, x + size):
                if paper[i][j] != temp:
                    size = size / 2
                    size = int(size)
                    cut(x, y, size)
                    cut(x, y + size, size)
                    cut(x + size, y, size)
                    cut(x + size, y + size, size)
                    return
        if temp == 1:
            blue += 1
        else:
            white += 1
    return

cut(0, 0, n)
print(white)
print(blue)