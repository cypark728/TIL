n, m = map(int, input().split())
tree = list(map(int, input().split()))

max_t = max(tree)
min_t = 1
result = 0

while min_t <= max_t:
    temp = int((min_t + max_t) // 2)
    save = 0
    for i in tree:
        if temp < i:
            save = save + (i - temp)

    if save >= m:
        min_t = temp + 1
    else:
        max_t = temp - 1

print(max_t)
