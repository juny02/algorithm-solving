from collections import deque


def bfs(graph, v):
    visited = [[-1]*X for _ in range(Y)]
    visited[v[1]][v[0]] = 0
    queue = deque([v])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_len = 0
    while queue:
        v = queue.popleft()
        for dx, dy in directions:
            nx, ny = v[0]+dx, v[1]+dy
            if 0<=nx<X and 0<=ny<Y and graph[ny][nx] == 'L' and visited[ny][nx]==-1: # 아직 방문 안햇으면 방문
                visited[ny][nx] = visited[v[1]][v[0]]+1
                max_len = max(visited[ny][nx], max_len)
                queue.append((nx, ny))
    return max_len
                
        

Y, X = map(int, input().split())
graph = [list(input()) for _ in range(Y)]

# graph[0][1]=0
# print(bfs(graph, (1, 0)))

sol = 0
for x in range(X):
    for y in range(Y):
        if graph[y][x] == 'L':
            sol = max((bfs(graph, (x, y))), sol)
print(sol)


"""
그래프를 계속 딥카피 하는거보다 bfs를 할때마다 visited 배열을 만드는게 더 조음
ㄷㄷ모든 점에 대해 bfs하는게 맞앗다니
최단거리는 무조건 bfs! DFS로는 최단거리를 절대 보장할 수 업당
"""