N = int(input())
MOD = 10007

dp = [[0]*10 for _ in range(N+1)] # 배열 반복할때는 이렇게 하기. *으로 하면 얕은복사 되어서 다 바뀜 -.-
dp[1] = [1] * 10


for i in range(1, N + 1):
    for k in range(0, 10):
        # k로 끝나는 i번째 합을 구한당
        for j in range(k+1): # k까지 ~ ~ 같은거 포함이니까 !
            dp[i][k] += (dp[i - 1][j])%MOD

print((sum(dp[N]))%MOD)
