n = int(input())

a = [0] * 11
a[0] = 1
a[1] = 2
a[2] = 4

def make(k):
    if k < 4:
        print(a[k - 1])
    else:
        for i in range(3, k):
            a[i] = a[i - 3] + a[i - 2] + a[i - 1]
        print(a[k - 1])
    
for i in range(n):
    temp = int(input())
    make(temp)