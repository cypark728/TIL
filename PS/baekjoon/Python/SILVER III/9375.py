n = int(input())

for i in range(n):
    t = int(input())
    s = {}
    for j in range(t):
        a , b = input().split()
        if b not in s:
            s[b] = 1
        else:
            s[b] += 1
    
    result = 1
    for key in s:
        result = result * (s[key] + 1)
    print(result - 1)
