from collections import deque

F, S, G, U, D = map(int, input().split())

queue = deque([S])
count = 0
visited = [-1]*(F+1)
visited[S] = 0

if S==G:
    print(0)
    exit()

while queue:
    v = queue.popleft()
    # print(v)
    for n in [v+U, v-D]:
        if n==G:
            print(visited[v]+1)
            exit()
        elif 1<=n<=F and visited[n]==-1:
            queue.append(n)
            visited[n] = visited[v]+1
    # print(visited)

print("use the stairs")