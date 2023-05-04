def cut(x, y, size):
    global m_one, zero, one
    x = int(x)
    y = int(y)
    size = int(size)
    curr = field[y][x]
    if size != 1:
        for i in range(0, size):
            for j in range(0, size):
                if curr != field[y +i][x + j]:
                    size = size / 3
                    cut(x, y, size)
                    cut(x + size, y, size)
                    cut(x + size*2, y, size)
                    cut(x, y + size, size)
                    cut(x + size, y + size, size)
                    cut(x + size*2, y + size, size)
                    cut(x, y + size*2, size)
                    cut(x + size, y + size*2, size)
                    cut(x + size*2, y + size*2, size)
                    return 0

    if curr == -1:
        m_one += 1
    elif curr == 0:
        zero += 1
    elif curr == 1:
        one += 1
    return 0

n = int(input())
field = []
m_one = 0
zero = 0
one = 0
       
    
for i in range(n):
    temp = list(map(int, input().split()))
    field.append(temp)

cut(0, 0, n)
print(m_one)
print(zero)
print(one)
