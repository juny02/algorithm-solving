N = int(input())
matrix = [[0]*N for _ in range(N)]
answer = 0
row_store = [-1 for _ in range(N)]

def possible(r, c):
    for i in range(r): # 위에 애들에 대해서만 확인하면 됨
        if row_store[i]==c or abs(r-i) == abs(c-row_store[i]):
            return False
    return True


def n_queens(row):
    global answer

    if row == N:
        answer += 1
        return

    for col in range(N):
        if possible(row, col):
            row_store[row] = col
            n_queens(row+1)
            # row_store[row] = -1 # 사실 굳이해줄필요가 없음

n_queens(0)
print(answer)