import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

graph = {key: sorted(value) for key, value in graph.items()}

# dfs

def dfs(graph, visited, v):
    print(v, end=' ')
    visited[v-1] = True

    for i in graph[v]:
        if not visited[i-1]:
            dfs(graph, visited, i)
    
# bfs
def bfs(graph, visited, start):
    queue = deque([start])
    visited[start-1] = True

    while queue:
        v = queue.popleft()
        visited[v-1] = True
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i-1]:
                queue.append(i)
                visited[i-1] = True


dfs(graph, [False]*n, v)
print()
bfs(graph, [False]*n, v)
print()