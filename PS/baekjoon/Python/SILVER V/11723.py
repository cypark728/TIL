count = int(input())

s = set()

for i in range(0, count):
    a = list(input().split())
    if(a[0] == "add"):
        s.add(int(a[1]))
    elif(a[0] == "remove"):
        s.discard(int(a[1]))
    elif(a[0] == "check"):
        if(int(a[1]) in s):
            print("1")
        else:
            print("0")
    elif(a[0] == "toggle"):
        if(int(a[1]) in s):
            s.discard(int(a[1]))
        else:
            s.add(int(a[1]))
    elif(a[0] == "all"):
        s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif(a[0] == "empty"):
        s = set()