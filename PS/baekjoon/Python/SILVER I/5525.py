n = int(input())
m = int(input())
s = input()

result, count, index = 0, 0, 0

while index < m - 1:
    if s[index : index + 3] == "IOI":
        index += 2
        count += 1
        if count == n:
            result += 1
            count -= 1
    else:
        count = 0
        index += 1

print(result)
