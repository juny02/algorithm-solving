from collections import deque

n, k = map(int, input().split())

def bfs(n, k):
    visited = [0] * 100001
    queue = deque([n])
    visited[n] = 1

    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x]-1)
            exit()
        for y in [x+1, x-1, 2*x]:
            if 0 <= y <= 100000 and visited[y] == 0 :
                queue.append(y)
                visited[y] = visited[x]+1

bfs(n, k)

# 0~100 까지면 길이는 101 !!! 주의주의
# 이전 노드의 정보를 배열에 저장해둔다 predecessor 저장하는것처럼 해두낟