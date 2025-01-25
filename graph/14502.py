import sys
from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
infected_coordinates = set()
wall_candidates = set()
for x in range(N):
    for y in range(M):
        if matrix[x][y] == 2:
            infected_coordinates.add((x, y))
        if matrix[x][y] == 0:
            wall_candidates.add((x, y))


answers = []
def bfs(matrix, x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny]==0:
                queue.append((nx, ny))
                matrix[nx][ny]=2

def get_safe_area(infected_coordinates, matrix):
    for x, y in infected_coordinates:
        bfs(matrix, x, y)
    return sum(row.count(0) for row in matrix)


def print_mat(matrix):
    for row in matrix:
        print(row)
    print()

for wall_coordinates in combinations(wall_candidates, 3):
    copied_matrix = copy.deepcopy(matrix)
    for x, y in wall_coordinates:
        copied_matrix[x][y]=1
    # print_mat(copied_matrix)
    answers.append(get_safe_area(infected_coordinates, copied_matrix))
    # print_mat(copied_matrix)
print(max(answers))
