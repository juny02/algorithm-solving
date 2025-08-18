T = int(input())
arrs = []
for _ in range(T):
    N = int(input())
    arr = [0]
    arr += list(map(int, input().split()))
    arrs.append(arr)

for arr in arrs:
    visited = [False]*(len(arr))
    count = 0
    for i in range(1, len(arr)):
        if not visited[i]:
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = arr[cur]
            count += 1
    print(count)