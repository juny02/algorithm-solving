N = int(input())
dp = [[0]*10]
dp.append([1]*10)
dp[1][0] = 0

MOD = 1000000000

for i in range(2, N+1):
    _arr = [0]*10
    for k in range(10): # 0부터 9
        if k==0:
            _arr[0] = (dp[i-1][1])% MOD # 이건 그냥 그대로라서 MOD적용이 필요가 없을 듯
        elif k==9:
            _arr[9] = (dp[i-1][8])% MOD
        else:
            _arr[k] = (dp[i-1][k-1] + dp[i-1][k+1])% MOD
    dp.append(_arr)


print((sum(dp[N]))%MOD)