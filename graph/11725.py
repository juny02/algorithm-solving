import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited = [0]*(N+1)
visited[1] = 1

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            queue.append(i)

for i in visited[2:]:
    print(i)