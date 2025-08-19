from collections import deque


N = int(input())
graph = [list(input()) for _ in range(N)]

def bfs(graph, v, target, visited):
    queue = deque([v])
    x, y = v
    visited[y][x] = True
    
    while queue:
        v = queue.popleft()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            x, y = v
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and  graph[ny][nx] in target:
                visited[ny][nx] = True
                queue.append((nx, ny))

visited = [[False]*N for _ in range(N)]
count = 0
for x in range(N):
    for y in range(N):
        if not visited[y][x]: 
            bfs(graph, (x, y), graph[y][x], visited)
            count += 1
print(count, end=' ')

visited = [[False]*N for _ in range(N)]
count = 0
for x in range(N):
    for y in range(N):
        if not visited[y][x]: 
            if graph[y][x] in "RG":
                bfs(graph, (x, y), "RG", visited)
            else:
                bfs(graph, (x, y), "B", visited)
            count += 1
print(count)

