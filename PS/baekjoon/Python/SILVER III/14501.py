N = int(input())

T = []
P = []
K = [0 for i in range(N + 1)]

for i in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

for i in range(N):
    for j in range(i + T[i], N + 1):
        if K[j] < K[i] + P[i]:
            K[j] = K[i] + P[i]

print(K[-1])

