from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


def bfs(graph):
    queue = deque([(0, 0)])
    visited_set = set((0, 0))

    while queue:
        i, j = queue.popleft()

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and (ni, nj) not in visited_set:
                queue.append((ni, nj))
                visited_set.add((ni, nj))


"""
최단거리 -> bfs
자기주위꺼 
일단포기
"""
