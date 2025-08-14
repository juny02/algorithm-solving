N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
dp = [float('inf')]*(K+1)

# K까지 도달함
# i수를 만드는 경우의 수가 저장됨
for i in range(1, K+1):
    for num in nums:
        if i == num:
            dp[i] = 1 # 그 숫자들은 코인 1개씩으로 만들 수 있음
        elif i-num > 0:
            dp[i] = min(dp[i], dp[i-num]+1)

if dp[-1] != float('inf'):
    print(dp[-1])
else:
    print(-1)


""" 인덱스 에러가 난 이유는 코인의 값이 K보다 큰게 들어올수도 있기 때문~~ 바부"""