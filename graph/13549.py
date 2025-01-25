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
        for y in [2*x, x+1, x-1]:
            if 0 <= y <= 100000:
                if visited[y] == 0:
                    queue.appendleft(y)
                    if y == 2*x:
                        visited[y] = visited[x] # 이거빼먹으면안됨 0 초니까 그대로가야됨
                    else:  
                        visited[y] = visited[x]+1


bfs(n, k)

'''
방문햇엇어도 그게 더 길게가는 길일 수 있다 왜냐면 x+1 로갓을땐 1인데 x*2로가면 0초걸리는데
+1로 갓으면 이미 visited라 0으로가는걸 카운트안함
=> 방문안한점 이거나, 더 짧게갈수잇는 길 이면! 갱신해줘야함. 짧게간길이니까 

또는 순간이동한거를 무조건 우선적으로 처리하도록 (가중치 0인거를 우선적으로)
큐 맨앞에 넣어줄 수 있다
'''

