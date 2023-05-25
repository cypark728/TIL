from dataclasses import dataclass


@dataclass
class meet:
    x: int = None
    y: int = None


n = int(input())
graph = []
result = 0
standard_x = 0

for i in range(n):
    x, y = map(int, input().split())
    temp = meet()
    temp.x = x
    temp.y = y
    graph.append(temp)

graph = sorted(graph, key=lambda meet: (meet.y, meet.x))

for j in graph:
    if j.x >= standard_x:
        result += 1
        standard_x = j.y

print(result)
