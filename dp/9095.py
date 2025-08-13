n = int(input())
inputs = [int(input()) for i in range(n)]


def sol(n):
    dp = [0, 1, 2, 4]

    for i in range(4, n + 1):
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

    print(dp[n])


for i in inputs:
    sol(i)
