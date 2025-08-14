N = int(input())
arr = [0]
arr += list(map(int, input().split()))

dp = [0]*(N+1)
for i in range(1, N+1):
    # i개를 살때의 최대 코인 갯수
    for j in range(1, i+1): 
        dp[i] = max(dp[i], dp[i-j]+arr[j])
        
print(dp[-1])