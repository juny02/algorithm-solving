import sys

matrix = [list(map(int, sys.stdin.readline().split()))for _ in range(10)]
spots = []
for i in range(10):
    for j in range(10):
        if matrix[i][j] == 1:
            spots.append((i, j))

def fill(ox, oy, p):
    for i in range(p):
        for j in range(p):
            x, y = ox+i, oy+j
            matrix[x][y] = 0

def remove(ox, oy, p):
    for i in range(p):
        for j in range(p):
            x, y = ox+i, oy+j
            matrix[x][y] = 1

def fill_possible(ox, oy, p):
    if available[p] <= 0:
        return False
    for i in range(p):
        for j in range(p):
            x, y = ox+i, oy+j
            if 0>x or x>= 10 or 0>y or y>=10 or matrix[x][y] == 0:
                return False
    return True



answer = 26

def fill_paper(idx, count):
    global answer
    global matrix

    if idx == len(spots):
        left = sum(available.values())
        answer = min(answer, 25-left)
        return
    
    if count >= answer:
        return

    x, y = spots[idx]
    if matrix[x][y] == 1:
        for p in range(5,0, -1):
            if fill_possible(x, y, p):
                fill(x, y, p)
                available[p] -= 1
                fill_paper(idx+1, count+1)
                remove(x, y, p)
                available[p] += 1
    else:
        fill_paper(idx+1, count)

answers = []
available = {i:5 for i in range(1, 6)}
fill_paper(0, 0)
if answer == 26 :
    print(-1)
else:
    print(answer)

# def fill_paper2(paper):
#     if not any(1 in row for row in matrix):
#         return 
    
#     if paper == 0:
#         return
    
#     if available[paper] == 0:
#         fill_paper2(paper-1)
#     else:
#         possible, filled_matrix = fill(paper)

#         if possible:
#             origin_matrix = copy.deepcopy(matrix) 
#             matrix = filled_matrix
#             fill_paper2(paper)
#             matrix = origin_matrix
#         else:
#             fill_paper2(paper-1)
            

            


'''
경우맞는거 찾았을때 exit말고 바로 리턴하려면?!
안그러면 모든 경우를 다찾고있음!!
근데 모든경우 봐야한다고할 때 가치지기를 어떻게 할 것인가
행렬카피하고 하는연산이 큰가봐
그냥 판단만하고 채워줘야할거깉이
'''