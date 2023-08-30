from collections import deque

a, b = map(int, input().split())
s = deque([a])
depth = deque([1])


while True:
    if not s:
        break
    temp = s.popleft()
    depth_temp = depth.popleft()
    if temp == b:
        print(depth_temp)
        break
    elif temp < b:
        s.append(temp * 2)
        s.append(temp * 10 + 1)
        depth.append(depth_temp + 1)
        depth.append(depth_temp + 1)

if not s:
    print(-1)
