import sys
input = sys.stdin.readline

count = int(input())

s = set()

for i in range(0, count):
    a = list(input().split())
    if(len(a) == 1):
        x = a[0]
    else:
        x, y = a[0], int(a[1])
        
    if(x == "add"):
        s.add(y)
    elif(x == "remove"):
        s.discard(y)
    elif(x == "check"):
        if(y in s):
            print("1")
        else:
            print("0")
    elif(x == "toggle"):
        if(y in s):
            s.discard(y)
        else:
            s.add(y)
    elif(x == "all"):
        s = set([i for i in range(1, 21)])
    elif(x == "empty"):
        s = set()