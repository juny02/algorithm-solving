import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(N)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = set()


def dfs(visited: set, v, graph):
    visited.add(v)

    for i in graph[v]:
        if not (i in visited):
            dfs(visited, i, graph)


count = 0
for node in range(N):
    if node not in visited:
        dfs(visited, node, graph)
        count += 1

print(count)