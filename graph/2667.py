import sys
from collections import deque

N = int(input())
matrix = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]


# 방문 처리를 굳이 visited만들지 않고, matrix에서 한번에 0 으로 넣어준다
# 백터로 처리할 수 있도록 한다!


def bfs(matrix, x, y):
    queue = deque([(x, y)])
    matrix[x][y] = 0
    length = 0

    directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    while queue:
        x, y = queue.popleft()
        length += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0

    return length


lengths = []
count = 0
for i in range(0, N * N):
    r, c = int(i / N), i % N
    if matrix[r][c] == 1:
        lengths.append(bfs(matrix, r, c))
        count += 1

print(count)
for i in sorted(lengths):
    print(i)
