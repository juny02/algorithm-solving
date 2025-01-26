import sys
from collections import deque

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# empty_spot : candidates list
def get_spots(matrix):
    empty_spots = deque()
    candidates = {}
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                empty_spots.append((i, j))
                candidates[(i, j)] = set(i for i in range(1, 10))
    return empty_spots, candidates

def test_candidate(x, y, i):
    if i in matrix[x]:
        return False
    
    for a in range(9):
        if matrix[a][y] == i:
            return False
        
    dxs = [ 2-x%3, 1-x%3, 0-x%3]
    dys = [ 2-y%3, 1-y%3, 0-y%3]
    for dx in dxs:
        for dy in dys:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny] == i:
                return False
    return True
        

def find_candidates(x, y):
    for i in list(candidates[(x, y)]):
        if not test_candidate(x, y, i): # 값 가능하지않으면
            candidates[(x, y)].remove(i)


empty_spots, candidates = get_spots(matrix)
while empty_spots:
    x, y = empty_spots.popleft()
    find_candidates(x, y)
    if len(candidates[(x, y)]) == 1:
        matrix[x][y] = next(iter(candidates[(x, y)]))
    else:
        empty_spots.append((x,y))

for row in matrix:
    print(*row)

