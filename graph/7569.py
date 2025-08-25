from collections import deque

M, N, H = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N * H)]


def bfs(graph, points, count):
    queue = deque([points])  # 리스트의 리스트
    visited = set(points)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    hop_directions = [(0, N), (0, -N)]
    while queue:
        add = []
        visited |= set(add)
        for x, y in queue.popleft():
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (y//N)*N <= ny < (y//N+1)*N and 0<=ny<N*H and 0 <= nx < M and (nx, ny) not in visited and graph[ny][nx] >= 0:
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = graph[y][x] + 1
                        add.append((nx, ny))
                    else:
                        if graph[y][x] + 1 < graph[ny][nx]:
                            add.append((nx, ny))
                    count = max(graph[ny][nx], count)
            for dx, dy in hop_directions:
                nx, ny = x + dx, y + dy
                if 0 <= ny < H*N and 0 <= nx < M and (nx, ny) not in visited and graph[ny][nx] >= 0:
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = graph[y][x] + 1
                        add.append((nx, ny))
                    else:
                        if graph[y][x] + 1 < graph[ny][nx]:
                            add.append((nx, ny))
                    count = max(graph[ny][nx], count)
        if len(add) != 0:
            queue.append(list(set(add)))
    return count


count = 0
points = []
for x in range(M):
    for y in range(N*H):
        if tomatos[y][x] == 1:
            points.append((x, y))
count = bfs(tomatos, points, count)
for tomato in tomatos:
    if 0 in tomato:
        print(-1)
        exit()
if count == 0:
    print(0)
else:
    print(count - 1)

    """
    다시방문 안한데를 방문하ㅣㄱ 위해 visited를 따로 둠 graph에 갱신하는거로못하고
    """
