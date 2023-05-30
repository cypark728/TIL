import heapq
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    m = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * 1000001
    for j in range(m):
        a, b = input().split()
        b = int(b)
        if a == "I":
            heapq.heappush(min_heap, (b, j))
            heapq.heappush(max_heap, (-b, j))
            visited[j] = True
        else:
            if b == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif b == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print("{} {}".format(-max_heap[0][0], min_heap[0][0]))
    else:
        print("EMPTY")
