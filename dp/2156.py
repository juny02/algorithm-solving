N = int(input())

arr = [int(input()) for _ in range(N)]
if N == 1:
    print(arr[0])
elif N==2:
    print(arr[0]+arr[1])
else:
    dp = [0, arr[0], arr[0]+arr[1]]

    for i in range(2, N):
        dp.append(max(dp[i], dp[i-1]+arr[i], dp[i-2]+arr[i-1]+arr[i]))
    print(dp[N])