n, y, x = map(int, input().split())
result = 0

while n != 0:
    if n == 1:
        if x == 0 and y == 0:
            print(result)
        elif x == 1 and y == 0:
            print(result + 1)
        elif x == 0 and y == 1:
            print(result + 2)
        elif x == 1 and y == 1:
            print(result + 3)
        n -= 1
    else:
        n -= 1
        if 2 ** n <= x and 2 ** n <= y:
            result = result + ((4 ** n) * 3)
            x = x - 2 ** n
            y = y - 2 ** n
        elif 2 ** n <= x and 2 ** n > y:
            result = result + 4 ** n
            x = x - 2 ** n
        elif 2 ** n > x and 2 ** n <= y:
            result = result + ((4 ** n) * 2)
            y = y - 2 ** n

