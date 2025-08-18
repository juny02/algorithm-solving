from collections import deque

T = int(input())
arrs = []
for _ in range(T):
    N = int(input())
    arr = [0]
    arr += list(map(int, input().split()))
    arrs.append(arr)

def sol(arr):
    visited = set([])
    count = 0
    for i in range(1, len(arr)):
        if i not in visited:
            dfs(arr, i, visited)
            count += 1
    return count


def dfs(graph, v, visited):
    visited.add(v)
    
    i = graph[v]
    if i not in visited:
        dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited.add(v)
    while queue:
        v = queue.popleft()
        i = graph[v]
        if i not in visited:
            queue.append(i)
            visited.add(i)
    


for arr in arrs:
    print(sol(arr))