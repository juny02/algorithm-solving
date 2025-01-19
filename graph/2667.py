import sys
from collections import deque

N = int(input())
matrix = []
visited = [[False]*N for _ in range(N)]

for _ in range(N):
    row = sys.stdin.readline().strip()
    matrix.append(row)



def bfs(matrix, visited, r,c) -> int:
    queue = deque([(r,c)])
    visited[r][c] = True
    length = 0

    while queue:
        r, c = queue.popleft()
        length += 1

        if c>0 and matrix[r][c-1]=='1' and not visited[r][c-1]:
            queue.append((r,c-1))
            visited[r][c-1] = True
        if c<N-1 and matrix[r][c+1] == '1' and not visited[r][c+1]:
            queue.append((r,c+1))
            visited[r][c+1] = True
        if r>0 and matrix[r-1][c] == '1'and not visited[r-1][c]:
            queue.append((r-1,c))
            visited[r-1][c] = True
        if r<N-1 and matrix[r+1][c] =='1'and not visited[r+1][c]:
            queue.append((r+1,c))
            visited[r+1][c] = True

    return length

lengths = []
count = 0
for i in range(0, N*N):
    r, c = int(i/N), i%N
    if matrix[r][c] == '1' and not visited[r][c]:
        lengths.append(bfs(matrix, visited, r,c))
        count += 1

print(count)
for i in sorted(lengths):
    print(i)

