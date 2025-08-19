import sys
input = sys.stdin.readline

N = int(input())
T = [0]
P = [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
dp = [0 for _ in range(N+2)]

for i in range(1, N+1):
    for j in range(T[i]+i, N+1):
        dp[j] = max(dp[j], dp[i]+arr)

