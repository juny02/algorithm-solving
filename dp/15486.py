N = int(input())
arr = [[0,0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [[0,0] for _ in range(N+1)]
# 첫번재 인덱스에는 가능인덱스
# 두번째 인덱스에는 최댓값

for i in range(1, N+1): # i번째 요소를 채움. dp[i] 를 구함
    for j in range(i): # 그 이전것들이랑 비교함
        if (i+arr[i][0]) <= N+1:
            if dp[j][0] <= i: # 가능하면 지금꺼랑 내꺼 추가한거 비교
                if dp[i][1] < dp[j][1] + arr[i][1]:
                    dp[i][1] = dp[j][1] + arr[i][1]
                    dp[i][0] = i + arr[i][0]

            else: # 불가능하면 지금꺼랑 그 안추가한거 비교
                if dp[i][1] < arr[i][1]:
                    dp[i][1] = arr[i][1]
                    dp[i][0] = i + arr[i][0]
        else:
            if dp[i][1] < dp[j][1]:
                dp[i][1] = dp[j][1]
                dp[i][0] = dp[i][1]
    # print(dp)

print(dp[-1][-1])