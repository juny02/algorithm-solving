import sys
from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0  # global 변수 활용!


def createWall(matrix, count):
    if count == 3:
        bfs(matrix)
        return

    for x in range(N):
        for y in range(M):
            if matrix[x][y] == 0:
                matrix[x][y] = 1
                createWall(matrix, count + 1)
                matrix[x][y] = 0


def bfs(origin_matrix):
    global answer
    queue = deque()
    matrix = copy.deepcopy(origin_matrix)
    # 2인 점들 넣기
    for x in range(N):
        for y in range(M):
            if matrix[x][y] == 2:
                queue.append((x, y))
    #  bfs
    while queue:
        x, y = queue.popleft()
        directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                queue.append((nx, ny))
                matrix[nx][ny] = 2
    result = sum(row.count(0) for row in matrix)
    answer = max(result, answer)


createWall(matrix, 0)
print(answer)


"""
bfs활용
-> count하기
!! 중요한점 !! 미리 queue에 infected인 애들을 넣어둔다!

벽세우기 -> 완전탐색
-> 이때 백트래킹 - 최대한 후보를 줄이도록 한다


"""
