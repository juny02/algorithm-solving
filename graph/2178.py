from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


def bfs(graph):
    queue = deque([(0, 0)])
    while queue:
        i, j = queue.popleft()
        if i==N-1 and j == M-1:
            return graph[i][j] 
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and graph[ni][nj]==1:
                queue.append((ni, nj))
                graph[ni][nj]=graph[i][j]+1
                
print(bfs(graph))

