import heapq
import sys
input = sys.stdin.readline
MAX = 1000000

n = int(input())
m = int(input())
field = [[]for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    field[a].append((b, c))
start, finish = map(int, input().split())


def dijkstra(graph, start):
    distances = [int(1e9)] * (n + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [start, distances[start]])

    while queue:
        node, dist = heapq.heappop(queue)

        if dist > distances[node]:
            continue

        for cur_node, cur_dist in field[node]:
            distance = dist + cur_dist
            if distances[cur_node] > distance:
                distances[cur_node] = distance
                heapq.heappush(queue, [cur_node, (cur_dist + dist)])
    return distances


result = dijkstra(field, start)
print(result[finish])
