import sys
input = sys.stdin.readline

N = int(input())
arr = [[0,0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [0 for _ in range(N+2)]

for i in range(1, N+2):
    dp[i] = max(dp[i-1], dp[i]) # dp[i-1] 은 과거의 최고 기록 !! # dp[i] 는 그날 끝난 상담의 기록값
    # 그리고 이제 내 상담 갱신
    if i<N+1 and arr[i][0]+i <= N+1: # 가능하면
        idx = arr[i][0]+i
        dp[idx] = max(dp[idx], dp[i]+arr[i][1])

print(dp[-1])