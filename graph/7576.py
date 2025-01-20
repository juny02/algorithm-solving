import sys
from collections import deque
import copy

N, M = map(int, input().split())
matrix = []
for _ in range(M):
    matrix.append(list(map(int, sys.stdin.readline().split())))


def bfs(matrix, queue: deque):
    directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] == 0:
                queue.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1


# 1인 점들에 대해
ans = 0
queue = deque([])
for x in range(M):
    for y in range(N):
        if matrix[x][y] == 1:
            queue.append((x, y))

bfs(matrix, queue)
ans = 0
for i in matrix:
    if 0 in i:
        print(-1)
        exit(0)
    ans = max(ans, max(i))

print(ans-1)