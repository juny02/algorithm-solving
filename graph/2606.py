import sys
from collections import deque

N = int(input())
M = int(input())
visited = [False]* N
graph = {i:[] for i in range(N)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

queue = deque([0])
visited[0] = True
ans = 0
while queue:
    v = queue.popleft()
    ans += 1
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True

print(ans-1)