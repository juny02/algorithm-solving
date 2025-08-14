N, K = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(N)]

dp=[[0]*(K+1) for _ in range(N+1)]
# i = 0 인 초기상태도 잇어야하므로 N+1

for i in range(1, N+1):
    w, v = data[i-1]
    for k in range(0, K+1): # 지금무게부터 최대 무게까지
        if k-w >= 0:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-w]+v)
        else:
            dp[i][k] = dp[i-1][k]

print(dp[-1][-1])
    
    
    
    
# 잘못된 코드
# dp = [float('-inf')]*(K+1) # 불가능. 을 미리 알려줘야됨
# dp[0] = 0



# for i in range(1, K+1):
#     for k in data.keys():
#         if i-k>=0:
#             dp[i] = max(dp[i-k] + data[k], dp[i])
    
# print(max(dp))    