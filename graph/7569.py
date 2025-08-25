from collections import deque

M, N, H = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# HxNxM [z][y][x]


def bfs(graph, queue: deque):
    global unripen
    global sol
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while queue:
        x, y, z = queue.popleft()
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nx, ny, nz))
                unripen -= 1
                sol = max(graph[nz][ny][nx], sol)


queue = deque([])
unripen = 0
sol = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[z][y][x] == 1:
                queue.append((x, y, z))
            elif tomatos[z][y][x] == 0:
                unripen += 1
bfs(tomatos, queue)
if unripen != 0:
    print(-1)
elif sol == 0:
    print(0)
else:
    print(sol-1)
