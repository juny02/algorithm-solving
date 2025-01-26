import sys
from collections import deque

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# empty_spot : candidates list
def get_spots(matrix):
    empty_spots = []
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                empty_spots.append((i, j))
    return empty_spots

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
        

# def find_candidates(x, y):
#     for i in list(candidates[(x, y)]):
#         if not test_candidate(x, y, i): # 값 가능하지않으면
#             candidates[(x, y)].remove(i)


def fill_number(count, empty_spots): # count라기보단 idx! 몇번인덱스 까지 채웠는지!!
    if count == len(empty_spots):
        for row in matrix:
            print(*row)
        exit()
    x, y = empty_spots[count]
    for i in range(1, 10):
        if test_candidate(x, y, i):
            matrix[x][y] = i
            fill_number(count+1,empty_spots)
            matrix[x][y] = 0
        


empty_spots = get_spots(matrix)
fill_number(0, empty_spots)


'''
난 큐로하는 방식을했는데 시간초과가 뜸

이것보다 백트래킹을쓰면 일단 가능하면 넣고 실패하면 끝내
성공하면쭉쭉가는거지!!


글고 경우가 여러가지인 경우 -> return하면 계속하니가 exit 해줘야함!!
'''