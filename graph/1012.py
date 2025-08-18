import sys
sys.setrecursionlimit(10**6)

T = int(input())


def dfs(graph, v, visited):
    visited.add(v)
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        x, y = v
        if 0<=x+dx<N and 0<=y+dy<M and graph[x+dx][y+dy]==1 and (x+dx, y+dy) not in visited:
            new_v = (x+dx, y+dy)
            dfs(graph, new_v, visited)

answers = []
for _ in range(T):
    M, N, K = list(map(int, input().split()))
    graph = [[0]*M for _ in range(N)]
    visited = set([])
    coords = []
    count = 0
    for _ in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1
        coords.append((n, m))
    
    for coord in coords:
        if coord not in visited:
            dfs(graph, coord, visited)
            count += 1
    answers.append(count)

for i in answers:
    print(i)

    """
    허얼 ; 어이없음
    걍 저 coords에 잇는지 여부로 확인해도되는데 굳이 그래프를.. OTL
    """
    
    """
    개선한다면
    - visited를 따로 만들지말고 graph를 0으로 바꾼다.
    - 그리고 배열로안만들고 그냥 두 for문으로 해도 됨. 메모리만더씀. ㅂㄹ 다르지도안음..
    -  if graph[y][x] == 1: 이면 bfs /dfs 하는고임
    """