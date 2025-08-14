N = int(input())
arr = [[0,0,0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0,0,0] for _ in range(N+1)]
dp[1] = arr[1]

#dp[i] = i번째수에 R/G/B 를 각각 칠햇을 때의 최소 비용

for i in range(2, N+1):
    dp[i][0] = min(dp[i-1][1]+arr[i][0], dp[i-1][2]+arr[i][0])
    dp[i][1] = min(dp[i-1][0]+arr[i][1], dp[i-1][2]+arr[i][1])
    dp[i][2] = min(dp[i-1][0]+arr[i][2], dp[i-1][1]+arr[i][2])

print(min(dp[-1]))