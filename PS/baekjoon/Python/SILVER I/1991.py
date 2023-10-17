# https://www.acmicpc.net/problem/1991
from collections import deque


def pre():
    result = q.popleft()
    preorder.append(result)
    if dictonary[result][0] != '.':
        q.append(dictonary[result][0])
        pre()

    if dictonary[result][1] != '.':
        q.append(dictonary[result][1])
        pre()


def inor(root):
    if root != '.':
        inor(dictonary[root][0])
        print(root, end='')
        inor(dictonary[root][1])


def postor(root):
    if root != '.':
        postor(dictonary[root][0])
        postor(dictonary[root][1])
        print(root, end='')


preorder = []
inorder = []
postorder = []

dictonary = {}

n = int(input())
for i in range(n):
    temp = list(map(str, input().split()))
    dictonary[temp[0]] = temp[1:3]


q = deque(['A'])
pre()
for i in preorder:
    print(i, end='')
print()
inor('A')
print()
postor('A')
