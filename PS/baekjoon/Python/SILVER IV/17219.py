import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = {}

for i in range(0, a):
    temp1, temp2 = input().split()
    c[temp1] = temp2

for j in range(0, b):
    temp = input().rstrip()
    print(c[temp])